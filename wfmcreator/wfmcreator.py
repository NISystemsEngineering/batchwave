import os
import tempfile
import re
import typing
import wfmcreator.propconst
from .wfmcreator_enums import *


class WaveformCreator:
    def __init__(self):
        self._wc_exe = os.path.join(
            os.environ['ProgramFiles'], 'National Instruments', 'RFmxWaveformCreator', 'BatchWaveformCreationUtility',
            'RFmxBatchWaveformCreationUtility.exe')
        if not os.path.exists(self._wc_exe):
            raise FileNotFoundError('Batch Waveform Creation Utility was not found.'
                                    'Please ensure RFmxNR 20.0 or later is installed.')
        self._out_dir = os.getcwd()
        self._create_only_configs = False
        self._parallel_mode = False
        self._include_description = False
        self._keep_rfws = False
        self._precision = FloatingPointPrecision.SINGLE
        self._log_file_path = os.environ['temp']
        self._wfm_path = None

    @property
    def output_directory(self) -> str:
        return self._out_dir

    @output_directory.setter
    @wfmcreator.propconst.constrain_type(str)
    def output_directory(self, value: str):
        self._out_dir = value

    @property
    def create_only_configs(self) -> bool:
        return self._create_only_configs

    @create_only_configs.setter
    @wfmcreator.propconst.constrain_type(bool)
    def create_only_configs(self, value: bool):
        self._create_only_configs = value

    @property
    def parallel_mode(self) -> bool:
        return self._parallel_mode

    @parallel_mode.setter
    @wfmcreator.propconst.constrain_type(bool)
    def parallel_mode(self, value: bool):
        self._parallel_mode = value

    @property
    def include_description(self) -> bool:
        return self._include_description

    @include_description.setter
    @wfmcreator.propconst.constrain_type(bool)
    def include_description(self, value: bool):
        self._include_description = value

    @property
    def keep_rfws(self) -> bool:
        return self._keep_rfws

    @keep_rfws.setter
    @wfmcreator.propconst.constrain_type(bool)
    def keep_rfws(self, value: bool):
        self._keep_rfws = value

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value: FloatingPointPrecision):
        if not isinstance(value, FloatingPointPrecision):
            raise TypeError('Value must be a Precision enum.')
        self._precision = value

    @property
    def log_file_path(self) -> str:
        return self._log_file_path

    @log_file_path.setter
    @wfmcreator.propconst.constrain_type(str)
    def log_file_path(self, value: str):
        self._log_file_path = value

    @property
    def wfm_path(self):
        """ Returns the path of the most recently generated waveform. """
        return self._wfm_path

    @wfm_path.deleter
    def wfm_path(self):
        self._wfm_path = None

    def _build_flag_list(self):
        flag_list = ['-singlePrecision' if self._precision == FloatingPointPrecision.SINGLE else '-doublePrecision']
        if self._create_only_configs:
            flag_list.append('-createOnlyConfigs')
        if self._parallel_mode:
            flag_list.append('parallelMode')
        if self._include_description:
            flag_list.append('-includeDescription')
        if not self._keep_rfws:
            flag_list.append('-donotKeepRfws')
        return flag_list

    def _find_log_file_paths(self):
        log_paths = []
        candidate_paths = [path for path in os.listdir(self._log_file_path) if path.endswith('.log')]
        try:
            batch_creator_log_path = next(path for path in candidate_paths
                                          if re.match('BatchWaveformCreationUtility', path))
            log_paths.append(os.path.join(self._log_file_path, batch_creator_log_path))
        except StopIteration:
            pass
        try:
            wfm_creator_log_path = next(path for path in candidate_paths if re.match('RFmx Waveform Creator', path))
            log_paths.append(os.path.join(self._log_file_path, wfm_creator_log_path))
        except StopIteration:
            pass
        return log_paths

    def _delete_log_files(self):
        for log_file in self._find_log_file_paths():
            if log_file is not None:
                os.remove(log_file)

    def create(self, wfm_key_values: typing.Iterable[tuple], file_name: str = None):
        tf = tempfile.NamedTemporaryFile(mode='w', dir=self._out_dir, suffix='.csv', delete=False)
        wfm_key_values = list(wfm_key_values)
        if file_name is not None:
            if file_name.endswith('.tdms') or file_name.endswith('.rfws'):
                file_name = os.path.splitext(file_name)[0]
            wfm_key_values.insert(0, ('FileName', file_name))
        keys, values = zip(*wfm_key_values)
        tf.write(','.join(keys) + '\n')
        tf.write(','.join(values))
        tf.close()

        cmd = [f'\"{self._wc_exe}\"', f'\"csvfilepath={tf.name}\"', f'\"outputdirectory={self._out_dir}\"']
        flags = self._build_flag_list()

        # delete previous log files
        self._delete_log_files()

        # execute waveform creator
        cmd.extend(flags)  # add flags to command
        os.system(f'"{" ".join(cmd)}"')
        os.remove(tf.name)

        # if no errors, get generated file path and return
        log_file_paths = self._find_log_file_paths()
        if not log_file_paths:
            if file_name is None:
                return
            self._wfm_path = os.path.splitext(file_name)[0]
            self._wfm_path = self._wfm_path + '.tdms'
            return self._wfm_path

        # handle errors otherwise
        error_message = 'An external error has occurred.'
        for log_file_path in self._find_log_file_paths():
            if log_file_path is not None:
                error_message = error_message + '\n' + f'Log from {log_file_path}:'
                log_file = open(log_file_path)
                with log_file:
                    error_message = error_message + '\n' + log_file.read().strip()
        raise RuntimeError(error_message)

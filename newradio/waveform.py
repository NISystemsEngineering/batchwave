import typing
import wfmcreator.propconst
import wfmcreator.replist
import newradio


class Waveform:
    def __init__(self):
        self._file_name = None
        self._auto_increment_cell_id_enabled = None
        self._num_subblocks = 1
        self._subblocks = wfmcreator.replist.ReplicatingList(newradio.Subblock, 1)

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    @wfmcreator.propconst.constrain_type(str)
    def file_name(self, value: str):
        self._file_name = value

    @file_name.deleter
    def file_name(self):
        self._file_name = None

    @property
    def auto_increment_cell_id_enabled(self) -> bool:
        return self._auto_increment_cell_id_enabled

    @auto_increment_cell_id_enabled.setter
    @wfmcreator.propconst.constrain_type(bool)
    def auto_increment_cell_id_enabled(self, value: bool):
        self._auto_increment_cell_id_enabled = value

    @auto_increment_cell_id_enabled.deleter
    def auto_increment_cell_id_enabled(self):
        self._auto_increment_cell_id_enabled = None

    @property
    def num_subblocks(self) -> int:
        return self._num_subblocks

    @num_subblocks.setter
    @wfmcreator.propconst.constrain_type(int)
    def num_subblocks(self, value: int):
        self._subblocks.extend_to_capacity(value)
        self._num_subblocks = value

    @property
    def subblocks(self) -> typing.List[newradio.Subblock]:
        return self._subblocks

    @subblocks.deleter
    def subblocks(self):
        self._subblocks = wfmcreator.replist.ReplicatingList(newradio.Subblock, 1)
        self._num_subblocks = 1

    def __iter__(self):
        if self._file_name is not None:
            yield 'FileName', self._file_name
        if self._auto_increment_cell_id_enabled is not None:
            yield 'AutoIncrementCellIdEnabled', str(self._auto_increment_cell_id_enabled)
        for i in range(self._num_subblocks):
            yield 'Subblock', str(i)
            for key_val in self._subblocks[i]:
                yield key_val

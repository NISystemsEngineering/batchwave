"""
The example is very verbose and intended to show the majority of configurable settings.
Many settings can be omitted and left as their default values.
Refer to the NI-RFmx Waveform Creator documentation for more information about each parameter.
"""

import rpyc
from wfmcreator import nr  # the nr package is cross platform, we will execute it locally

# open rpyc connection
host_name = 'semoore-sutter'
port = 18861
print(f'Opening connection to {host_name} on port {port}..', end='')
conn = rpyc.connect('semoore-sutter', 18861, config={'allow_all_attrs': True})
print('done')

# upload and re-bind wfmcreator package
print('Configuring remote packages..', end='')
remote_sys = conn.root.import_module('sys')
remote_os_path = conn.root.import_module('os.path')
remote_batchwave_dir = remote_os_path.join(remote_sys.path[0], 'batchwave')
if remote_batchwave_dir not in remote_sys.path:
    remote_sys.path.append(remote_sys.path.append(remote_batchwave_dir))
print('done')

# import remote packages
print('Importing remote packages..', end='')
NIRfsg = conn.root.NIRfsg
NIRfsgPlayback = conn.root.NIRfsgPlayback
wfmcreator = conn.root.import_module('wfmcreator')  # the wfmcreator package is windows only
print('done')

# rfsg settings
resource_name = 'BCN_01'
center_freq = 6.5e9  # Hz
power_level = -10.0  # dBm
external_attenuation = 0.0  # dB
selected_ports = 'if0'
frequency_reference_source = NIRfsg.RfsgFrequencyReferenceSource.OnboardClock
frequency_reference_frequency = 10e6  # Hz
marker_event_output_terminal = NIRfsg.RfsgMarkerEventExportedOutputTerminal.PxiTriggerLine0

print('Configuring waveform..', end='')

# waveform
nrw = nr.Waveform()
file_name = 'nr_waveform.rfws'
nrw.auto_increment_cell_id_enabled = True

# subblock
subblock = nrw.subblocks[0]
subblock.offset = 0.0
subblock.spacing_type = nr.SubblockSpacingType.NOMINAL
subblock.reference_cc_index = -1

# carrier
carrier = subblock.carriers[0]
carrier.cell_id = 0
carrier.channel_bandwidth = 100e6
carrier.frequency_range = nr.FrequencyRange.RANGE_1
carrier.link_direction = nr.LinkDirection.UPLINK
carrier.downlink_channel_configuration_mode = nr.DownlinkChannelConfigurationMode.USER_DEFINED
carrier.downlink_test_model = nr.DownlinkTestModel.TM1_1
carrier.downlink_test_model_duplex_scheme = nr.DownlinkTestModelDuplexScheme.FDD
carrier.bandwidth_part_subcarrier_spacing = 30e3

# pusch
pusch = carrier.pusch[0]
pusch.rb_allocation = '0:last'
pusch.slot_allocation = '0:last'
pusch.symbol_allocation = '0:last'
pusch.modulation_type = nr.PuschModulationType.QAM256
pusch.mapping_type = nr.PuschMappingType.TYPE_A
pusch.dmrs_duration = nr.PuschDmrsDuration.SINGLE_SYMBOL
pusch.dmrs_configuration = nr.PuschDmrsConfiguration.TYPE_1
pusch.dmrs_additional_positions = 0
pusch.dmrs_type_a_position = 2
pusch.transform_precoding_enabled = False
pusch.dmrs_release_version = nr.PuschDmrsReleaseVersion.RELEASE_15
pusch.number_of_cdm_groups = 1

# pdsch
pdsch = carrier.pdsch[0]
pdsch.rb_allocation = '0:last'
pdsch.slot_allocation = '0:last'
pdsch.symbol_allocation = '0:last'
pdsch.modulation_type = nr.PdschModulationType.QAM256
pdsch.mapping_type = nr.PdschMappingType.TYPE_A
pdsch.dmrs_duration = nr.PdschDmrsDuration.SINGLE_SYMBOL
pdsch.dmrs_configuration = nr.PdschDmrsConfiguration.TYPE_1
pdsch.dmrs_additional_positions = 0
pdsch.dmrs_type_a_position = 2
pdsch.transform_precoding_enabled = False
pdsch.dmrs_release_version = nr.PdschDmrsReleaseVersion.RELEASE_15
pdsch.number_of_cdm_groups = 1

print('done')
print('Creating waveform..', end='')

# invoke waveform creator
wc = wfmcreator.WaveformCreator()
wfm_path = wc.create(list(nrw), file_name=file_name)

print('done')
print('Opening instrument session..', end='')

# open instrument session
rfsg = NIRfsg.NIRfsg(resource_name, True, False)
rfsg_handle = rfsg.GetInstrumentHandle().DangerousGetHandle()
rfsg.FrequencyReference.Configure(frequency_reference_source, frequency_reference_frequency)

print('done')
print('Configuring instrument and downloading waveform..', end='')

# configure RF
rfsg.RF.Configure(center_freq, power_level)
rfsg.RF.ExternalGain = -external_attenuation
rfsg.SignalPath.SelectedPorts = selected_ports

# export events
rfsg.DeviceEvents.MarkerEvents[0].ExportedOutputTerminal = marker_event_output_terminal

# download waveform to instrument
NIRfsgPlayback.NIRfsgPlayback.ReadAndDownloadWaveformFromFile(rfsg_handle, wfm_path, 'wfm')
script = 'script exampleScript\nrepeat forever\ngenerate wfm marker0(0)\nend repeat\nend script'
NIRfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsg_handle, script)

print('done')

# initiate and wait on user
rfsg.Initiate()
rfsg.CheckGenerationStatus()

input('Generating dynamic waveform. Press the return key to abort..')
print('Aborting instrument and closing session..', end='')

# stop generation and disable output
rfsg.Abort()
rfsg.RF.OutputEnabled = False

# close sessions
rfsg.Close()

print('done')

"""
This example shows how to create multiple waveforms by sweeping various parameters.
"""

import wfmcreator
from wfmcreator import nr

carrier_counts = [1, 2, 4, 8]
channel_bandwidths = [20e6, 50e6, 100e6]
subcarrier_spacings = [30e3]
modulation_schemes = [nr.PuschModulationType.QPSK, nr.PuschModulationType.QAM16,
                      nr.PuschModulationType.QAM64, nr.PuschModulationType.QAM256]

# waveform
nrw = nr.Waveform()
nrw.auto_increment_cell_id_enabled = True

# waveform creator
wc = wfmcreator.WaveformCreator()

# subblock
subblock = nrw.subblocks[0]
subblock.offset = 0.0
subblock.spacing_type = nr.SubblockSpacingType.NOMINAL
subblock.reference_cc_index = -1

# carrier
for num_carriers in carrier_counts:
    del subblock.carriers
    subblock.carriers.extend_to_capacity(num_carriers)
    for bandwidth in channel_bandwidths:
        for scs in subcarrier_spacings:
            for modulation in modulation_schemes:
                for carrier in subblock.carriers:
                    carrier.cell_id = 0
                    carrier.frequency_range = nr.FrequencyRange.RANGE_1
                    carrier.link_direction = nr.LinkDirection.UPLINK
                    carrier.downlink_channel_configuration_mode = nr.DownlinkChannelConfigurationMode.USER_DEFINED
                    carrier.downlink_test_model = nr.DownlinkTestModel.TM1_1
                    carrier.downlink_test_model_duplex_scheme = nr.DownlinkTestModelDuplexScheme.FDD
                    carrier.channel_bandwidth = bandwidth
                    carrier.bandwidth_part_subcarrier_spacing = scs

                    # pusch
                    pusch = carrier.pusch[0]
                    pusch.rb_allocation = '0:last'
                    pusch.slot_allocation = '0:last'
                    pusch.symbol_allocation = '0:last'
                    pusch.modulation_type = modulation
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

                    # invoke waveform creator
                    file_name = 'NR_CC{:d}_BW_{:.0f}M_SCS_{:.0f}k_Mod_{:s}.tdms'.format(
                        num_carriers, bandwidth / 1e6, scs / 1e3, modulation.name)
                    wfm_path = wc.create(nrw, file_name)

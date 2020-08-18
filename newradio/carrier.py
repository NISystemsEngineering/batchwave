import typing
import wfmcreator.propconst
import wfmcreator.replist
import newradio
from .carrier_enums import *


class Carrier:
    def __init__(self):
        self._cell_id = None
        self._channel_bandwidth = None
        self._frequency_range = None
        self._link_direction = None
        self._downlink_channel_configuration_mode = None
        self._downlink_test_model = None
        self._downlink_test_model_duplex_scheme = None
        self._bandwidth_part_subcarrier_spacing = None
        self._num_pusch = 1
        self._pusch = wfmcreator.replist.ReplicatingList(newradio.Pusch, 1)
        self._num_pdsch = 1
        self._pdsch = wfmcreator.replist.ReplicatingList(newradio.Pdsch, 1)

    @property
    def cell_id(self) -> int:
        return self._cell_id

    @cell_id.setter
    @wfmcreator.propconst.constrain_type(int)
    def cell_id(self, value: int):
        self._cell_id = value

    @cell_id.deleter
    def cell_id(self):
        self._cell_id = None

    @property
    def channel_bandwidth(self) -> float:
        return self._channel_bandwidth

    @channel_bandwidth.setter
    @wfmcreator.propconst.constrain_type(float)
    def channel_bandwidth(self, value: float):
        self._channel_bandwidth = value

    @channel_bandwidth.deleter
    def channel_bandwidth(self):
        self._channel_bandwidth = None

    @property
    def frequency_range(self) -> FrequencyRange:
        return self._frequency_range

    @frequency_range.setter
    @wfmcreator.propconst.constrain_type(FrequencyRange)
    def frequency_range(self, value: FrequencyRange):
        self._frequency_range = value

    @frequency_range.deleter
    def frequency_range(self):
        self._frequency_range = None
    
    @property
    def link_direction(self) -> LinkDirection:
        return self._link_direction
    
    @link_direction.setter
    @wfmcreator.propconst.constrain_type(LinkDirection)
    def link_direction(self, value: LinkDirection):
        self._link_direction = value

    @link_direction.deleter
    def link_direction(self):
        self._link_direction = None

    @property
    def downlink_channel_configuration_mode(self) -> DownlinkChannelConfigurationMode:
        return self._downlink_channel_configuration_mode

    @downlink_channel_configuration_mode.setter
    @wfmcreator.propconst.constrain_type(DownlinkChannelConfigurationMode)
    def downlink_channel_configuration_mode(self, value: DownlinkChannelConfigurationMode):
        self._downlink_channel_configuration_mode = value

    @downlink_channel_configuration_mode.deleter
    def downlink_channel_configuration_mode(self):
        self._downlink_channel_configuration_mode = None

    @property
    def downlink_test_model(self) -> DownlinkTestModel:
        return self._downlink_test_model

    @downlink_test_model.setter
    @wfmcreator.propconst.constrain_type(DownlinkTestModel)
    def downlink_test_model(self, value: DownlinkTestModel):
        self._downlink_test_model = value

    @downlink_test_model.deleter
    def downlink_test_model(self):
        self._downlink_test_model = None

    @property
    def downlink_test_model_duplex_scheme(self) -> DownlinkTestModelDuplexScheme:
        return self._downlink_test_model_duplex_scheme

    @downlink_test_model_duplex_scheme.setter
    @wfmcreator.propconst.constrain_type(DownlinkTestModelDuplexScheme)
    def downlink_test_model_duplex_scheme(self, value: DownlinkTestModelDuplexScheme):
        self._downlink_test_model_duplex_scheme = value

    @downlink_test_model_duplex_scheme.deleter
    def downlink_test_model_duplex_scheme(self):
        self._downlink_test_model = None

    @property
    def bandwidth_part_subcarrier_spacing(self):
        return self._bandwidth_part_subcarrier_spacing

    @bandwidth_part_subcarrier_spacing.setter
    @wfmcreator.propconst.constrain_type(float)
    def bandwidth_part_subcarrier_spacing(self, value):
        self._bandwidth_part_subcarrier_spacing = value

    @bandwidth_part_subcarrier_spacing.deleter
    def bandwidth_part_subcarrier_spacing(self):
        self._bandwidth_part_subcarrier_spacing = None

    @property
    def num_pusch(self):
        return self._pusch

    @num_pusch.setter
    @wfmcreator.propconst.constrain_type(int)
    def num_pusch(self, value):
        self._pusch.extend_to_capacity(value)
        self._num_pusch = value

    @property
    def pusch(self) -> typing.List[newradio.Pusch]:
        return self._pusch

    @pusch.deleter
    def pusch(self):
        self._pusch = wfmcreator.replist.ReplicatingList(newradio.Pusch, 1)
        self._num_pusch = 1

    @property
    def num_pdsch(self):
        return self._num_pdsch

    @num_pdsch.setter
    @wfmcreator.propconst.constrain_type(int)
    def num_pdsch(self, value):
        self._pdsch.extend_to_capacity(value)
        self._num_pdsch = value

    @property
    def pdsch(self) -> typing.List[newradio.Pdsch]:
        return self._pdsch

    @pdsch.deleter
    def pdsch(self):
        self._pdsch = wfmcreator.replist.ReplicatingList(newradio.Pdsch, 1)
        self._num_pdsch = 1

    def __iter__(self):
        if self._cell_id is not None:
            yield 'CellID', str(self._cell_id)
        if self._channel_bandwidth is not None:
            yield 'ChannelBandwidth', '{:.0f}M'.format(self._channel_bandwidth / 1e6)
        if self._frequency_range is not None:
            yield 'FrequencyRange', self._frequency_range.value
        if self._link_direction is not None:
            yield 'LinkDirection', self._link_direction.value
        if self._downlink_channel_configuration_mode is not None:
            yield 'DownlinkChannelConfigurationMode', self._downlink_channel_configuration_mode.value
        if self._downlink_test_model is not None:
            yield 'DownlinkTestModel', self._downlink_test_model.value
        if self._downlink_test_model_duplex_scheme is not None:
            yield 'DownlinkTestModelDuplexScheme', self._downlink_test_model_duplex_scheme.value
        if self._bandwidth_part_subcarrier_spacing is not None:
            yield 'BandwidthPartSubcarrierSpacing', '{:.0f}k'.format(self._bandwidth_part_subcarrier_spacing / 1e3)
        yield 'User', '0'
        for i in range(self._num_pusch):
            yield 'PUSCH', str(i)
            for key_val in self._pusch[i]:
                yield key_val
        for i in range(self._num_pdsch):
            yield 'PDSCH', str(i)
            for key_val in self._pdsch[i]:
                yield key_val

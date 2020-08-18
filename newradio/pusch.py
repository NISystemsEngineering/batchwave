import wfmcreator.propconst
from .pusch_enums import *


class Pusch:
    def __init__(self):
        self._rb_allocation = None
        self._slot_allocation = None
        self._symbol_allocation = None
        self._modulation_type = None
        self._mapping_type = None
        self._dmrs_duration = None
        self._dmrs_configuration = None
        self._dmrs_additional_positions = None
        self._dmrs_type_a_position = None
        self._transform_precoding_enabled = None
        self._dmrs_release_version = None
        self._number_of_cdm_groups = None

    @property
    def rb_allocation(self) -> str:
        return self._rb_allocation

    @rb_allocation.setter
    @wfmcreator.propconst.constrain_type(str)
    def rb_allocation(self, value: str):
        self._rb_allocation = value

    @rb_allocation.deleter
    def rb_allocation(self):
        self._rb_allocation = None

    @property
    def slot_allocation(self) -> str:
        return self._slot_allocation

    @slot_allocation.setter
    @wfmcreator.propconst.constrain_type(str)
    def slot_allocation(self, value: str):
        self._slot_allocation = value

    @slot_allocation.deleter
    def slot_allocation(self):
        self._slot_allocation = None

    @property
    def symbol_allocation(self) -> str:
        return self._symbol_allocation

    @symbol_allocation.setter
    @wfmcreator.propconst.constrain_type(str)
    def symbol_allocation(self, value: str):
        self._symbol_allocation = value

    @symbol_allocation.deleter
    def symbol_allocation(self):
        self._symbol_allocation = None

    @property
    def modulation_type(self) -> PuschModulationType:
        return self._modulation_type

    @modulation_type.setter
    @wfmcreator.propconst.constrain_type(PuschModulationType)
    def modulation_type(self, value: PuschModulationType):
        self._modulation_type = value

    @modulation_type.deleter
    def modulation_type(self):
        self._modulation_type = None

    @property
    def mapping_type(self) -> PuschMappingType:
        return self._mapping_type

    @mapping_type.setter
    @wfmcreator.propconst.constrain_type(PuschMappingType)
    def mapping_type(self, value: PuschMappingType):
        self._mapping_type = value

    @mapping_type.deleter
    def mapping_type(self):
        self._mapping_type = None

    @property
    def dmrs_duration(self) -> PuschDmrsDuration:
        return self._dmrs_duration

    @dmrs_duration.setter
    @wfmcreator.propconst.constrain_type(PuschDmrsDuration)
    def dmrs_duration(self, value: PuschDmrsDuration):
        self._dmrs_duration = value

    @dmrs_duration.deleter
    def dmrs_duration(self):
        self._dmrs_duration = None

    @property
    def dmrs_configuration_type(self) -> PuschDmrsConfiguration:
        return self._dmrs_configuration

    @dmrs_configuration_type.setter
    @wfmcreator.propconst.constrain_type(PuschDmrsConfiguration)
    def dmrs_configuration_type(self, value: PuschDmrsConfiguration):
        self._dmrs_configuration = value

    @dmrs_configuration_type.deleter
    def dmrs_configuration_type(self):
        self._dmrs_configuration = None

    @property
    def dmrs_additional_positions(self) -> int:
        return self._dmrs_additional_positions

    @dmrs_additional_positions.setter
    @wfmcreator.propconst.constrain_type(int)
    def dmrs_additional_positions(self, value: int):
        self._dmrs_additional_positions = value

    @dmrs_additional_positions.deleter
    def dmrs_additional_positions(self):
        self._dmrs_additional_positions = None

    @property
    def dmrs_type_a_position(self) -> int:
        return self._dmrs_type_a_position

    @dmrs_type_a_position.setter
    @wfmcreator.propconst.constrain_type(int)
    def dmrs_type_a_position(self, value: int):
        self._dmrs_type_a_position = value

    @dmrs_type_a_position.deleter
    def dmrs_type_a_position(self):
        self._dmrs_type_a_position = None

    @property
    def transform_precoding_enabled(self) -> bool:
        return self._transform_precoding_enabled

    @transform_precoding_enabled.setter
    @wfmcreator.propconst.constrain_type(bool)
    def transform_precoding_enabled(self, value: bool):
        self._transform_precoding_enabled = value

    @transform_precoding_enabled.deleter
    def transform_precoding_enabled(self):
        self._transform_precoding_enabled = None

    @property
    def dmrs_release_version(self) -> PuschDmrsReleaseVersion:
        return self._dmrs_release_version

    @dmrs_release_version.setter
    @wfmcreator.propconst.constrain_type(PuschDmrsReleaseVersion)
    def dmrs_release_version(self, value: PuschDmrsReleaseVersion):
        self._dmrs_release_version = value

    @dmrs_release_version.deleter
    def dmrs_release_version(self):
        self._dmrs_release_version = None

    @property
    def number_of_cdm_groups(self) -> int:
        return self._number_of_cdm_groups

    @number_of_cdm_groups.setter
    @wfmcreator.propconst.constrain_type(int)
    def number_of_cdm_groups(self, value: int):
        self._number_of_cdm_groups = value

    @number_of_cdm_groups.deleter
    def number_of_cdm_groups(self):
        self._number_of_cdm_groups = None

    def __iter__(self):
        if self._rb_allocation is not None:
            yield 'PUSCHRBAllocation', self._rb_allocation
        if self._slot_allocation is not None:
            yield 'PUSCHSlotAllocation', self._slot_allocation
        if self._symbol_allocation is not None:
            yield 'PUSCHSymbolAllocation', self._symbol_allocation
        if self._modulation_type is not None:
            yield 'PUSCHModulationType', self._modulation_type.value
        if self._mapping_type is not None:
            yield 'PUSCHMappingType', self._mapping_type.value
        if self._dmrs_duration is not None:
            yield 'PUSCHDMRSDuration', self._dmrs_duration.value
        if self._dmrs_configuration is not None:
            yield 'PUSCHDMRSConfigurationType', self._dmrs_configuration.value
        if self._dmrs_additional_positions is not None:
            yield 'PUSCHDMRSAdditionalPositions', str(self._dmrs_additional_positions)
        if self._dmrs_type_a_position is not None:
            yield 'PUSCHDMRSTypeAPosition', str(self._dmrs_type_a_position)
        if self._transform_precoding_enabled is not None:
            yield 'PUSCHTransformPrecodingEnabled', str(self._transform_precoding_enabled)
        if self._dmrs_release_version is not None:
            yield 'PUSCHDmrsReleaseVersion', self._dmrs_release_version.value
        if self._number_of_cdm_groups is not None:
            yield 'PUSCHNumberOfCDMGroups', str(self._number_of_cdm_groups)

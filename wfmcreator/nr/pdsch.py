from ..propconst import constrain_type
from .pdsch_enums import *


class Pdsch:
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
        self._dmrs_release_version = None
        self._number_of_cdm_groups = None

    @property
    def rb_allocation(self) -> str:
        return self._rb_allocation

    @rb_allocation.setter
    @constrain_type(str)
    def rb_allocation(self, value: str):
        self._rb_allocation = value

    @rb_allocation.deleter
    def rb_allocation(self):
        self._rb_allocation = None

    @property
    def slot_allocation(self) -> str:
        return self._slot_allocation

    @slot_allocation.setter
    @constrain_type(str)
    def slot_allocation(self, value: str):
        self._slot_allocation = value

    @slot_allocation.deleter
    def slot_allocation(self):
        self._slot_allocation = None

    @property
    def symbol_allocation(self) -> str:
        return self._symbol_allocation

    @symbol_allocation.setter
    @constrain_type(str)
    def symbol_allocation(self, value: str):
        self._symbol_allocation = value

    @symbol_allocation.deleter
    def symbol_allocation(self):
        self._symbol_allocation = None

    @property
    def modulation_type(self) -> PdschModulationType:
        return self._modulation_type

    @modulation_type.setter
    @constrain_type(PdschModulationType)
    def modulation_type(self, value: PdschModulationType):
        self._modulation_type = value

    @modulation_type.deleter
    def modulation_type(self):
        self._modulation_type = None

    @property
    def mapping_type(self) -> PdschMappingType:
        return self._mapping_type

    @mapping_type.setter
    @constrain_type(PdschMappingType)
    def mapping_type(self, value: PdschMappingType):
        self._mapping_type = value

    @mapping_type.deleter
    def mapping_type(self):
        self._mapping_type = None

    @property
    def dmrs_duration(self) -> PdschDmrsDuration:
        return self._dmrs_duration

    @dmrs_duration.setter
    @constrain_type(PdschDmrsDuration)
    def dmrs_duration(self, value: PdschDmrsDuration):
        self._dmrs_duration = value

    @dmrs_duration.deleter
    def dmrs_duration(self):
        self._dmrs_duration = None

    @property
    def dmrs_configuration_type(self) -> PdschDmrsConfiguration:
        return self._dmrs_configuration

    @dmrs_configuration_type.setter
    @constrain_type(PdschDmrsConfiguration)
    def dmrs_configuration_type(self, value: PdschDmrsConfiguration):
        self._dmrs_configuration = value

    @dmrs_configuration_type.deleter
    def dmrs_configuration_type(self):
        self._dmrs_configuration = None

    @property
    def dmrs_additional_positions(self) -> int:
        return self._dmrs_additional_positions

    @dmrs_additional_positions.setter
    @constrain_type(int)
    def dmrs_additional_positions(self, value: int):
        self._dmrs_additional_positions = value

    @dmrs_additional_positions.deleter
    def dmrs_additional_positions(self):
        self._dmrs_additional_positions = None

    @property
    def dmrs_type_a_position(self) -> int:
        return self._dmrs_type_a_position

    @dmrs_type_a_position.setter
    @constrain_type(int)
    def dmrs_type_a_position(self, value: int):
        self._dmrs_type_a_position = value

    @dmrs_type_a_position.deleter
    def dmrs_type_a_position(self):
        self._dmrs_type_a_position = None

    @property
    def dmrs_release_version(self) -> PdschDmrsReleaseVersion:
        return self._dmrs_release_version

    @dmrs_release_version.setter
    @constrain_type(PdschDmrsReleaseVersion)
    def dmrs_release_version(self, value: PdschDmrsReleaseVersion):
        self._dmrs_release_version = value

    @dmrs_release_version.deleter
    def dmrs_release_version(self):
        self._dmrs_release_version = None

    @property
    def number_of_cdm_groups(self) -> int:
        return self._number_of_cdm_groups

    @number_of_cdm_groups.setter
    @constrain_type(int)
    def number_of_cdm_groups(self, value: int):
        self._number_of_cdm_groups = value

    @number_of_cdm_groups.deleter
    def number_of_cdm_groups(self):
        self._number_of_cdm_groups = None

    def __iter__(self):
        if self._rb_allocation is not None:
            yield 'PDSCHRBAllocation', self._rb_allocation
        if self._slot_allocation is not None:
            yield 'PDSCHSlotAllocation', self._slot_allocation
        if self._symbol_allocation is not None:
            yield 'PDSCHSymbolAllocation', self._symbol_allocation
        if self._modulation_type is not None:
            yield 'PDSCHModulationType', self._modulation_type.value
        if self._mapping_type is not None:
            yield 'PDSCHMappingType', self._mapping_type.value
        if self._dmrs_duration is not None:
            yield 'PDSCHDMRSDuration', self._dmrs_duration.value
        if self._dmrs_configuration is not None:
            yield 'PDSCHDMRSConfigurationType', self._dmrs_configuration.value
        if self._dmrs_additional_positions is not None:
            yield 'PDSCHDMRSAdditionalPositions', str(self._dmrs_additional_positions)
        if self._dmrs_type_a_position is not None:
            yield 'PDSCHDMRSTypeAPosition', str(self._dmrs_type_a_position)
        if self._dmrs_release_version is not None:
            yield 'PDSCHDmrsReleaseVersion', self._dmrs_release_version.value
        if self._number_of_cdm_groups is not None:
            yield 'PDSCHNumberOfCDMGroups', str(self._number_of_cdm_groups)

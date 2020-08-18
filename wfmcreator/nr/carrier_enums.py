import enum


class FrequencyRange(enum.Enum):
    RANGE_1 = 'Range 1'
    RANGE_2 = 'Range 2'


class LinkDirection(enum.Enum):
    DOWNLINK = 'Downlink'
    UPLINK = 'Uplink'


class DownlinkChannelConfigurationMode(enum.Enum):
    USER_DEFINED = 'User Defined'
    TEST_MODEL = 'Test Model'


class DownlinkTestModel(enum.Enum):
    TM1_1 = 'TM1.1'
    TM1_2 = 'TM1.2'
    TM2 = 'TM2'
    TM2A = 'TM2a'
    TM3_1 = 'TM3.1'
    TM3_1A = 'TM3.1a'
    TM3_2 = 'TM3.2'
    TM3_3 = 'TM3.3'


class DownlinkTestModelDuplexScheme(enum.Enum):
    FDD = 'FDD'
    TDD = 'TDD'



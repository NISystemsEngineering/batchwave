from enum import Enum


class PdschModulationType(Enum):
    PI_OVER_2_BPSK = 'PI/2 BPSK'
    BPSK = 'BPSK'
    QPSK = 'QPSK'
    QAM16 = 'QAM16'
    QAM64 = 'QAM64'
    QAM256 = 'QAM256'


class PdschMappingType(Enum):
    TYPE_A = 'Type A'
    TYPE_B = 'Type B'


class PdschDmrsDuration(Enum):
    SINGLE_SYMBOL = 'Single Symbol'
    DOUBLE_SYMBOL = 'Double Symbol'


class PdschDmrsConfiguration(Enum):
    TYPE_1 = 'Type 1'
    TYPE_2 = 'Type 2'


class PdschDmrsReleaseVersion(Enum):
    RELEASE_15 = '3GPP Release 15'
    RELEASE_16 = '3GPP Release 16'



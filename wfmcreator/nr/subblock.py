import typing
from ..propconst import constrain_type
from ..replist import ReplicatingList
from .carrier import Carrier
from .subblock_enums import *


class Subblock:
    def __init__(self):
        self._offset = None
        self._spacing_type = None
        self._reference_cc_index = None
        self._num_carriers = 1
        self._carriers = ReplicatingList(Carrier, 1)

    @property
    def offset(self) -> float:
        return self._offset

    @offset.setter
    @constrain_type(float)
    def offset(self, value: float):
        self._offset = value

    @offset.deleter
    def offset(self):
        self._offset = None

    @property
    def spacing_type(self) -> SubblockSpacingType:
        return self._spacing_type

    @spacing_type.setter
    @constrain_type(SubblockSpacingType)
    def spacing_type(self, value: SubblockSpacingType):
        self._spacing_type = value

    @spacing_type.deleter
    def spacing_type(self):
        self._spacing_type = None

    @property
    def reference_cc_index(self) -> int:
        return self._reference_cc_index

    @reference_cc_index.setter
    @constrain_type(int)
    def reference_cc_index(self, value: int):
        self._reference_cc_index = value

    @reference_cc_index.deleter
    def reference_cc_index(self):
        self._reference_cc_index = None

    @property
    def num_carriers(self) -> int:
        return self._num_carriers

    @num_carriers.setter
    @constrain_type(int)
    def num_carriers(self, value: int):
        self._carriers.extend_to_capacity(value)
        self._num_carriers = value

    @property
    def carriers(self) -> typing.List[Carrier]:
        return self._carriers

    @carriers.deleter
    def carriers(self):
        self._carriers = ReplicatingList(Carrier, 1)
        self._num_carriers = 1

    def __iter__(self):
        if self._offset is not None:
            yield 'SubblockOffset', str(self._offset)
        if self._spacing_type is not None:
            yield 'SubblockSpacingType', str(self._spacing_type.value)
        if self._reference_cc_index is not None:
            yield 'SubblockReferenceCCIndex', str(self._reference_cc_index)
        for i in range(self._num_carriers):
            yield 'Carrier', str(i)
            for key_val in self._carriers[i]:
                yield key_val

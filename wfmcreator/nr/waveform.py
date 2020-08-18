import typing
from ..propconst import constrain_type
from ..replist import ReplicatingList
from .subblock import Subblock


class Waveform:
    def __init__(self):
        self._auto_increment_cell_id_enabled = None
        self._num_subblocks = 1
        self._subblocks = ReplicatingList(Subblock, 1)

    @property
    def auto_increment_cell_id_enabled(self) -> bool:
        return self._auto_increment_cell_id_enabled

    @auto_increment_cell_id_enabled.setter
    @constrain_type(bool)
    def auto_increment_cell_id_enabled(self, value: bool):
        self._auto_increment_cell_id_enabled = value

    @auto_increment_cell_id_enabled.deleter
    def auto_increment_cell_id_enabled(self):
        self._auto_increment_cell_id_enabled = None

    @property
    def num_subblocks(self) -> int:
        return self._num_subblocks

    @num_subblocks.setter
    @constrain_type(int)
    def num_subblocks(self, value: int):
        self._subblocks.extend_to_capacity(value)
        self._num_subblocks = value

    @property
    def subblocks(self) -> typing.List[Subblock]:
        return self._subblocks

    @subblocks.deleter
    def subblocks(self):
        self._subblocks = ReplicatingList(Subblock, 1)
        self._num_subblocks = 1

    def __iter__(self):
        if self._auto_increment_cell_id_enabled is not None:
            yield 'AutoIncrementCellIdEnabled', str(self._auto_increment_cell_id_enabled)
        for i in range(self._num_subblocks):
            yield 'Subblock', str(i)
            for key_val in self._subblocks[i]:
                yield key_val

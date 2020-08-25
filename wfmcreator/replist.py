from typing import Callable
import wfmcreator.propconst


class ReplicatingList(list):
    """
    Represents a list that replicates a Callable configuration when getting an element that is out of bounds.
    """
    @wfmcreator.propconst.constrain_type(Callable)
    def __init__(self, callable_type: Callable, callable_args=(), callable_kwargs: dict = None):
        if callable_kwargs is None:
            callable_kwargs = {}
        self._callable = callable_type
        self._args = callable_args
        self._kwargs = callable_kwargs
        super().__init__()

    def __getitem__(self, index):
        self.extend_to_capacity(index + 1)
        return super().__getitem__(index)

    def extend_to_capacity(self, capacity):
        dist_past_bounds = capacity - len(self)
        if dist_past_bounds > 0:
            self.extend([self._callable(*self._args, **self._kwargs)] * dist_past_bounds)

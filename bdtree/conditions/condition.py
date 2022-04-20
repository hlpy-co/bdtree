from abc import ABC, abstractmethod
from typing import Any, Type, Iterable


class Condition(ABC):

    def __init__(self, value: Any):
        super().__init__()
        self._value = value

    @classmethod
    @abstractmethod
    def new(cls, value: Any) -> 'Condition':
        pass

    @classmethod
    @abstractmethod
    def supported_types(cls) -> Iterable[Type]:
        pass

    @abstractmethod
    def evaluate(self, input: Any) -> bool:
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @property
    def value(self) -> Any:
        return self._value


class SizedCondition(Condition):

    @classmethod
    @abstractmethod
    def supported_size(cls) -> int:
        pass

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [set, list]

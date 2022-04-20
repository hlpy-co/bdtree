from typing import Any, Iterable, Type

from bdtree.conditions import Condition


class LessThan(Condition):

    @classmethod
    def new(cls, value: Any) -> Condition:
        return LessThan(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [int, float]

    def evaluate(self, input: Any) -> bool:
        return input < self._value

    def __repr__(self):
        return f"< {self._value}"

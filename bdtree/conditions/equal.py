from typing import Any, Iterable, Type

from bdtree.conditions import Condition


class Equal(Condition):

    @classmethod
    def new(cls, value: Any) -> Condition:
        return Equal(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [object, Any]

    def evaluate(self, input: Any) -> bool:
        return self._value == input

    def __repr__(self):
        return f"== {self._value}"

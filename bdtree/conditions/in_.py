from typing import Any, Iterable, Type, List, Set

from bdtree.conditions import Condition


class In(Condition):

    @classmethod
    def new(cls, value: Any) -> Condition:
        return In(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [Set, Iterable, List, set, list]

    def evaluate(self, input: Any) -> bool:
        return input in self._value

    def __repr__(self):
        return f"in {self._value}"

from typing import Any, Iterable, Type

from bdtree.conditions.condition import SizedCondition, Condition


class BetweenExclude(SizedCondition):

    def __init__(self, value: Any):
        super().__init__(value)
        self.__lower = value[0]
        self.__higher = value[1]

    @classmethod
    def new(cls, value: Any) -> Condition:
        return BetweenExclude(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [list]

    @classmethod
    def supported_size(cls) -> int:
        return 2

    def evaluate(self, input: Any) -> bool:
        return self.__lower < input < self.__higher

    def value(self) -> Any:
        return [self.__lower, self.__higher]

    def __repr__(self):
        return f"between ({self.__lower}..{self.__higher})"
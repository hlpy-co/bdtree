from abc import ABC, abstractmethod
from typing import Any, Set, Type, Iterable, List


class Condition(ABC):

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


class SizedCondition(Condition):

    @classmethod
    @abstractmethod
    def supported_size(cls) -> int:
        pass

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [set, list]


class Equal(Condition):

    def __init__(self, value: Any):
        super().__init__()
        self.__value = value

    @classmethod
    def new(cls, value: Any) -> Condition:
        return Equal(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [object, Any]

    def evaluate(self, input: Any) -> bool:
        return self.__value == input

    def __repr__(self):
        return f"== {self.__value}"


class GreaterThan(Condition):

    def __init__(self, value: Any):
        super().__init__()
        self.__value = value

    @classmethod
    def new(cls, value: Any) -> Condition:
        return GreaterThan(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [int, float]

    def evaluate(self, input: Any) -> bool:
        return input > self.__value

    def __repr__(self):
        return f"> {self.__value}"


class GreaterThanOrEqual(Condition):

    def __init__(self, value: Any):
        super().__init__()
        self.__value = value

    @classmethod
    def new(cls, value: Any) -> Condition:
        return GreaterThanOrEqual(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [int, float]

    def evaluate(self, input: Any) -> bool:
        return input >= self.__value

    def __repr__(self):
        return f">= {self.__value}"


class LessThan(Condition):

    def __init__(self, value: Any):
        super().__init__()
        self.__value = value

    @classmethod
    def new(cls, value: Any) -> Condition:
        return LessThan(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [int, float]

    def evaluate(self, input: Any) -> bool:
        return input < self.__value

    def __repr__(self):
        return f"< {self.__value}"


class LessThanOrEqual(Condition):

    def __init__(self, value: Any):
        super().__init__()
        self.__value = value

    @classmethod
    def new(cls, value: Any) -> Condition:
        return LessThanOrEqual(value)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [int, float]

    def evaluate(self, input: Any) -> bool:
        return input <= self.__value

    def __repr__(self):
        return f"<= {self.__value}"


class BetweenInclude(SizedCondition):

    def __init__(self, lower: Any, higher):
        super().__init__()
        self.__lower = lower
        self.__higher = higher

    @classmethod
    def new(cls, value: Any) -> Condition:
        lower = value[0]
        higher = value[1]
        return BetweenInclude(lower, higher)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [list]

    @classmethod
    def supported_size(cls) -> int:
        return 2

    def evaluate(self, input: Any) -> bool:
        return self.__lower <= input <= self.__higher

    def __repr__(self):
        return f"between [{self.__lower}..{self.__higher}]"


class BetweenExclude(SizedCondition):

    def __init__(self, lower: Any, higher):
        super().__init__()
        self.__lower = lower
        self.__higher = higher

    @classmethod
    def new(cls, value: Any) -> Condition:
        lower = value[0]
        higher = value[1]
        return BetweenExclude(lower, higher)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [list]

    @classmethod
    def supported_size(cls) -> int:
        return 2

    def evaluate(self, input: Any) -> bool:
        return self.__lower < input < self.__higher

    def __repr__(self):
        return f"between ({self.__lower}..{self.__higher})"


class In(Condition):

    def __init__(self, value: Any):
        super().__init__()
        self.__value = value

    @classmethod
    def new(cls, value: Any) -> Condition:
        lower = value[0]
        higher = value[1]
        return BetweenExclude(lower, higher)

    @classmethod
    def supported_types(cls) -> Iterable[Type]:
        return [Set, Iterable, List, set, list]

    def evaluate(self, input: Any) -> bool:
        return input in set(self.__value)

    def __repr__(self):
        return f"in {self.__value}"

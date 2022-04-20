from abc import ABC, abstractmethod
from typing import Dict, Type, Any, Iterable, TypeVar, Generic

from bdtree import BdTree
from ..condition import Condition, Equal, GreaterThan, GreaterThanOrEqual, LessThan, LessThanOrEqual, In, \
    SizedCondition, BetweenInclude, BetweenExclude
from ..exceptions import TreeSchemaError

BdTreeReaderInput = TypeVar("BdTreeReaderInput")


class BdTreeReader(ABC, Generic[BdTreeReaderInput]):

    def __init__(self):
        super().__init__()

        self._operators: Dict[str, Type[Condition]] = {
            '=': Equal,
            '>': GreaterThan,
            '>=': GreaterThanOrEqual,
            '<': LessThan,
            '<=': LessThanOrEqual,
            'IN': In,
            'BETWEEN': BetweenInclude,
            'BETWEEN_INCLUDE_BOUNDARIES': BetweenInclude,
            'BETWEEN_EXCLUDE_BOUNDARIES': BetweenExclude,
        }

    @abstractmethod
    def read(self, input: BdTreeReaderInput) -> BdTree:
        """
        :return:
        :raise TreeSchemaError
        """
        pass

    def _read_condition(self, operator: str, value: Any) -> Condition:
        found_operator = self._operators.get(operator)
        if found_operator is None:
            raise TreeSchemaError(f"The operator '{operator}' is not supported.")

        if not self.__is_supported_type(found_operator.supported_types(), value):
            raise TreeSchemaError(f"The operator '{operator}' not support this type: {type(value)}. "
                                  f"Supported types: {found_operator.supported_types()}")

        if isinstance(found_operator, SizedCondition):
            supported_size = found_operator.supported_size()
            if len(value) != supported_size:
                raise TreeSchemaError(f"The operator '{operator}' supports only "
                                      f"this length: {supported_size}")

        return found_operator.new(value)

    @staticmethod
    def __is_supported_type(supported_types: Iterable[Type], value: Any) -> bool:
        for supported_type in supported_types:
            if isinstance(value, supported_type):
                return True
        return False

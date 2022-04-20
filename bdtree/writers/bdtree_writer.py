from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Type

from bdtree import BdTree, Condition, Equal, GreaterThan, GreaterThanOrEqual, LessThan, LessThanOrEqual, In, \
    BetweenInclude, BetweenExclude

BdTreeWriterOutput = TypeVar("BdTreeWriterOutput")


class BdTreeWriter(ABC, Generic[BdTreeWriterOutput]):

    def __init__(self):
        super().__init__()

        self._operators: Dict[Type[Condition]: str] = {
            Equal: '=',
            GreaterThan: '>',
            GreaterThanOrEqual: '>=',
            LessThan: '<',
            LessThanOrEqual: '<=',
            In: 'IN',
            BetweenInclude: 'BETWEEN',
            BetweenExclude: 'BETWEEN_EXCLUDE_BOUNDARIES',
        }

    @abstractmethod
    def write(self, tree: BdTree) -> BdTreeWriterOutput:
        """
        :return:
        :raise TreeSchemaError
        """
        pass

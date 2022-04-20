from typing import List, Any, Optional

from bdtree import Condition


class BdNode:
    ROOT_KEY = 'root'

    def __init__(self,
                 field: str = ROOT_KEY,
                 condition: Optional[Condition] = None,
                 children: Optional[List['BdNode']] = None,
                 result: Optional[Any] = None):
        self.__field = field
        self.__condition = condition
        self.__children = children
        self.__result = result

    @property
    def field(self) -> str:
        return self.__field

    @property
    def condition(self) -> Optional[Condition]:
        return self.__condition

    @property
    def children(self) -> List['BdNode']:
        return self.__children or []

    @property
    def result(self) -> Optional[Any]:
        return self.__result

    @property
    def is_root(self) -> bool:
        return self.field == self.ROOT_KEY

    @property
    def is_leaf(self) -> bool:
        return len(self.__children) == 0

    def evaluate(self, value: Optional[Any]) -> bool:
        if value is None or self.__condition is None:
            return False
        return self.__condition.evaluate(value)

    def __repr__(self) -> str:
        return f"Node{{" \
               f"condition={self.field} {self.__condition}, " \
               f"children={'some' if len(self.children) > 0 else 'empty'}, " \
               f"result={self.result}" \
               f"}}"

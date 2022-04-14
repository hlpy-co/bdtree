from typing import Any, Dict, Optional

from .node import BdNode


class BdTree:

    def __init__(self, root: BdNode):
        self.__root = root

    def decide(self, input: Dict[str, Any]) -> Optional[Any]:
        return self.__nested_decide(self.__root, input)

    def __nested_decide(self, parent: BdNode, input: Dict[str, Any]) -> Optional[Any]:
        for child in parent.children:
            value = input.get(child.field)

            if child.evaluate(value):
                return child.result if child.is_leaf else self.__nested_decide(child, input)

        return None

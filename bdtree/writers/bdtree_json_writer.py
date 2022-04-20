from typing import Dict, Any

from bdtree import BdTree, BdNode
from bdtree.exceptions import TreeSchemaError
from bdtree.writers import BdTreeWriter
from bdtree.writers.bdtree_writer import BdTreeWriterOutput


class BdTreeJsonWriter(BdTreeWriter[Dict[str, Any]]):

    def write(self, tree: BdTree) -> BdTreeWriterOutput:
        return self.__write_recursive(tree.root)

    def __write_recursive(self, node: BdNode) -> Dict[str, Any]:
        result = {}
        if node.field is not None and not node.is_root:
            result['field'] = node.field
        if node.condition is not None:
            raw_condition = self._operators.get(type(node.condition))
            if raw_condition is None:
                raise TreeSchemaError(f"The condition {node.condition} cannot be serialized.")

            result['condition'] = raw_condition
            result['value'] = node.condition.value
        if node.result is not None:
            result['result'] = node.result

        result['children'] = [self.__write_recursive(child) for child in node.children]
        return result

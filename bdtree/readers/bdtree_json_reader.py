from typing import Dict, Any, Optional

from bdtree import BdTree, BdNode
from bdtree.exceptions import TreeSchemaError
from bdtree.readers import BdTreeReader


class BdTreeJsonReader(BdTreeReader):

    def __init__(self, json: Dict[str, Any]):
        super().__init__()
        self._json = json

    def read(self) -> BdTree:
        return BdTree(self.__read_recursive(self._json))

    def __read_recursive(self, json: Dict[str, Any]) -> BdNode:
        field = self.__process_field(json)
        condition = self._read_condition(
            operator=self.__process_condition(json),
            value=self.__process_value(json),
        ) if field != self.ROOT_KEY else None
        children = self.__process_children(json)
        result = self.__process_result(json)

        processed_children = []
        for child in children:
            processed_children.append(self.__read_recursive(child))

        return BdNode(
            field=field,
            condition=condition,
            children=processed_children,
            result=result,
        )

    def __process_field(self, json: Dict[str, Any]) -> str:
        field = json.get('field', self.ROOT_KEY)
        if field is not None and isinstance(field, str):
            return field
        raise TreeSchemaError(f"The field value {field} must be a string.")

    @staticmethod
    def __process_condition(json: Dict[str, Any]) -> str:
        condition = json.get('condition', '=')
        if condition is not None and isinstance(condition, str):
            return condition
        raise TreeSchemaError(f"The condition {condition} must be a string.")

    @staticmethod
    def __process_value(json: Dict[str, Any]) -> Any:
        value = json.get('value')
        if value is not None:
            return value
        raise TreeSchemaError(f"The condition value must not be null.")

    @staticmethod
    def __process_children(json: Dict[str, Any]) -> list:
        children = json.get('children', [])
        if children is not None and isinstance(children, list):
            return children
        raise TreeSchemaError(f"The children must be a list.")

    @staticmethod
    def __process_result(json: Dict[str, Any]) -> Optional[Any]:
        return json.get('result')

import json
import unittest

from bdtree.exceptions import TreeSchemaError
from bdtree.readers import BdTreeJsonReader


class TestBdTreeJsonReader(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        with open('tests/assets/valid_tree.json', 'r') as file:
            self.valid_json = json.loads(file.read())

        with open('tests/assets/invalid_tree.json', 'r') as file:
            self.invalid_json = json.loads(file.read())

        self.json_reader = BdTreeJsonReader()

    def test_read_valid_json(self):
        result = self.json_reader.read(self.valid_json)
        print(result)

    def test_read_invalid_json(self):
        with self.assertRaises(TreeSchemaError):
            self.json_reader.read(self.invalid_json)


if __name__ == '__main__':
    unittest.main()

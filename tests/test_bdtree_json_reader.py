import json
import unittest

from bdtree.readers import BdTreeJsonReader


class TestBdTreeJsonReader(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        with open('tests/assets/valid_tree.json', 'r') as file:
            self.valid_json = json.loads(file.read())

        with open('tests/assets/invalid_tree.json', 'r') as file:
            self.invalid_json = json.loads(file.read())

        self.json_reader = BdTreeJsonReader(self.valid_json)

    def test_read(self):
        result = self.json_reader.read()
        print(result)


if __name__ == '__main__':
    unittest.main()

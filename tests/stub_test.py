import unittest

from bdtree import hello_world


class StubTest(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello world")

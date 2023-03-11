from Unit_testing import rearange
import unittest

class TestRearange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada, Lovelace"
        self.assertEqual(rearange(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearange(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearange(testcase), expected)

    def test_single_name(self):
        testcase = "Vanko"
        expected = "Vanko"
        self.assertEqual(rearange(testcase), expected)



unittest.main()


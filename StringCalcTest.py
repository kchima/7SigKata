import unittest
from StringCalc import TDDKata

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.calculator = TDDKata()

    def test_zero(self):
        self.assertEqual(self.calculator.string_calc("0"), 0)

    def test_empty_string(self):
        self.assertEqual(self.calculator.string_calc(""), 0)

    def test_one(self):
        self.assertEqual(self.calculator.string_calc("1"), 1)

if __name__ == '__main__':
    unittest.main()
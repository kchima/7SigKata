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

    def test_twos(self):
        self.assertEqual(self.calculator.string_calc("2"), 2)

    def test_multi(self):
        self.assertEqual(self.calculator.string_calc("1,2"), 3)

    def test_big_multi(self):
        self.assertEqual(self.calculator.string_calc("10, 0, 0, 9, 1, 2, 8, 7, 6, 3, 4, 5"), 55)

    def test_newline_delimeter(self):
        self.assertEqual(self.calculator.string_calc("1\n2"), 3)

    def test_dynamic_delimeter(self):
        self.assertEqual(self.calculator.string_calc('//;\n1;2'), 3)

if __name__ == '__main__':
    unittest.main()
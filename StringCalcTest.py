import unittest
from StringCalc import TDDKata

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.calculator = TDDKata()

    def test_upper(self):
        self.assertEqual(self.calculator.string_calc("0"), 0)

if __name__ == '__main__':
    unittest.main()
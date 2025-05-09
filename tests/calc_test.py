import unittest
from decimal import Decimal

from decimal_calculator.utils import process_and_calc, calc_vars, process_set_var


class CalcTest(unittest.TestCase):
    def test_first_calc(self):
        self.assertEqual(Decimal("0.5"), process_and_calc("3/6"))

    def test_function_calc(self):
        self.assertEqual(Decimal("8.33"), process_and_calc("25.sqrt() + 3.33"))

    def test_no_import(self):
        try:
            process_and_calc("import os")
        except RuntimeError as e:
            self.assertEqual(str(e), "Import is not supported")

    def test_last_result(self):
        calc_vars["_"] = Decimal("0.5")
        self.assertEqual(Decimal("0.5"), process_and_calc("3/6"))

    def test_last_result_with_space(self):
        calc_vars["_"] = Decimal("3")
        self.assertEqual(Decimal("0.5"), process_and_calc("_/6"))
        self.assertEqual(Decimal("1"), process_and_calc(" _ + 0.5"))

    def test_decode_set_var(self):
        process_set_var("a = 5, b=6")
        self.assertEqual(calc_vars["a"], Decimal("5"))
        self.assertEqual(calc_vars["b"], Decimal("6"))

    def test_decode_set_complex_var(self):
        process_set_var("f=10**30")
        self.assertEqual(calc_vars["f"], Decimal(10) ** Decimal(30))
        process_set_var("a=25.sqrt()")
        self.assertEqual(calc_vars["a"], Decimal(5))
        process_set_var("m=25.sqrt(), n=10**2")
        self.assertEqual(calc_vars["m"], Decimal(5))
        self.assertEqual(calc_vars["n"], Decimal(100))

    def test_calc_with_complex_var(self):
        process_set_var("a=10**30")
        process_set_var("b=1000")
        self.assertEqual(Decimal("1000000000000000000000000001000"), process_and_calc("a+b"))
        self.assertEqual(Decimal("100"), process_and_calc("a/10**28"))

    def test_decode_set_var_numeric_name(self):
        try:
            process_set_var("33 = 5")
        except RuntimeError as e:
            self.assertEqual(str(e), "Various name can not be numeric")

    def test_use_var(self):
        process_and_calc("a = 5, b=6")
        self.assertEqual(Decimal("8"), process_and_calc("a+3"))
        self.assertEqual(Decimal("11"), process_and_calc("a+b"))

    def test_use_same_name_var(self):
        process_and_calc("sqrt=6")
        self.assertEqual(Decimal("8"), process_and_calc("sqrt+4.sqrt()"))

    def test_last_result_with_name(self):
        process_and_calc("1+2")
        process_and_calc("a_ = 4")

        self.assertEqual(Decimal("7"), process_and_calc("a_ + _"))

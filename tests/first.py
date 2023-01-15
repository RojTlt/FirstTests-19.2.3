import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calc_correct(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calc_correct(self):
        assert self.calc.subtraction(self, 2023, 2022) == 1

    def test_adding_calc_correct(self):
        assert self.calc.adding(self, 102, 220) == 322

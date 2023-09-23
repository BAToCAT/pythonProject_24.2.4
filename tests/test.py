import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_sum(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_sum(self):
        assert self.calc.subtraction(self, 8, 5) == 3

    def test_multiply_sum(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_adding_sum(self):
        assert self.calc.adding(self, 10, 10) == 20

    def teardown(self):
        print('teardown completed')
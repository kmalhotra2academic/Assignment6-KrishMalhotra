"""
Description: A class used to test the Mortgage class.
Author: Krish Malhotra
Date: November 16, 2024
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixel_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    """Test cases for the Mortgage class."""

    def test_invalid_loan_amount(self):
        with self.assertRaises(ValueError) as context:
            Mortgage(0, 'FIXED_5', 'MONTHLY', 15)
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_invalid_rate(self):
        with self.assertRaises(ValueError) as context:
            Mortgage(100000, 'INVALID_RATE', 'MONTHLY', 15)
        self.assertEqual(str(context.exception), "Rate provided is invalid.")

    def test_invalid_frequency(self):
        with self.assertRaises(ValueError) as context:
            Mortgage(100000, 'FIXED_5', 'INVALID_FREQ', 15)
        self.assertEqual(str(context.exception), "Frequency provided is invalid.")

    def test_invalid_amortization(self):
        with self.assertRaises(ValueError) as context:
            Mortgage(100000, 'FIXED_5', 'MONTHLY', 35)
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")

    def test_valid_inputs(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        self.assertTrue(mortgage)

    def test_set_negative_loan_amount(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -50000
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_set_zero_loan_amount(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_set_positive_loan_amount(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        mortgage.loan_amount = 200000
        self.assertEqual(mortgage.loan_amount, 200000)
    def test_set_valid_rate(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        mortgage.rate = 'FIXED_3'
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_3)

    def test_set_invalid_rate(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        with self.assertRaises(ValueError) as context:
            mortgage.rate = 'INVALID_RATE'
        self.assertEqual(str(context.exception), "Rate provided is invalid.")

    def test_set_valid_frequency(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        mortgage.frequency = 'WEEKLY'
        self.assertEqual(mortgage.frequency, PaymentFrequency.WEEKLY)

    def test_set_invalid_frequency(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        with self.assertRaises(ValueError) as context:
            mortgage.frequency = 'INVALID_FREQ'
        self.assertEqual(str(context.exception), "Frequency provided is invalid.")

    def test_set_valid_amortization(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        mortgage.amortization = 15
        self.assertEqual(mortgage.amortization, 15)

    def test_set_invalid_amortization(self):
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)
        with self.assertRaises(ValueError) as context:
            mortgage.amortization = 35
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")
    
    def test_str_monthly(self):
        mortgage = Mortgage(682912.43, 'FIXED_3', 'MONTHLY', 30)
        expected_output = ("Mortgage Amount: $682,912.43\n"
                           "Rate: 5.89%\n"
                           "Amortization: 30\n"
                           "Frequency: Monthly -- Calculated Payment: $4,046.23")
        self.assertEqual(str(mortgage), expected_output)

    def test_str_biweekly(self):
        mortgage = Mortgage(500000, 'VARIABLE_5', 'BI_WEEKLY', 20)
        output = str(mortgage)
        self.assertIn("Rate: 6.49%", output)  # Check for specific format

    def test_str_weekly(self):
        mortgage = Mortgage(300000, 'FIXED_1', 'WEEKLY', 15)
        output = str(mortgage)
        self.assertIn("Frequency: Weekly", output)  # Check for specific format

    def test_repr(self):
        mortgage = Mortgage(682912.43, 'FIXED_1', 'MONTHLY', 30)
        expected_output = "Mortgage(682912.43, 0.0599, 12, 30)"
        self.assertEqual(repr(mortgage), expected_output)
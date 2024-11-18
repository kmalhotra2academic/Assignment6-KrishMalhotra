"""
Description: A class meant to manage Mortgage options.
Author: Krish Malhotra
Date: November 16, 2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixel_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """A class to represent a mortgage with specific properties and validations."""

    def __init__(self, loan_amount: float, string_rate_value: str, string_frequency_value: str, amortization: int):
        # Validate Loan Amount
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

        # Validate Rate
        try:
            self.__rate = MortgageRate[string_rate_value]
        except Exception:
            raise ValueError("Rate provided is invalid.")

        # Validate Frequency
        try:
            self.__frequency = PaymentFrequency[string_frequency_value]
        except Exception:
            raise ValueError("Frequency provided is invalid.")

        # Validate Amortization
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization

    # Accessor for Loan Amount
    @property
    def loan_amount(self):
        """Get the loan amount."""
        return self.__loan_amount

    # Mutator for Loan Amount
    @loan_amount.setter
    def loan_amount(self, value):
        """Set the loan amount after validation."""
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = value

    # Accessor for Rate
    @property
    def rate(self):
        """Get the mortgage rate."""
        return self.__rate

    # Mutator for Rate
    @rate.setter
    def rate(self, value):
        """Set the mortgage rate after validation."""
        try:
            self.__rate = MortgageRate[value]
        except Exception:
            raise ValueError("Rate provided is invalid.")

        # Accessor for Frequency
    @property
    def frequency(self):
        """Get the payment frequency."""
        return self.__frequency

    # Mutator for Frequency
    @frequency.setter
    def frequency(self, value):
        """Set the payment frequency after validation."""
        try:
            self.__frequency = PaymentFrequency[value]
        except Exception:
            raise ValueError("Frequency provided is invalid.")

        # Accessor for Amortization
    @property
    def amortization(self):
        """Get the amortization period."""
        return self.__amortization

    # Mutator for Amortization
    @amortization.setter
    def amortization(self, value):
        """Set the amortization period after validation."""
        if value not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = value

    def __init__(self, loan_amount: float, string_rate_value: str, string_frequency_value: str, amortization: int):
        # Initialization and validation logic (previously defined)
        pass  # Placeholder for the already implemented constructor

    # Accessor and mutator methods (already defined)

    def calculate_payment(self) -> float:
        """Calculate the mortgage payment amount."""
        # Convert annual rate to rate per period
        annual_rate = self.__rate.value
        rate_per_period = annual_rate / self.__frequency.value

        # Total number of payments
        total_payments = self.__frequency.value * self.__amortization

        # Calculate the mortgage payment using the formula
        payment = (self.__loan_amount * rate_per_period) / (1 - pow(1 + rate_per_period, -total_payments))
        return round(payment, 2)
    
    def test_calculate_payment_monthly(self):
        mortgage = Mortgage(682912.43, 'FIXED_1', 'MONTHLY', 10)
        payment = mortgage.calculate_payment()
        self.assertAlmostEqual(payment, 7578.30, places=2)

    def test_calculate_payment_biweekly(self):
        mortgage = Mortgage(500000, 'FIXED_5', 'BI_WEEKLY', 20)
        payment = mortgage.calculate_payment()
        self.assertAlmostEqual(payment, 1695.88, places=2)  # Adjust based on expected outcome

    def test_calculate_payment_weekly(self):
        mortgage = Mortgage(300000, 'VARIABLE_1', 'WEEKLY', 15)
        payment = mortgage.calculate_payment()
        self.assertAlmostEqual(payment, 508.67, places=2)  # Adjust based on expected outcome

    def __str__(self) -> str:
        """Return a formatted string representation of the mortgage object."""
        formatted_amount = f"${self.__loan_amount:,.2f}"
        formatted_rate = f"{self.__rate.value * 100:.2f}%"
        payment = self.calculate_payment()
        formatted_payment = f"${payment:,.2f}"
        frequency_display = self.__frequency.name.replace('_', ' ').title()

        return (f"Mortgage Amount: {formatted_amount}\n"
                f"Rate: {formatted_rate}\n"
                f"Amortization: {self.__amortization}\n"
                f"Frequency: {frequency_display} -- Calculated Payment: {formatted_payment}")
    
    def __repr__(self) -> str:
        """Return a developer-friendly string representation of the mortgage object."""
        return (f"Mortgage({self.__loan_amount}, {self.__rate.value}, "
                f"{self.__frequency.value}, {self.__amortization})")
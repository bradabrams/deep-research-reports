"""
GDP Validation Module (gdpval)

Provides utilities for validating and processing GDP (Gross Domestic Product) data.
Includes validation, conversion, and analysis functions.
"""


class GDPValidator:
    """Validates GDP data and values."""

    def __init__(self, currency="USD"):
        """
        Initialize the GDP validator.

        Args:
            currency (str): Currency code for GDP values (default: USD)
        """
        self.currency = currency
        self.min_gdp = 0
        self.max_gdp = float('inf')

    def validate_gdp_value(self, value):
        """
        Validate a GDP value.

        Args:
            value: The GDP value to validate

        Returns:
            bool: True if valid, False otherwise
        """
        if not isinstance(value, (int, float)):
            return False
        if value < self.min_gdp:
            return False
        if value > self.max_gdp:
            return False
        return True

    def validate_gdp_dict(self, data):
        """
        Validate a GDP data dictionary.

        Args:
            data (dict): Dictionary with 'country', 'value', and optionally 'year'

        Returns:
            bool: True if valid, False otherwise
        """
        if not isinstance(data, dict):
            return False
        if 'country' not in data or 'value' not in data:
            return False
        if not isinstance(data['country'], str) or not data['country'].strip():
            return False
        if not self.validate_gdp_value(data['value']):
            return False
        if 'year' in data:
            if not isinstance(data['year'], int) or data['year'] < 1900:
                return False
        return True

    def set_constraints(self, min_gdp=None, max_gdp=None):
        """
        Set constraints for valid GDP values.

        Args:
            min_gdp (float): Minimum valid GDP value
            max_gdp (float): Maximum valid GDP value
        """
        if min_gdp is not None:
            self.min_gdp = min_gdp
        if max_gdp is not None:
            self.max_gdp = max_gdp


class GDPConverter:
    """Convert GDP values between different units and scales."""

    @staticmethod
    def billions_to_trillions(value):
        """Convert GDP value from billions to trillions."""
        return value / 1000

    @staticmethod
    def trillions_to_billions(value):
        """Convert GDP value from trillions to billions."""
        return value * 1000

    @staticmethod
    def millions_to_billions(value):
        """Convert GDP value from millions to billions."""
        return value / 1000

    @staticmethod
    def billions_to_millions(value):
        """Convert GDP value from billions to millions."""
        return value * 1000


class GDPAnalyzer:
    """Analyze GDP data."""

    @staticmethod
    def calculate_average_gdp(gdp_list):
        """
        Calculate average GDP from a list of values.

        Args:
            gdp_list (list): List of GDP values

        Returns:
            float: Average GDP value
        """
        if not gdp_list:
            return 0
        return sum(gdp_list) / len(gdp_list)

    @staticmethod
    def calculate_total_gdp(gdp_list):
        """
        Calculate total GDP from a list of values.

        Args:
            gdp_list (list): List of GDP values

        Returns:
            float: Sum of all GDP values
        """
        return sum(gdp_list)

    @staticmethod
    def find_highest_gdp(gdp_list):
        """
        Find the highest GDP value in a list.

        Args:
            gdp_list (list): List of GDP values

        Returns:
            float: Highest GDP value
        """
        if not gdp_list:
            return None
        return max(gdp_list)

    @staticmethod
    def find_lowest_gdp(gdp_list):
        """
        Find the lowest GDP value in a list.

        Args:
            gdp_list (list): List of GDP values

        Returns:
            float: Lowest GDP value
        """
        if not gdp_list:
            return None
        return min(gdp_list)

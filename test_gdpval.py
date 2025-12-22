"""
Test suite for the GDP Validation Module (gdpval)

This test file provides comprehensive coverage for all gdpval classes and functions.
"""

import unittest
from gdpval import GDPValidator, GDPConverter, GDPAnalyzer


class TestGDPValidator(unittest.TestCase):
    """Test cases for the GDPValidator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.validator = GDPValidator()

    def test_validator_initialization(self):
        """Test GDPValidator initialization."""
        validator = GDPValidator("EUR")
        self.assertEqual(validator.currency, "EUR")
        self.assertEqual(validator.min_gdp, 0)

    def test_validate_gdp_value_valid_integer(self):
        """Test validation of valid integer GDP value."""
        self.assertTrue(self.validator.validate_gdp_value(1000))

    def test_validate_gdp_value_valid_float(self):
        """Test validation of valid float GDP value."""
        self.assertTrue(self.validator.validate_gdp_value(1500.5))

    def test_validate_gdp_value_zero(self):
        """Test validation of zero GDP value."""
        self.assertTrue(self.validator.validate_gdp_value(0))

    def test_validate_gdp_value_negative(self):
        """Test that negative GDP values are invalid."""
        self.assertFalse(self.validator.validate_gdp_value(-100))

    def test_validate_gdp_value_string(self):
        """Test that string values are invalid."""
        self.assertFalse(self.validator.validate_gdp_value("1000"))

    def test_validate_gdp_value_none(self):
        """Test that None is invalid."""
        self.assertFalse(self.validator.validate_gdp_value(None))

    def test_validate_gdp_value_with_constraints(self):
        """Test GDP value validation with constraints."""
        self.validator.set_constraints(min_gdp=1000, max_gdp=10000)
        self.assertFalse(self.validator.validate_gdp_value(500))
        self.assertTrue(self.validator.validate_gdp_value(5000))
        self.assertFalse(self.validator.validate_gdp_value(15000))

    def test_validate_gdp_dict_valid(self):
        """Test validation of valid GDP dictionary."""
        data = {'country': 'USA', 'value': 25000}
        self.assertTrue(self.validator.validate_gdp_dict(data))

    def test_validate_gdp_dict_with_year(self):
        """Test validation of GDP dictionary with year."""
        data = {'country': 'Germany', 'value': 5000, 'year': 2023}
        self.assertTrue(self.validator.validate_gdp_dict(data))

    def test_validate_gdp_dict_missing_country(self):
        """Test that missing country makes dictionary invalid."""
        data = {'value': 5000}
        self.assertFalse(self.validator.validate_gdp_dict(data))

    def test_validate_gdp_dict_missing_value(self):
        """Test that missing value makes dictionary invalid."""
        data = {'country': 'France'}
        self.assertFalse(self.validator.validate_gdp_dict(data))

    def test_validate_gdp_dict_empty_country(self):
        """Test that empty country string makes dictionary invalid."""
        data = {'country': '', 'value': 5000}
        self.assertFalse(self.validator.validate_gdp_dict(data))

    def test_validate_gdp_dict_invalid_year(self):
        """Test that invalid year makes dictionary invalid."""
        data = {'country': 'Japan', 'value': 4000, 'year': 1800}
        self.assertFalse(self.validator.validate_gdp_dict(data))

    def test_validate_gdp_dict_invalid_value(self):
        """Test that invalid value makes dictionary invalid."""
        data = {'country': 'UK', 'value': -1000}
        self.assertFalse(self.validator.validate_gdp_dict(data))

    def test_validate_gdp_dict_not_dict(self):
        """Test that non-dict input is invalid."""
        self.assertFalse(self.validator.validate_gdp_dict("not a dict"))

    def test_set_constraints(self):
        """Test setting GDP constraints."""
        self.validator.set_constraints(min_gdp=100, max_gdp=50000)
        self.assertEqual(self.validator.min_gdp, 100)
        self.assertEqual(self.validator.max_gdp, 50000)

    def test_set_constraints_partial(self):
        """Test setting partial constraints."""
        self.validator.set_constraints(min_gdp=500)
        self.assertEqual(self.validator.min_gdp, 500)
        self.assertEqual(self.validator.max_gdp, float('inf'))


class TestGDPConverter(unittest.TestCase):
    """Test cases for the GDPConverter class."""

    def test_billions_to_trillions(self):
        """Test conversion from billions to trillions."""
        result = GDPConverter.billions_to_trillions(1000)
        self.assertEqual(result, 1.0)

    def test_billions_to_trillions_decimal(self):
        """Test conversion from billions to trillions with decimal result."""
        result = GDPConverter.billions_to_trillions(500)
        self.assertEqual(result, 0.5)

    def test_trillions_to_billions(self):
        """Test conversion from trillions to billions."""
        result = GDPConverter.trillions_to_billions(1)
        self.assertEqual(result, 1000)

    def test_trillions_to_billions_decimal(self):
        """Test conversion from trillions to billions with decimal input."""
        result = GDPConverter.trillions_to_billions(2.5)
        self.assertEqual(result, 2500)

    def test_millions_to_billions(self):
        """Test conversion from millions to billions."""
        result = GDPConverter.millions_to_billions(1000)
        self.assertEqual(result, 1.0)

    def test_millions_to_billions_decimal(self):
        """Test conversion from millions to billions with decimal result."""
        result = GDPConverter.millions_to_billions(500)
        self.assertEqual(result, 0.5)

    def test_billions_to_millions(self):
        """Test conversion from billions to millions."""
        result = GDPConverter.billions_to_millions(1)
        self.assertEqual(result, 1000)

    def test_billions_to_millions_decimal(self):
        """Test conversion from billions to millions with decimal input."""
        result = GDPConverter.billions_to_millions(1.5)
        self.assertEqual(result, 1500)

    def test_conversion_roundtrip(self):
        """Test that conversions can be reversed."""
        original = 2000
        converted = GDPConverter.billions_to_trillions(original)
        back = GDPConverter.trillions_to_billions(converted)
        self.assertEqual(back, original)


class TestGDPAnalyzer(unittest.TestCase):
    """Test cases for the GDPAnalyzer class."""

    def test_calculate_average_gdp(self):
        """Test calculating average GDP."""
        gdp_list = [1000, 2000, 3000]
        result = GDPAnalyzer.calculate_average_gdp(gdp_list)
        self.assertEqual(result, 2000)

    def test_calculate_average_gdp_empty_list(self):
        """Test calculating average of empty list."""
        result = GDPAnalyzer.calculate_average_gdp([])
        self.assertEqual(result, 0)

    def test_calculate_average_gdp_single_value(self):
        """Test calculating average of single value."""
        result = GDPAnalyzer.calculate_average_gdp([5000])
        self.assertEqual(result, 5000)

    def test_calculate_average_gdp_decimal(self):
        """Test calculating average with decimal values."""
        gdp_list = [1000.5, 2000.5, 3000.5]
        result = GDPAnalyzer.calculate_average_gdp(gdp_list)
        self.assertAlmostEqual(result, 2000.5)

    def test_calculate_total_gdp(self):
        """Test calculating total GDP."""
        gdp_list = [1000, 2000, 3000]
        result = GDPAnalyzer.calculate_total_gdp(gdp_list)
        self.assertEqual(result, 6000)

    def test_calculate_total_gdp_empty_list(self):
        """Test calculating total of empty list."""
        result = GDPAnalyzer.calculate_total_gdp([])
        self.assertEqual(result, 0)

    def test_calculate_total_gdp_single_value(self):
        """Test calculating total of single value."""
        result = GDPAnalyzer.calculate_total_gdp([5000])
        self.assertEqual(result, 5000)

    def test_calculate_total_gdp_decimal(self):
        """Test calculating total with decimal values."""
        gdp_list = [1000.5, 2000.5, 3000.5]
        result = GDPAnalyzer.calculate_total_gdp(gdp_list)
        self.assertAlmostEqual(result, 6001.5)

    def test_find_highest_gdp(self):
        """Test finding highest GDP value."""
        gdp_list = [1000, 5000, 3000]
        result = GDPAnalyzer.find_highest_gdp(gdp_list)
        self.assertEqual(result, 5000)

    def test_find_highest_gdp_empty_list(self):
        """Test finding highest in empty list."""
        result = GDPAnalyzer.find_highest_gdp([])
        self.assertIsNone(result)

    def test_find_highest_gdp_single_value(self):
        """Test finding highest with single value."""
        result = GDPAnalyzer.find_highest_gdp([5000])
        self.assertEqual(result, 5000)

    def test_find_highest_gdp_negative_values(self):
        """Test finding highest with negative values."""
        gdp_list = [-1000, -500, -2000]
        result = GDPAnalyzer.find_highest_gdp(gdp_list)
        self.assertEqual(result, -500)

    def test_find_lowest_gdp(self):
        """Test finding lowest GDP value."""
        gdp_list = [1000, 5000, 3000]
        result = GDPAnalyzer.find_lowest_gdp(gdp_list)
        self.assertEqual(result, 1000)

    def test_find_lowest_gdp_empty_list(self):
        """Test finding lowest in empty list."""
        result = GDPAnalyzer.find_lowest_gdp([])
        self.assertIsNone(result)

    def test_find_lowest_gdp_single_value(self):
        """Test finding lowest with single value."""
        result = GDPAnalyzer.find_lowest_gdp([5000])
        self.assertEqual(result, 5000)

    def test_find_lowest_gdp_negative_values(self):
        """Test finding lowest with negative values."""
        gdp_list = [-1000, -500, -2000]
        result = GDPAnalyzer.find_lowest_gdp(gdp_list)
        self.assertEqual(result, -2000)


class TestGDPIntegration(unittest.TestCase):
    """Integration tests combining multiple components."""

    def test_validation_and_analysis_workflow(self):
        """Test a realistic workflow of validation and analysis."""
        validator = GDPValidator()
        gdp_data = [
            {'country': 'USA', 'value': 25000, 'year': 2023},
            {'country': 'China', 'value': 17000, 'year': 2023},
            {'country': 'Germany', 'value': 4000, 'year': 2023},
        ]

        # Validate all entries
        valid_gdp_values = []
        for entry in gdp_data:
            if validator.validate_gdp_dict(entry):
                valid_gdp_values.append(entry['value'])

        self.assertEqual(len(valid_gdp_values), 3)

        # Analyze the valid values
        average = GDPAnalyzer.calculate_average_gdp(valid_gdp_values)
        total = GDPAnalyzer.calculate_total_gdp(valid_gdp_values)
        highest = GDPAnalyzer.find_highest_gdp(valid_gdp_values)

        self.assertAlmostEqual(average, 15333.33, places=2)
        self.assertEqual(total, 46000)
        self.assertEqual(highest, 25000)

    def test_conversion_and_analysis(self):
        """Test converting units and analyzing results."""
        gdp_billions = [1000, 2000, 3000]
        gdp_trillions = [GDPConverter.billions_to_trillions(x) for x in gdp_billions]

        average_trillions = GDPAnalyzer.calculate_average_gdp(gdp_trillions)
        self.assertAlmostEqual(average_trillions, 2.0)

        # Convert back
        average_billions = GDPConverter.trillions_to_billions(average_trillions)
        self.assertAlmostEqual(average_billions, 2000)


if __name__ == '__main__':
    unittest.main()

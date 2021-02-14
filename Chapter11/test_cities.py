import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Class to test city_country fx"""
    def test__city_country(self):
        """method to test fx"""
        formatted_line = city_country("tokyo", "japan")
        self.assertEqual(formatted_line, "Tokyo, Japan")

    def test_city_country_population(self):
        """Test cases with population inclusion"""
        formatted_line = city_country("beijing", "china", "500")
        self.assertEqual(formatted_line, "Beijing, China - Population: 500")

if __name__ == "__main__":
    unittest.main()

import unittest
from weather_data import kelvin_to_celsius

class TestWeatherProcessing(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        self.assertEqual(round(kelvin_to_celsius(273.15), 2), 0.00)
        self.assertEqual(round(kelvin_to_celsius(300), 2), 26.85)
    
    def test_data_storage(self):
        # Implement tests for data storage
        pass

    def test_alerting(self):
        # Implement tests for alerting system
        pass

if __name__ == '__main__':
    unittest.main()

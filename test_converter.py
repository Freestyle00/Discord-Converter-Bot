"""
Prgram tests
"""
import unittest #I just cut my finger on the fucking keyboard like how on earth did i manaed that

from Converter import Converting
Converter = Converting()

class TestConverter(unittest.TestCase):
    """
    tests for the converter
    """
    def test_temperature(self):
        """
        tests for the temparature converter
        """
        self.assertEqual(Converter.TemperatureCtoF(50), 122)
        self.assertEqual(Converter.TemperatureCtoF(-50), -58)
        self.assertEqual(Converter.TemperatureFtoC(50), 10)
        self.assertAlmostEqual(Converter.TemperatureFtoC(-50), -45.55, places=0)
    def test_measurment(self):
        """
        tests for the measurment converter
        """
        self.assertEqual(Converter.MeasurmentWorldtoUS(10, "km"), 6.214)
        self.assertEqual(Converter.MeasurmentWorldtoUS(10, "m"), 10.936)
        self.assertEqual(Converter.MeasurmentWorldtoUS(10, "cm"), 0.328)
        self.assertEqual(Converter.MeasurmentWorldtoUS(10, "mm"), 0.394)
        self.assertEqual(Converter.MeasurmentUStoWorld(10, "mi"), 16.093)
        self.assertEqual(Converter.MeasurmentUStoWorld(10, "yd"), 9.144)
        self.assertEqual(Converter.MeasurmentUStoWorld(10, "ft"), 304.8)
        self.assertEqual(Converter.MeasurmentUStoWorld(10, "in"), 254)
    def test_speed(self):
        """
        test for the speed converter
        """
        self.assertEqual(Converter.SpeedKMHtoMPH(10), 6.2)
        self.assertEqual(Converter.SpeedMPHtoKMH(10), 16.1)

if __name__ == "__main__":
    unittest.main()

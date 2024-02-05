"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add(self):
        """Test adding numbers"""
        result = calc.add(2, 4)
        self.assertEqual(result, 6)

    def test_subtract(self):
        """Test subtracting numbers"""
        result = calc.subtract(10, 4)
        self.assertEqual(result, 6)
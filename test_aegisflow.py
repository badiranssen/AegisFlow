# test_aegisflow.py
"""
Tests for AegisFlow module.
"""

import unittest
from aegisflow import AegisFlow

class TestAegisFlow(unittest.TestCase):
    """Test cases for AegisFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AegisFlow()
        self.assertIsInstance(instance, AegisFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AegisFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

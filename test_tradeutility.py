# test_tradeutility.py
"""
Tests for TradeUtility module.
"""

import unittest
from tradeutility import TradeUtility

class TestTradeUtility(unittest.TestCase):
    """Test cases for TradeUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TradeUtility()
        self.assertIsInstance(instance, TradeUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TradeUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

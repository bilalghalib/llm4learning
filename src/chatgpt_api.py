# src/tests/test_chatgpt_api.py
import unittest
from chatgpt_api import fetch_artists  # Adjust import path as needed

class TestChatGPTAPI(unittest.TestCase):
    def test_fetch_artists(self):
        """Test that fetching artists returns a non-empty dictionary."""
        result = fetch_artists()
        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch

from summedia.text import Text


class TestText(unittest.TestCase):
    def setUp(self):
        self.text = Text(api_key="dummy_api_key")

    @patch("summedia.api.APIRequester.request_api")
    def test_summarize_text_normal(self, mock_request_api):
        # Mocking the response from request_api
        mock_request_api.return_value = "Mocked summarized text"

        # Test normal behavior
        result = self.text.summarize_text("Long text to be summarized", 150)
        self.assertEqual(result, "Mocked summarized text")

    @patch("summedia.api.APIRequester.request_api")
    def test_analyze_sentiment_normal(self, mock_request_api):
        # Mocking the response from request_api
        mock_request_api.return_value = "Mocked sentiment analysis"

        # Test normal behavior
        result = self.text.analyze_sentiment("Sample text for sentiment analysis")
        self.assertEqual(result, "Mocked sentiment analysis")

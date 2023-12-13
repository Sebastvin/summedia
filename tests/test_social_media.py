import unittest
from unittest.mock import patch

from summedia.social_media import SocialMedia


class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        self.social_media = SocialMedia(api_key="dummy_api_key")

    @patch("summedia.api.APIRequester.request_api")
    def test_condense_text_empty_input(self, mock_request_api):
        # Configure the mock to return a specific string
        mock_request_api.return_value = "Mocked response"

        # Test with empty string
        result = self.social_media.condense_text_to_tweet("")
        self.assertEqual(result, "Mocked response")

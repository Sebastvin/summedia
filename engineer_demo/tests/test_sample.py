import pytest
from unittest.mock import patch, Mock
from engineer_demo.twitter import condense_text_to_tweet


def test_condense_text_to_tweet():
    # Mocked response from OpenAI
    mock_response = {
        'choices': [
            {
                'message': {
                    'content': 'Mocked tweet text'
                }
            }
        ]
    }

    # Using the patch function to mock openai.ChatCompletion.create method
    with patch('engineer_demo.twitter.openai.ChatCompletion.create', return_value=mock_response) as mock_method:
        result = condense_text_to_tweet("This is a long text that should be condensed", "gpt-4.0-turbo")
        assert result == 'Mocked tweet text'
        mock_method.assert_called_once_with(
            model="gpt-4.0-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that condenses long texts into tweets."},
                {"role": "user",
                 "content": "Condense the following text into a tweet: This is a long text that should be condensed"}
            ]
        )

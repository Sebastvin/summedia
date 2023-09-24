from unittest.mock import patch
from engineer_demo.text import summarize_text


def test_summarize_text():
    # Mocked response from OpenAI
    mock_response = {"choices": [{"message": {"content": "Mocked summarize text"}}]}

    # Using the patch function to mock openai.ChatCompletion.create method
    with patch(
        "engineer_demo.text.openai.ChatCompletion.create", return_value=mock_response
    ) as mock_method:
        result = summarize_text(
            "This is a long text that should be summarize into a smaller piece",
            "gpt-4.0-turbo",
            3,
        )
        assert result == "Mocked summarize text"
        mock_method.assert_called_once_with(
            model="gpt-4.0-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarize long texts into"
                    " text with maximum 3 words.",
                },
                {
                    "role": "user",
                    "content": "Summarize the following text into a text "
                    "with maximum 3 words, the text is This is a long text that should be"
                    " summarize into a smaller piece",
                },
            ],
        )


# Mock data
SAMPLE_ARTICLE_URL = "https://example.com/sample-article"
SAMPLE_ARTICLE_TEXT = (
    "This is a sample article text. It's meant to represent the content of an article."
)
SAMPLE_SUMMARY = "Sample article summary."

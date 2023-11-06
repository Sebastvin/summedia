import pytest
from engineer_demo.fetching_data import get_text_from_article, article_time_read
from unittest.mock import patch


# Test cases for the 'get_text_from_article' function.
@pytest.mark.parametrize(
    "article_url, expected_text",
    [
        ("https://example.com/article1", "This is the text of article 1."),
        ("https://example.com/article2", "This is the text of article 2."),
    ],
)
@patch("engineer_demo.fetching_data.Article")
def test_get_text_from_article(mock_article, article_url, expected_text):
    # Mock the behavior of the Article class.
    mock_instance = mock_article.return_value
    mock_instance.download.return_value = None
    mock_instance.parse.return_value = None
    mock_instance.text = expected_text

    # Call the function and compare the result to the expected text.
    actual_text = get_text_from_article(article_url)
    assert actual_text == expected_text


def test_article_time_read_empty_text():
    """Test for an empty text."""
    assert article_time_read("") == 0


def test_article_time_read_short_text():
    """Test for a very short text."""
    assert article_time_read("123") == 0


def test_article_time_read_long_text():
    """Test for a long text."""
    text = "word " * 500
    assert article_time_read(text) == 2

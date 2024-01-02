from unittest.mock import patch

import pytest
import responses

from summedia.fetching_data import (
    article_time_read,
    get_images_from_html,
    get_text_from_article,
)


@pytest.mark.parametrize(
    "article_url, expected_text",
    [
        ("https://example.com/article1", "This is the text of article 1."),
        ("https://example.com/article2", "This is the text of article 2."),
    ],
)
@patch("summedia.fetching_data.Article")
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


@responses.activate
def test_get_images_from_html():
    # Mock the HTML response
    mock_url = "https://example.com/article"
    mock_html_content = """
    <html>
        <body>
            <img src="https://example.com/image1.jpg" alt="Image 1">
            <img src="https://example.com/image1.jpg" alt="Duplicated image">
            <img src="/image2.jpg" alt="Image 2">
            <img src="image3.jpg" alt="Image 3">
        </body>
    </html>
    """
    responses.add(responses.GET, mock_url, body=mock_html_content, status=200)

    # Call the function
    img_urls = get_images_from_html(mock_url)
    print(set(img_urls))

    # Assertions
    assert len(img_urls) == 1
    assert "https://example.com/image1.jpg" in img_urls


def test_get_images_from_html_error():
    mock_url = "https://error.com/article"
    responses.add(responses.GET, mock_url, status=404)

    # Call the function for a non-existent page
    img_urls = get_images_from_html(mock_url)

    # Assertions
    assert img_urls == []

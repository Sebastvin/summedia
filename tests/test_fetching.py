from unittest.mock import patch

import pytest
import responses

from summedia.fetching_data import get_images, get_text, get_time_read

ARTICLE_BODY = (
    "Lorem Ipsum is simply dummy text of the printing and"
    " typesetting industry. Lorem Ipsum has been the industry's "
    "standard dummy text ever since the 1500s, when an unknown "
    "printer took a galley of type and scrambled it to make a"
    " type specimen book. "
)


@pytest.mark.parametrize(
    "article_url, expected_text",
    [
        ("https://example.com/article1", "This is the text of article 1."),
        ("https://example.com/article2", "This is the text of article 2."),
    ],
)
@patch("summedia.fetching_data.Article")
def test_get_text(mock_article, article_url, expected_text):
    # Mock the behavior of the Article class.
    mock_instance = mock_article.return_value
    mock_instance.download.return_value = None
    mock_instance.parse.return_value = None
    mock_instance.text = expected_text

    # Call the function and compare the result to the expected text.
    actual_text = get_text(article_url)
    assert actual_text == expected_text


@responses.activate
def test_article_time_read_empty_text():
    """Test for an empty text."""
    mock_url = "https://example.com/article"

    mock_html_content = """
        <html>
            <body>
                <article>
                    <div>
                        <p>
                        </p>
                    </div>
                </article>
            </body>
        </html"""
    responses.add(responses.GET, mock_url, body=mock_html_content, status=200)

    assert get_time_read(mock_url) == 0


@responses.activate
def test_time_read_short_text():
    """Test for a very short text."""

    mock_url = "https://example.com/article"
    mock_html_content = (
        """
        <html>
            <body>
                <article>
                    <div>
                        <p>
                    """
        + ARTICLE_BODY * 12
        + """
                         </p>
                    </div>
                </article>
            </body>
        </html"""
    )

    responses.add(responses.GET, mock_url, body=mock_html_content, status=200)

    assert get_time_read(mock_url) == 2


@responses.activate
def test_article_time_read_long_text():
    """Test for a long text."""
    mock_url = "https://example.com/article"

    mock_html_content = (
        """
        <html>
            <body>
                <article>
                    <div>
                        <p>
                    """
        + ARTICLE_BODY * 60
        + """
                         </p>
                    </div>
                </article>
            </body>
        </html"""
    )
    responses.add(responses.GET, mock_url, body=mock_html_content, status=200)

    assert get_time_read(mock_url) == 11


@responses.activate
def test_get_images():
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
    img_urls = get_images(mock_url)
    print(set(img_urls))

    # Assertions
    assert len(img_urls) == 1
    assert "https://example.com/image1.jpg" in img_urls


def test_get_images_error():
    mock_url = "https://error.com/article"
    responses.add(responses.GET, mock_url, status=404)

    # Call the function for a non-existent page
    img_urls = get_images(mock_url)

    # Assertions
    assert img_urls == []

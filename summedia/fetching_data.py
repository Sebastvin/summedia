from typing import List

import requests
from bs4 import BeautifulSoup
from newspaper import Article


def get_article(article_url: str) -> Article:
    """
    Retrieves the text content of a web article from the specified URL.

    This function uses the Newspaper3k library to download and extract the main
    body text of a news article or similar web page.

    Parameters:
    - article_url (str): The URL of the web article to be retrieved.

    Returns:
    - Article: The main content of the web article.
    """
    article = Article(article_url)
    article.download()
    return article


def get_text_from_article(article_url: str) -> str:
    """
    Extracts the main text content from an article given its URL.

    Args:
    - article_url (str): The URL of the article from which the text content is to be extracted.

    Returns:
    - str: The main text content of the article.

    Note:
    This function uses the 'newspaper3k' library to download and parse the article.
    """
    article = get_article(article_url)
    article.parse()
    return article.text


def article_time_read(article_text: str, words_per_minute: int = 238) -> int:
    """
    Source: https://scholarwithin.com/average-reading-speed

    Args:
    - article_text(str): Text from which we count reading time
    - words_per_minute(int): Number of words read per minute

    Returns:
    - int: Reading time returned in minutes
    """

    num_chars = len(article_text.split())
    estimated_minutes = num_chars / words_per_minute

    return round(estimated_minutes)


def get_images_from_html(article_url: str) -> List[str]:
    """
    Extracts all unique img tags from an HTML article while preserving their order.

    Parameters:
    - article_url (str): The URL of the HTML article.

    Returns:
    - List[str]: A list of unique img tags, in the order they appear in the HTML.
    """
    try:
        html_code = get_article(article_url).html
        soup = BeautifulSoup(html_code, "html.parser")

        full_img_urls = []
        for img in soup.find_all("img"):
            if (
                img.has_attr("src")
                and img["src"].startswith("http")
                and img["src"] not in full_img_urls
            ):
                full_img_urls.append(img["src"])
        return full_img_urls

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

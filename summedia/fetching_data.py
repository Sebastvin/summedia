from typing import List, Union

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


def get_text(article_url: str) -> str:
    """
    Extracts the main text content from an article given its URL.

    Parameters:
    - article_url (str): The URL of the article from which the text content is to be extracted.

    Returns:
    - str: The main text content of the article.

    Note:
    - This function uses the 'newspaper3k' library to download and parse the article.
    """
    article = get_article(article_url)
    article.parse()
    return article.text


def get_time_read(article_url: str, words_per_minute: int = 238) -> int:
    """
    Source: https://scholarwithin.com/average-reading-speed

    Parameters:
    - article_text(str): Text from which we count reading time
    - words_per_minute(int): Number of words read per minute

    Returns:
    - int: Reading time returned in minutes
    """

    article_text = get_text(article_url)
    num_chars = len(article_text.split())
    estimated_minutes = num_chars / words_per_minute

    return round(estimated_minutes)


def get_images(article_url: str) -> List[str]:
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


def get_publishing_date(article_url: str):
    """
    Retrieves the publishing date of an article from the given URL.

    This function fetches an article using the specified URL, parses it,
    and extracts the publishing date of the article.

    Parameters:
    - article_url (str): The URL of the article from which to extract the publishing date.

    Returns:
    - The publishing date of the article. The return type depends on how the publish_date
      is structured in the article object. It could be a string, a datetime object, etc.
    """
    article = get_article(article_url)
    article.parse()
    return article.publish_date


def get_authors(article_url: str):
    """
    Retrieves the list of authors of an article from the given URL.

    This function fetches an article using the specified URL, parses it,
    and extracts the list of authors associated with the article.

    Args:
    - article_url (str): The URL of the article from which to extract the authors.

    Returns:
    - A list of authors of the article. If no authors are found, the function
      may return an empty list, depending on the implementation of the article object.
    """
    article = get_article(article_url)
    article.parse()
    return article.authors


def get_title(article_url: str) -> str:
    """
    Retrieves the title of an article from the given URL.

    This function fetches an article using the specified URL, parses it,
    and extracts the title of the article.

    Parameters:
    - article_url (str): The URL of the article from which to extract the title.

    Returns:
    - The title of the article as a string.
    """
    article = get_article(article_url)
    article.parse()
    return article.title


def get_movies(article_url: str) -> str:
    """
    Extracts and returns the title of a movie from a given article URL.

    This function fetches an article from the specified URL, parses it,
    and returns the title of the movie mentioned in the article.

    Parameters:
    - article_url (str): The URL of the article to extract the movie title from.

    Returns:
    - str: The title of the movie extracted from the article.

    Note:
    - This function assumes that the article contains a movie title and
     that the 'get_article' function is capable of fetching and parsing
     the article correctly.
    """

    article = get_article(article_url)
    article.parse()
    return article.movies


def get_meta_description(article_url: str) -> Union[str, None, list]:
    """
    Extracts the meta description from a given article URL.

    Parameters:
    - article_url (str): The URL of the article from which to extract the meta description.

    Returns:
    - Union[str, None, list]: A string containing the content of the 'meta description' tag,
      None if the tag is not found, or an empty list in case of a request exception.

    Raises:
    - requests.RequestException: If there is an error fetching the article URL.
    """
    try:
        html_code = get_article(article_url).html
        soup = BeautifulSoup(html_code, "html.parser")

        meta_description = soup.find("meta", attrs={"name": "description"})

        if meta_description:
            return meta_description.get("content", None)

        return None
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []


def get_meta_keywords(article_url: str) -> Union[str, None, list]:
    """
    Extracts the meta keywords from a given article URL.

    Parameters:
    - article_url (str): The URL of the article from which to extract the meta keywords.

    Returns:
    - Union[str, None, list]: A string containing the content of the 'meta keywords' tag,
     None if the tag is not found, or an empty list in case of a request exception.

    Raises:
    - requests.RequestException: If there is an error fetching the article URL.
    """

    try:
        html_code = get_article(article_url).html
        soup = BeautifulSoup(html_code, "html.parser")

        meta_keywords = soup.find("meta", attrs={"name": "keywords"})

        if meta_keywords:
            return meta_keywords.get("content", None)

        return None
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

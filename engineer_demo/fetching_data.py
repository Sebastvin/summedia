from newspaper import Article


def get_article(article_url: str) -> str:
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

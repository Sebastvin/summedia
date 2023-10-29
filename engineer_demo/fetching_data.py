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


print(
    get_text_from_article(
        "https://boringcashcow.com/post/business-ideas-for-software-developers-in-2023"
    )
)

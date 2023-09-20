from newspaper import Article


def get_text_from_article(article_url: str) -> str:
    article = Article(article_url)
    article.download()
    article.parse()
    return article.text

from summedia.fetching_data import get_text_from_article
from newspaper.article import ArticleException
from summedia.api import APIRequester


class Text(APIRequester):
    def summarize_text(
        self, text: str, max_number_words: int, model_type: str = None
    ) -> str:
        """
        Summarize a longer text into a shorter
        message using OpenAI's chat model.

        Parameters:
        - text (str): The input text that is to be summarized.
        - model_type (str):  The type model what you want to use
        - max_number_words (int): The max number words of summarized text

        Returns:
        - str: The summarized text suitable for a max_number_words.
        """

        content_system = (
            f"You are a helpful assistant that summarize "
            f"long texts into text with maximum {max_number_words} words."
        )

        content_user = (
            f"Summarize the following text into a text with"
            f" maximum {max_number_words} words, the text is {text}"
        )

        if model_type:
            return super().request_api(content_system, content_user, model_type)
        else:
            return super().request_api(content_system, content_user)

    def summary_article(
        self, article_url: str, article_text: str = None, max_number_words: int = 150
    ) -> str:
        """
        Summarizes the content of an article provided either through a URL or as a text string.

        This function attempts to fetch and summarize the article content from the given URL.
        If the URL is not provided or inaccessible, it falls back to summarizing the article content
        passed as a text string.

        Args:
            article_url (str): The URL of the article to be summarized.
                               If provided, the function fetches
                               the article text from this URL.
            article_text (str, optional): Direct text input of the article.
                                          This is used if `article_url`
                                          is not provided or the content could not be
                                          fetched from the URL.
            max_number_words (int, optional): The maximum number of words for the summary.
                                            Defaults to 150.

        Returns:
            str: The summarized version of the article content.
                If an error occurs during the process, an error message is returned instead.

        Raises:
            ArticleException: If there's an issue with fetching or
                            processing the article from the URL.

        Note:
            The function prioritizes `article_url` over `article_text`.
            If both are provided, it attempts to use `article_url` first.
        """

        try:
            if article_url:
                text = get_text_from_article(article_url)
                summarized_text = self.summarize_text(text, max_number_words)
                return summarized_text
            elif article_text:
                summarized_text = self.summarize_text(article_text, max_number_words)
                return summarized_text

        except ArticleException as e:
            return f"Error summarizing the article: {str(e)}"

    def analyze_sentiment(self, text: str, model_type: str = None) -> str:
        """
        Analyze the sentiment of a given text using the OpenAI API.

        Args:
        - text (str): The text to be analyzed.
        - model_type (str): The model to use for the analysis.

        Returns:
        - str: The full response from the model.
        """
        try:
            # Return the full response from the model

            content_system = (
                "You are a helpful assistant that analyzes"
                " sentiment in the given text."
            )

            content_user = f"Analyze the sentiment of this text: {text}"

            if model_type:
                return super().request_api(content_system, content_user, model_type)
            else:
                return super().request_api(content_system, content_user)

        except Exception as e:
            print(f"Error: {e}")
            return "Error in processing the request."

    def to_bullet_list(self, text: str, model_type: str = None) -> str:
        try:
            content_system = (
                "You are a helpful assistant that analyzes" " the given text."
            )

            content_user = (
                f"Give bullet a list of the most important"
                f" information from a given text, the text is: {text}"
            )

            if model_type:
                return super().request_api(content_system, content_user, model_type)
            else:
                return super().request_api(content_system, content_user)

        except Exception as e:
            print(e)
            return "Error in processing the request."

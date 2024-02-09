from newspaper.article import ArticleException

from summedia.api import APIRequester
from summedia.fetching_data import get_text
from summedia.level import SimplificationLevel
from summedia.translator import Language


class Text(APIRequester):
    """
    A subclass of APIRequester specialized in text analysis and manipulation tasks.

    The Text class extends the functionality of the APIRequester to provide
    specific methods for handling various text-based operations. These operations
    include text summarization, translation, sentiment analysis, text simplification,
    and categorization. It utilizes an external AI model (accessible through the
    APIRequesters request_api method) to perform these tasks.

    Methods:
    - summarize_text: Summarizes a given text.
    - summary_article: Summarizes the content of an article from a URL or text.
    - analyze_sentiment: Analyzes the sentiment of a given text.
    - to_bullet_list: Converts text into a bullet-point summary.
    - translate_text: Translates text to a specified language.
    - adjust_text_complexity: Simplifies text to a specified complexity level.
    - tag_and_categorize_text: Analyzes text for key themes and categories.

    The class is designed to be used where text analysis and manipulation
    functionalities are required, leveraging the capabilities of an AI model.
    """

    def summarize_text(self, text: str, max_number_words: int = 150, model_type: str = None) -> str:
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
            f"You are a helpful assistant that summarizes "
            f"long texts into a text with a maximum of {max_number_words} words. "
            f"All summaries must be in English."
        )

        content_user = (
            f"Summarize the following text into a concise version, "
            f"using a maximum of {max_number_words} words. "
            f"Ensure the summary is in English. The text to summarize is: {text}"
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
                text = get_text(article_url)
                summarized_text = self.summarize_text(text, max_number_words)
                return summarized_text
            elif article_text:
                summarized_text = self.summarize_text(article_text, max_number_words)
                return summarized_text

        except ArticleException as e:
            return f"Error summarizing the article: {str(e)}"

    def analyze_sentiment(
        self, text: str, max_number_words: int = 150, model_type: str = None
    ) -> str:
        """
        Analyze the sentiment of a given text using the OpenAI API.

        Args:
        - text (str): The text to be analyzed.
        - model_type (str): The model to use for the analysis.

        Returns:
        - str: The full response from the model.
        """

        try:
            content_system = (
                f"You are a helpful assistant that analyzes sentiment in given texts. "
                f"All analyses must be provided in English, and you can analyze"
                f" text with up to {max_number_words} words."
            )

            content_user = (
                f"Analyze the sentiment of the following text, "
                f"ensuring your analysis is in English. "
                f"The analysis should not exceed {max_number_words} words. "
                f"The text for sentiment analysis is: {text}"
            )

            if model_type:
                return super().request_api(content_system, content_user, model_type)
            else:
                return super().request_api(content_system, content_user)

        except Exception as e:
            print(f"Error: {e}")
            return "Error in processing the request."

    def to_bullet_list(self, text: str, model_type: str = None) -> str:
        """
        Converts the provided text into a bullet-point summary using an AI model.

        This method sends a request to an AI model to analyze the given text and
        summarize it into a list of bullet points, highlighting the most important
        information.

        Parameters:
        - text (str): The text to be converted into bullet points.
        - model_type (str, optional): The model type to use for the summary
                                        generation. If not provided, a default model
                                        is used.

        Returns:
        - str: A bullet-point summary of the provided text.

        Exceptions:
        - Catches and prints any exceptions that occur during processing, returning
        a generic error message.
        """
        try:
            content_system = (
                "You are a helpful assistant that analyzes"
                " the given text and provides responses in English."
            )

            content_user = (
                f"Provide a bullet-point list summarizing the most important"
                f" information from the given text, ensuring the summary"
                f" is in English. The text to be summarized is: {text}"
            )

            if model_type:
                return super().request_api(content_system, content_user, model_type)
            else:
                return super().request_api(content_system, content_user)

        except Exception as e:
            print(e)
            return "Error in processing the request."

    def translate_text(
        self,
        text: str,
        model_type: str = None,
        language_to_translate: str = "en",
    ) -> str:
        """
        Translates the provided text to a specified language using an AI model.

        This method first validates and retrieves the full name of the target language
        using the `Language` class. It then sends a request to an AI model to translate
        the text into the desired language.

        Parameters:
        - text (str): The text to be translated.
        - model_type (str, optional): The model type to use for the translation.
                                      If not provided, a default model is used.
        - language_to_translate (str, optional): The language code (e.g., 'en' for
                                                 English) to which the text should
                                                 be translated. Defaults to English.

        Returns:
        - str: The translated text in the target language.

        Exceptions:
        - Catches and prints any exceptions that occur during processing, returning
          a generic error message.
        """

        try:
            Language.validate_language(language_to_translate)

            lang = Language.get_language_name(language_to_translate)

            content_system = (
                "You are a helpful assistant that translate given" " text to other language."
            )

            content_user = f"Translate given text {text} to {lang} language"

            if model_type:
                return super().request_api(content_system, content_user, model_type)
            else:
                return super().request_api(content_system, content_user)

        except Exception as e:
            print(e)
            return "Error in processing the request."

    def adjust_text_complexity(
        self,
        text: str,
        level: SimplificationLevel = SimplificationLevel.STUDENT,
        model_type: str = None,
    ):
        """
        Simplifies the provided text to a specified complexity level using an AI model.

        This method sends a request to an AI model to simplify the given text. The
        level of simplification is determined by the 'level' parameter, which can be
        'child', 'teen', 'student', or 'expert', each representing a different degree
        of complexity.

        Parameters:
        - text (str): The text to be simplified.
        - level (SimplificationLevel): The complexity level to which the text should
                                       be simplified. Defaults to STUDENT level.
        - model_type (str, optional): The model type to use for the simplification.
                                      If not provided, a default model is used.

        Returns:
        - str: The simplified text suitable for the specified complexity level.

        Exceptions:
        - Catches and prints any exceptions that occur during processing, returning
          a generic error message.
        """

        try:
            content_system = (
                "You are an AI trained to simplify text to different levels of complexity,"
                " providing responses in English. "
                "Based on the specified level, simplify the text while preserving "
                "its main meaning. "
                "The levels are: 'child', 'teen', 'student', 'expert'. Each level represents "
                "a higher degree of complexity and vocabulary."
            )

            content_user = (
                f"Simplify the following text to the '{level.value}' level, "
                f"ensuring the simplified text is in English. "
                f"The text should be suitable for the understanding level of a '{level.value}', "
                f"using appropriate vocabulary and sentence structure for that level: {text}."
            )

            if model_type:
                response = super().request_api(content_system, content_user, model_type)
            else:
                response = super().request_api(content_system, content_user)

            return response

        except Exception as e:
            print(e)
            return "Error in processing the request."

    def tag_and_categorize_text(self, text: str, model_type: str = None):
        """
        Analyzes a given text to identify key themes, concepts, and categories,
        and suggests relevant tags and categories.

        This method sends a request to an AI model to analyze the provided text.
        It constructs a specific prompt for the AI to categorize the text into tags
        and categories, then parses the AI's response.

        Parameters:
        - text (str): The text to be analyzed.
        - model_type (str, optional): The model type to use for the analysis. If not
                                      provided, a default model is used.

        Returns:
        - str: The AI's response containing two lists - one for tags and another for
               categories of the provided text.

        Exceptions:
        - Catches and prints any exceptions that occur during processing, returning
          a generic error message.
        """

        try:
            content_system = (
                "You are an intelligent assistant trained to analyze text and "
                "identify key themes, concepts, and categories. "
                "Your task is to categorize the text and suggest relevant tags based"
                " on its content."
            )

            content_user = (
                f"Analyze the following text and categorize it into two lists: {text}. "
                f"List one should contain relevant tags representing the main themes "
                f"and subjects of the text. "
                f"List two should contain categories that the text belongs to. "
                f"Return the results as two separate lists: tags and categories."
            )

            if model_type:
                response = super().request_api(content_system, content_user, model_type)
            else:
                response = super().request_api(content_system, content_user)

            return response

        except Exception as e:
            print(e)
            return "Error in processing the request."

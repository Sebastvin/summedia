from summedia.api import APIRequester


class SocialMedia(APIRequester):
    """
    A subclass of APIRequester specialized in processing and optimizing
    text for social media platforms.

    The SocialMedia class extends the functionalities of APIRequester to provide methods
    specifically tailored for social media content creation and manipulation. It enables
    text condensation for tweets, formatting and optimization for Facebook posts, and
    potentially other social media-related functionalities. The class leverages an external
    AI model to perform these tasks, accessible through the inherited request_api method.

    Methods:
    - condense_text_to_tweet: Condenses text to fit within the character limit of a tweet.
    - post_to_facebook: Formats and optimizes text for posting on Facebook.

    This class is designed for applications where social media content creation and
    optimization are required, utilizing the capabilities of an AI model for effective
    communication in social media contexts.
    """

    def condense_text_to_tweet(self, text: str, model_type: str = None) -> str:
        """
        Condenses a longer text into a tweet-sized message.

        Parameters:
        - text (str): The input text that is to be condensed.

        Returns:
        - str: The condensed text suitable for a tweet.
        """

        content_system = (
            "You are a helpful assistant that condenses long texts into tweets."
        )
        content_user = f"Condense the following text into a tweet: {text}"

        if model_type:
            return super().request_api(content_system, content_user, model_type)
        else:
            return super().request_api(content_system, content_user)

    def post_to_facebook(
        self, text: str, model_type: str = None, word_length: int = 50
    ):
        """
        Posts the given text to Facebook after optimizing it for the platform.

        This method takes a text input and formats it to be suitable for a Facebook post.
        It utilizes an expert assistant model to optimize the text, ensuring it is engaging
        and appropriate for Facebook's audience and format. The content is tailored to fit
        within a specified word length, focusing on key messages and readability.
        The method can optionally use a specified model type for this optimization process.

        Parameters:
        - text (str): The text to be posted on Facebook.
        - model_type (str, optional): The type of model to be used for text optimization.
          If not provided, a default model is used.
        - word_length (int, optional): The target word count for the optimized text.
          Defaults to 50 words.

        Returns:
        - The response from the API call to post the text to Facebook.
        """

        content_system = (
            "You are an expert assistant skilled in preparing and"
            " optimizing texts for Facebook posts."
        )
        content_user = (
            f"Please format and optimize the following text for a Facebook post, ensuring "
            f"it is engaging and concise. "
            f"Tailor the content to fit within {word_length} words, focusing on retaining "
            f"key messages and readability: {text}"
        )

        if model_type:
            return super().request_api(content_system, content_user, model_type)
        else:
            return super().request_api(content_system, content_user)

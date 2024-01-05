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

    def condense_text_to_tweet(
        self, text: str, model_type: str = None, word_length: int = 50
    ) -> str:
        """
        Condenses a longer text into a tweet-sized message, considering a target word length.

        Parameters:
        - text (str): The input text that is to be condensed.
        - model_type (str, optional): Type of model to use for condensing. Defaults to None.
        - word_length (int, optional): The target word count for the optimized text. Defaults to 50.

        Returns:
        - str: The condensed text suitable for a tweet.
        """

        content_system = (
            "You are a helpful assistant that condenses long texts into tweets."
            " All responses must be in English."
        )

        content_user = (
            f"Condense the following text into a tweet, ensuring the output is in English. "
            f"Tailor the content to fit within {word_length} words, while "
            f"focusing on retaining key messages and readability: {text}"
        )

        # Retrieve the condensed text from the API
        condensed_text = (
            super().request_api(content_system, content_user, model_type)
            if model_type
            else super().request_api(content_system, content_user)
        )

        return condensed_text

    def post_to_facebook(
        self,
        text: str,
        model_type: str = None,
        word_length: int = 50,
    ):
        """
        Posts the given text to Facebook after optimizing it for the
         platform with optional emoji inclusion.

        This method formats and optimizes text for a Facebook post, ensuring it is engaging
        and appropriate for Facebook's audience. It focuses on key messages and readability
        within a specified word length and can optionally include emojis in the post.

        Parameters:
        - text (str): The text to be posted on Facebook.
        - model_type (str, optional): The type of model used for text optimization.
        - word_length (int, optional): The target word count for the optimized text. Defaults to 50.

        Returns:
        - The response from the API call to post the text to Facebook.
        """

        content_system = (
            "You are an expert assistant skilled in preparing and "
            "optimizing texts for Facebook posts. All responses must be in English."
        )

        content_user = (
            f"Please format and optimize the following text for a "
            f"Facebook post, ensuring it is engaging, concise, and in English. "
            f"Tailor the content to fit within {word_length} words, "
            f"focusing on retaining key messages and readability: {text}"
        )

        if model_type:
            return super().request_api(content_system, content_user, model_type)
        else:
            return super().request_api(content_system, content_user)

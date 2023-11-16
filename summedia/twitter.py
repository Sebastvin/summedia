from summedia.api import APIRequester


class Twitter(APIRequester):
    """Concrete class inheriting from APIRequester to handle text condensation via OpenAI."""

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

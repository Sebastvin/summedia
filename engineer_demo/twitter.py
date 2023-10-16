from engineer_demo.api import APIRequester


class Twitter(APIRequester):
    """Concrete class inheriting from APIRequester to handle text condensation via OpenAI."""

    def __init__(self, model_type: str):
        self.model_type = model_type

    def condense_text_to_tweet(self, text: str) -> str:
        """
        Condenses a longer text into a tweet-sized message.

        Parameters:
        - text (str): The input text that is to be condensed.

        Returns:
        - str: The condensed text suitable for a tweet.
        """
        # return self.request_api(text)
        content_system = (
            "You are a helpful assistant that condenses long texts into tweets."
        )
        content_user = "Condense the following text into a tweet"
        return super().request_api(content_system, content_user, text)

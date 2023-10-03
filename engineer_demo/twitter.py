import openai
from engineer_demo.api import APIRequester


class Twitter(APIRequester):
    """Concrete class inheriting from APIRequester to handle text condensation via OpenAI."""

    def __init__(self, model_type: str):
        self.model_type = model_type

    def request_api(self, text: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model_type,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that condenses long texts into tweets.",
                },
                {
                    "role": "user",
                    "content": f"Condense the following text into a tweet: {text}",
                },
            ],
        )
        return response["choices"][0]["message"]["content"].strip()

    def condense_text_to_tweet(self, text: str) -> str:
        """
        Condenses a longer text into a tweet-sized message.

        Parameters:
        - text (str): The input text that is to be condensed.

        Returns:
        - str: The condensed text suitable for a tweet.
        """
        return self.request_api(text)

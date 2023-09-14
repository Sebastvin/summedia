import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



def condense_text_to_tweet(text: str, model_type: str) -> str:
    """
    Condenses a longer text into a tweet-sized message using OpenAI's chat model.

    Parameters:
    - text (str): The input text that is to be condensed.
    - model_type (str):  The type model what you want to use

    Returns:
    - str: The condensed text suitable for a tweet.
    """

    # Using the chat model for condensing the text
    response = openai.ChatCompletion.create(
        model=model_type,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that condenses long texts into tweets."},
            {"role": "user", "content": f"Condense the following text into a tweet: {text}"}
        ]
    )
    tweet_text = response['choices'][0]['message']['content'].strip()

    return tweet_text

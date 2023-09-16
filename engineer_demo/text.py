import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def summarize_text(text: str, model_type: str, max_number_words: int) -> str:
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

    # Using the chat model for condensing the text
    response = openai.ChatCompletion.create(
        model=model_type,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarize"
                f" long texts into text with maximum {max_number_words} words.",
            },
            {
                "role": "user",
                "content": f"Summarize the following text into a text "
                           f"with maximum {max_number_words} words, the text is {text}",
            },
        ],
    )
    summarized_text = response["choices"][0]["message"]["content"].strip()

    return summarized_text

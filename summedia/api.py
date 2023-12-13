from openai import OpenAI


class APIRequester:
    """
    A class for handling requests to an API using a provided API key.

    This class encapsulates the functionality needed to interact with an external
    API, specifically designed to send requests and handle responses. It stores an
    API key for authentication purposes and provides methods for different types
    of API requests.

    Attributes:
    - api_key (str): The API key used for authenticating requests to the openai API.

    Usage:
    To use this class, instantiate it with a valid API key and then call its methods
    to interact with the API.
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def request_api(
        self,
        content_system: str,
        content_user: str,
        model_type: str = "gpt-3.5-turbo",
        *args,
        **kwargs,
    ) -> str:
        """
        Sends a request to the OpenAI API using the specified parameters.

        This method constructs a message payload with roles 'system' and 'user', then
        sends a request to OpenAI's chat completion API using the provided model.

        Parameters:
        - content_system (str): Content of the system message to be sent to the API.
        - content_user (str): Content of the user message to be sent to the API.
        - model_type (str, optional): The model type to be used for the API request.
                                      Defaults to 'gpt-3.5-turbo'.
        - *args: Variable length argument list.
        - **kwargs: Arbitrary keyword arguments.

        Returns:
        - str: The content of the response message from the API.
        """
        client = OpenAI(api_key=self.api_key)

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"{content_system}",
                },
                {
                    "role": "user",
                    "content": f"{content_user}",
                },
            ],
            model=model_type,
        )
        return response.choices[0].message.content

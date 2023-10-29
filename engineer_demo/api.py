import openai


class APIRequester:
    """Abstract class to handle API requests."""

    def request_api(
        self,
        content_system: str,
        content_user: str,
        model_type: str = "gpt-3.5-turbo",
        *args,
        **kwargs,
    ) -> str:
        response = openai.ChatCompletion.create(
            model=model_type,
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
        )
        return response["choices"][0]["message"]["content"].strip()

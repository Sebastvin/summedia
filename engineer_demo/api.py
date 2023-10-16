import openai


class APIRequester:
    """Abstract class to handle API requests."""

    def request_api(
        self, content_system: str, content_user: str, text: str, *args, **kwargs
    ) -> str:
        response = openai.ChatCompletion.create(
            model=self.model_type,
            messages=[
                {
                    "role": "system",
                    "content": f"{content_system}",
                },
                {
                    "role": "user",
                    "content": f"{content_user}: {text}",
                },
            ],
        )
        return response["choices"][0]["message"]["content"].strip()

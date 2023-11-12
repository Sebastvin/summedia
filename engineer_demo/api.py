from openai import OpenAI


class APIRequester:
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
        # return response["choices"][0]["message"]["content"]

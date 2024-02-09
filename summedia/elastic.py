from summedia.api import APIRequester


class ElasticAPIRequester(APIRequester):
    def elastic_prompt(
        self, content_system: str, content_user: str, model_type: str = None
    ) -> str:
        if model_type:
            return super().request_api(content_system, content_user, model_type)
        else:
            return super().request_api(content_system, content_user)

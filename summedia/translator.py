import pycountry


class Language:
    @classmethod
    def validate_language(cls, lang_code):
        if not pycountry.languages.get(alpha_2=lang_code):
            raise ValueError("Unsupported language")

    @classmethod
    def get_language_name(cls, lang_code):
        return pycountry.languages.get(alpha_2=lang_code).name

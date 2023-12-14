import unittest

from summedia.translator import Language


class TestLanguage(unittest.TestCase):
    def test_validate_language_valid_code(self):
        # Test with a valid language code
        self.assertIsNone(Language.validate_language("en"))  # English

    def test_validate_language_invalid_code(self):
        # Test with an invalid language code
        with self.assertRaises(ValueError):
            Language.validate_language("xx")

    def test_validate_language_non_string(self):
        # Test with a non-string input
        with self.assertRaises(LookupError):
            Language.validate_language(123)

    def test_get_language_name_valid_code(self):
        # Test getting name for a valid language code
        self.assertEqual(Language.get_language_name("en"), "English")

    def test_get_language_name_invalid_code(self):
        # Test getting name for an invalid language code
        with self.assertRaises(AttributeError):
            Language.get_language_name("xx")

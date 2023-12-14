import unittest

from summedia.level import SimplificationLevel


class TestSimplificationLevel(unittest.TestCase):
    def test_enum_values(self):
        """Test the values of each enum member."""
        self.assertEqual(SimplificationLevel.CHILD.value, "child")
        self.assertEqual(SimplificationLevel.TEEN.value, "teen")
        self.assertEqual(SimplificationLevel.STUDENT.value, "student")
        self.assertEqual(SimplificationLevel.EXPERT.value, "expert")

    def test_enum_uniqueness(self):
        """Test that all enum values are unique."""
        values = [member.value for member in SimplificationLevel]
        self.assertEqual(len(values), len(set(values)))

    def test_enum_immutability(self):
        """Test that the enum cannot be modified."""
        with self.assertRaises(AttributeError):
            SimplificationLevel.CHILD = "student"

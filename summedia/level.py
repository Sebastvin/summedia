from enum import Enum, unique


@unique
class SimplificationLevel(Enum):
    CHILD: str = "child"
    TEEN: str = "teen"
    STUDENT: str = "student"
    EXPERT: str = "expert"

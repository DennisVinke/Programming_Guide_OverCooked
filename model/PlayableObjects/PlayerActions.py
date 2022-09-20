from enum import Enum, unique


@unique
class Playeractions(Enum):
    IDLE = 1
    PICK_UP_OBJECT = 2
    PUT_DOWN_OBJECT = 3
    DASH = 4
    CHOP = 5
    INTERACT = 6



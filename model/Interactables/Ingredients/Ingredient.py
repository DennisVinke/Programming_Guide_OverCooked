from enum import Enum
from ..Interactable import Interactable

class IngredientState(Enum):
    UNPREPARED = 1
    PREPARED = 2
    INEDIBLE = 3

    @staticmethod
    def next_state(current_state):
        current_state_value = current_state.value
        if current_state_value + 1 < len(IngredientState):
            return IngredientState(current_state_value+1)
        else:
            return IngredientState(current_state)


class Ingredient(Interactable):
    def __init__(self):
        self.ingredient = None
        self.position = None
        self.interactable = True
        self.state = IngredientState.UNPREPARED

    def set_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position

    def update_state(self):
        self.state = IngredientState.next_state(self.state)
        print(self.state)

    def change_ingredient_state(self):
        pass

    def get_state(self):
        return self.state

    def interact(self):
        pass
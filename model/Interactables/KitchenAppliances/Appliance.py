from ..Interactable import Interactable
from enum import Enum


class Appliance(Interactable):
    def __init__(self):
        self.name = None
        self.active = False
        self.ingredient = None
        self.position = None
        self.interaction_time = 0
        self.current_interaction_time = 0

    def calculate_ingredient_position(self):
        pass

    def set_ingredient(self, ingredient):
        success = False
        if not self.ingredient:
            self.ingredient = ingredient
            ingredient.set_position(self.calculate_ingredient_position())
            success = True
        return success

    #Change in stove to make it possible to burn food
    def done_interacting(self):
        return self.interaction_time - self.current_interaction_time < 0

    def change_ingredient_state(self):
        self.ingredient.update_state()

    def remove_ingredient(self):
        ingredient = self.ingredient
        self.ingredient = None
        return ingredient

    def update_appliance(self):
        if self.active:
            if self.done_interacting():
                self.change_ingredient_state()
            else:
                self.current_interaction_time += 1


    def interact(self, ingredient=None):
        if ingredient is not None:
            return self.set_ingredient(ingredient)

        if self.ingredient:
            if self.ingredient.get_state().value > 1:
                return self.remove_ingredient()


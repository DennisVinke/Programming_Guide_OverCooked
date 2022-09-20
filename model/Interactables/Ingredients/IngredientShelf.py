class Ingredient:
    def __init__(self, ingredientType):
        self.ingredient = ingredientType

    def interact(self):
        return Ingredient(self.ingredient)

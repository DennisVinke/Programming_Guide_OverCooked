from model.Interactables.Ingredients.Ingredient import Ingredient
from model.Interactables.KitchenAppliances.Appliance import Appliance

if __name__ == '__main__':
    tomato = Ingredient()
    cuttingboard = Appliance()

    print(cuttingboard.ingredient)
    cuttingboard.interact(tomato)
    print(cuttingboard.ingredient)
    print("start cutting")
    while cuttingboard.ingredient.get_state().value == 1:
        cuttingboard.interact()
        print(cuttingboard.current_interaction_time, cuttingboard.ingredient.state)
    print("Cutting done")
    cuttingboard.interact()
    print(cuttingboard.ingredient)

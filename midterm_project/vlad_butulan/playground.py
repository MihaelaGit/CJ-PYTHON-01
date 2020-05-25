from shopping_list import *
import unittest


class Test_Recipe(unittest.TestCase):

    def test_recipe_object_attribute_initialization(self):
        ingredients = {'macaroni': 1, 'cheese': 0.5}
        name = "Famous Mac & Cheese"

        recipe = Recipe(name, ingredients)

        self.assertEqual(recipe.name, "Famous Mac & Cheese"), 'Recipe class is missing the name attribute'
        self.assertEqual(recipe.ingredients, {'macaroni': 1, 'cheese': 0.5}), 'Recipe class is missing the ingredients attribute'
        self.assertIsInstance(recipe, Recipe)


class Test_RecipesBox(unittest.TestCase):

    def test_recipesbox_object_attribute_initialization(self):
        ingredients1 = {'macaroni': 1, 'cheese': 0.5}
        name1 = "Test recipe name"

        recipe1 = Recipe(name1, ingredients1)

        rep_box = RecipesBox([recipe1])

        self.assertIsInstance(recipe1, Recipe)
        self.assertIsInstance(rep_box.recipies, list)
        self.assertEqual(rep_box.recipies[0].name, "Test recipe name")
    
    def test_recipesbox_pick_method(self):
        ingredients2 = {'macaroni': 1, 'cheese': 0.5}
        name2 = "Test recipe name 2"

        recipe2 = Recipe(name2, ingredients2)
        recipies_box2 = RecipesBox([recipe2])

        self.assertEqual(str(recipies_box2.pick()), str(recipe2))


class Test_Fridge(unittest.TestCase):

    def test_fridge_object_attribute_initialization(self):
        items = {'item1': 5, 'item2': 10}

        test_fridge = Fridge(items)

        self.assertIsInstance(test_fridge, Fridge)
        self.assertIsInstance(test_fridge.products, dict)
        self.assertEqual(test_fridge.products['item1'], 5)
    
    def test_fridge_take_method(self):
        items = {'item3': 7, 'item4': 15}

        test_fridge2 = Fridge(items)

        self.assertEqual(test_fridge2.take('item3', 2), 2)

    def test_check_the_fridge_fct(self):
        items = {'item3': 5, 'item4': 10}
        test_fridge2 = Fridge(items)

        ingredients3 = {'item3': 1, 'item4': 5, 'item5': 3}
        name3 = "Test recipe name 3"
        recipe3 = Recipe(name3, ingredients3)
        recipies_box3 = RecipesBox([recipe3])

        self.assertEqual(check_the_fridge(test_fridge2, recipies_box3), ["Test recipe name 3"])


mac_and_cheese_ingredients = {
    'macaroni': 1,
    'cheese': 0.5
}

peanut_butter_biscuit_ingredients = {
    'peanut butter': 1,
    'brown sugar': 0.5,
    'egg': 1,
    'vannilla': 1
}

oreo_cake_ingredients = {
    'oreo biscuits': 650,
    'kefir': 600,
    'bicarbonat': 3,
    'cheese': 0.5
}

sponge_cake_ingredients = {
    'egg': 4,
    'vannilla': 1,
    'butter': 225,
    'milk': 1
}

fridge_contents = {
    'peanut butter': 2,
    'brown sugar': 3,
    'egg': 8,
    'vannilla': 2,
    'cheese': 0.5,
    'milk': 2,
    'butter': 200,
    'oreo biscuits': 650
}

mac_and_cheese = Recipe("Famous Mac & Cheese", mac_and_cheese_ingredients)
peanut_butter_biscuit = Recipe("Unknown Biscuit", peanut_butter_biscuit_ingredients)
oreo_cake = Recipe("The Oreo Cake", oreo_cake_ingredients)
sponge_cake = Recipe("The Sponge", sponge_cake_ingredients)

recipies_box = RecipesBox()
recipies_box.append(mac_and_cheese)
recipies_box.append(peanut_butter_biscuit)
recipies_box.append(oreo_cake)
recipies_box.append(sponge_cake)

fridge1 = Fridge(fridge_contents)

# List recipe/fridge ingredients
print(f"Printing a recipe:\n{peanut_butter_biscuit}\n")
print("Pritty printing a recipe:")
peanut_butter_biscuit.pp_print_recipe()
print("\nPritty printing a fridge:")
fridge1.pp_print_recipe()

# List contents of RecipesBox
print(f"\nPrinting the RecipesBox contents:\n{recipies_box}\n")

# Test pick() method of RecipesBox
print(f"Removing a recipe randomly from RecipiesBox:\n{recipies_box.pick()}\n")
print(f"Remaining ingredients after pick:\n{recipies_box}\n")

# Test the fridge products listing
print(f"Printing Fridge contents:\n{fridge1}\n")

# Adding ingredients in the fridge
fridge1.update({'chicket leg': 2})
print(f"Adding chicket legs in fridge:\n{fridge1}\n")

# Test check_recipe()
print(f"Check_recipe for mac_and_cheese:\n{fridge1.check_recipe(mac_and_cheese)}\n")

# Taking 8 eggs from fridge
print(f"Taking 8 eggs from fridge:\n{fridge1.take('egg', 8)}\n")
print(fridge1)

# Testing check_the_fridge() method
print(f"\nChecking the fridge based on recipies box:\n{check_the_fridge(fridge1, recipies_box)}\n")

# testing prepare_shopping_list() and pretty_print_recipe()
print(f"Preparing a shopping list peanut_butter_biscuit:\n{prepare_shopping_list(fridge1, peanut_butter_biscuit)}\n")
print(f"Preparing a shopping list for mac_and_cheese:\n{prepare_shopping_list(fridge1, mac_and_cheese)}\n")

# check archive list
print(f"Checking archive list: {shopping_list_archive}\n")

if __name__ == '__main__':
    unittest.main()

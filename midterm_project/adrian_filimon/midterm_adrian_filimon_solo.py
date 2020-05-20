import random
from collections.abc import MutableMapping, MutableSequence, Iterable, Collection, Container, Sized


class Recipe:
    def __init__(self, name, ingredients):
        self._name = name
        self._ingredients = ingredients

    def __repr__(self):
        return self._name

    def __getitem__(self, item):
        return self._ingredients[item]

    def __iter__(self):
        return iter(self._ingredients)

    def __len__(self):
        return len(self._ingredients)

    def __contains__(self, item):
        return item in self._ingredients

    def keys(self):
        return self._ingredients.keys()



class RecipesBox:
    def __init__(self):
        self.recipes = []

    def __getitem__(self, index):
        return self.recipes[index]

    def __delitem__(self, index):
        return self.recipes[index]

    def __setitem__(self, index, value):
        self.recipes[index] = value

    def __len__(self):
        return len(self.recipes)

    def __iter__(self):
        return iter(self.recipes)

    def __contains__(self, item):
        return item in self.recipes

    def __reversed__(self):
        return reversed(self.recipes)

    def insert(self, index, value):
        self.recipes[index] = value

    def pick(self, name=None):
        if name and name in self.recipes:
            return name
        else:
            return self.recipes[random.randint(0, len(self.recipes))]

    def add(self, recipe):
        self.recipes.append(recipe)

    def delete(self, name=None):
        if name:
            self.recipes.remove(name)
        else:
            print('What do you want to remove?')

    def list_recipes(self):
        for recipe in self.recipes:
            print(recipe.name, "\n")


class Fridge:
    def __init__(self):
        self.items = {}

    def __getitem__(self, index):
        return self.items[index]

    def __delitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

    def add(self, item_name, item_quantity):
        self.items[item_name] = item_quantity

    def remove(self, item_name):
        del self.items[item_name]

    def search(self, ingredient):
        if self.items.get(ingredient):
            return True
        else:
            return False



cheesee_burger_ingredients = {
    'bun': 1,
    'beef_pork': 1,
    'cedar cheese': 0.5,
    'onion': 2,
    'salad': 1,
    'sauce': 2
}

submarine_sandwich_ingredients = {
    'long_roll': 1,
    'pork_veal_mince_meatballs': 3,
    'parmesan': 0.25,
    'tomato_passata': 0.5,
    'garlic_cloves': 2,
    'egg': 1
}

spaghetti_carbonara_ingredients = {
    'spaghetti': 0.25,
    'bacon': 0.2,
    'parmesan': 0.25,
    'olive_oil': 0.3,
    'egg_yolk': 2,
    'egg': 2
}



cheese_burger = Recipe('Beef Burger', cheesee_burger_ingredients)
submarine_sandwich = Recipe('Submarine Sandwich', submarine_sandwich_ingredients)
spaghetti_carbonara = Recipe('Spaghetti Carbonara', spaghetti_carbonara_ingredients)

recipes_box = RecipesBox()
recipes_box.add(cheese_burger)
recipes_box.add(submarine_sandwich)
recipes_box.add(spaghetti_carbonara)

fridge = Fridge()
fridge.add('garlic', 50)
fridge.add('egg', 30)
fridge.add('bacon', 20)
fridge.add('parmesan', 10)
fridge.add('beef_pork', 5)

print(fridge.search('garlic'))



################################################################################################
recipe_MutSeq = RecipesBox
fridge_MutMap = Fridge
abcs = [MutableMapping, MutableSequence]
for abc in abcs:
    print(
        'our class is a {}: {}'.format(
            abc.__name__, isinstance(fridge_MutMap, abc))
    )
#################################################################################################
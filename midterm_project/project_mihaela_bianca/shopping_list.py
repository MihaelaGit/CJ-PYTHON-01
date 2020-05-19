import random
import pprint

archived_list = []

pp = pprint.PrettyPrinter(indent=4)

__header__ = '''
   ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
'''
__footer__ = r'''
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.
'''


class PrettyPrinterMixin:

    def pp_print_recipe(self):

        pp.pprint(super().__str__())




class Recipe(PrettyPrinterMixin):

    def __init__(self, name, ingredients):
        """
        Ingredients should be a dictionary
        {egg:3, milk:3, flour:2, sugar:1}
        """
        self.name = name
        self.ingredients = ingredients
        self.recipe = {self.name: self.ingredients}
        if len(self.ingredients) < 4:
            raise Exception('The ingredients number should be  at least 4 !')

    def __iter__(self):
        return self.recipe

    def __getitem__(self, index):
        return self.recipe[index]

    def __len__(self):
        return len(self.recipe)

    def __str__(self):

        dash = '*' * 30
        result = ' {} \n{} \n{} \n '.format(dash, 'Famous ' + self.name, dash)

        for index, ingredients in enumerate(self.ingredients, start=1):
            result += '\n{}  {} :{} \n '.format(index, ingredients, self.ingredients[ingredients])
        result += '\n {}'.format(dash)
        return result

    def keys(self):
        return self.recipe.keys()

    def values(self):
        return self.recipe.values()

    def display(self):
        print('{} = \n {} \n '.format(self.name + '_ingredients', self.ingredients))


class RecipesBox:
    recipe = None

    def __init__(self, *args):
        """
             RecipesBox should be a list that holds our recipes
             [...]
        """
        self.recipe = list(args)

    def __iter__(self):
        return RecipesBox(self.recipe)

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        return self.recipe[item]

    def __setitem__(self, key, value):
        self.recipe[key] = value

    def __delitem__(self, key):
        del self.recipe[key]

    def __len__(self):
        return len(self.recipe)

    def insert(self, index, value):
        return self.recipe.insert(index, value)

    def add_recipe(self, name):
        self.recipe.append(name)
        # return self.recipes_list

    def delete_recipe(self, name):
        if len(self.recipe) >= 6:
            self.recipe.remove(name)
        #   return self.recipes_list
        else:
            raise ValueError('The recipe cannot be deleted from the RecipeBox!')

    def pick(self, recipe=None):
        if recipe:
            return Recipe(recipe.name, recipe.ingredients)
        else:
            return random.choice(self.recipe)

    def __str__(self):
        keys_list = []
        for recipe in self.recipe:
            keys_list.append(recipe.name)
        print_string = ''
        for recipe_name in keys_list:
            print_string = '\n '.join((print_string, recipe_name))

        return print_string


class Fridge(PrettyPrinterMixin):
    def __init__(self, ingredients):
        """
        Ingredients should be a dictionary
        {egg:3, milk:3, flour:2, sugar:1}
        """

        self.ingredients = ingredients
        if len(self.ingredients) < 5:
            raise Exception('The ingredients number should be  at least 5 !')

    def __str__(self):
        dash = '*' * 30
        result = ' {} \n{} \n{} \n '.format(dash, 'The fridge contains: ', dash)
        for index, ingred in enumerate(self.ingredients, start=1):
            result += '\n{}  {} :{} \n '.format(index, ingred, self.ingredients[ingred])
        result += '\n {}'.format(dash)
        return result

    def __getitem__(self, item):
        return self.ingredients[item]

    def __setitem__(self, key, value):
        self.ingredients[key] = value

    def __delitem__(self, key):
        del (self.ingredients[key])

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.ingredients)

    def check_ingredient(self, name):
        if name in list(self.ingredients.keys()):
            return 'Yes'
        else:
            return 'Nope'

    def add_ingredient(self, name, qty):
        if name in self.ingredients.keys():
            self.ingredients[name] += qty

        else:
            self.ingredients[name] = qty

    def remove_ingredient(self, name, qty):
        if name in self.ingredients.keys():
            self.ingredients[name] -= qty
            if self.ingredients[name] <= 0:
                del self.ingredients[name]
                return 'The ingredient {} is completely removed from the fridge !'.format(name)
        else:
            return 'The ingredient {} is not in the fridge at all !'.format(name)

    def check_recipe(self, recipe):

        existing_items = list(filter(lambda x: x in self.ingredients, recipe.ingredients))
        missing_items = list(filter(lambda x: x not in self.ingredients, recipe.ingredients))
        return existing_items, missing_items


def check_the_fridge(fridge, recipesbox):
    recipes_list = []
    ingred_in = []
    for recipe_index in range(len(recipesbox.recipe)):

        for ingredient in recipesbox.recipe[recipe_index].ingredients:
            if ingredient in fridge.ingredients:
                ingred_in.append('yes')

        if len(ingred_in) / len(recipesbox.recipe[recipe_index].ingredients) >= 0.5:
            recipes_list.append(recipesbox.recipe[recipe_index].name)

        del ingred_in[0:len(recipesbox.recipe[recipe_index].ingredients)]
    print(recipes_list)


def archive_shopping_list(fnc):
    def archive_list(fridge, recipe):
        archived_list.append(fnc(fridge, recipe))
        return fnc(fridge, recipe)

    return archive_list


def pretty_print_recipe(fnc):
    def wrapper(fridge, recipe):
        shopping_list = fnc(fridge, recipe).items()
        list_str = "\n".join(["\t| {0}. {1}: {2} {3}|.".format(
            index + 1, key, value, (22 - (len(str(index + 1)) + len(str(key)) + len(str(value)))) * " ")
            for index, (key, value) in enumerate(shopping_list)])
        print("".join([
            __header__,
            "\t| \t\tShopping list: \t\t |. \n",
            "\t| \t\t\t\t\t\t\t |.\n",
            "\t| \t\t\t\t\t\t\t |.\n",
            list_str,
            __footer__
        ]))
        return fnc(fridge, recipe)
    return wrapper




@archive_shopping_list
@pretty_print_recipe
def prepare_shopping_list(fridge, recipe):
    ingr = fridge.check_recipe(recipe)
    shopping_list = {}
    if len(ingr[1]):
        shopping_list.update({item: recipe.ingredients[item] for item in ingr[1]})
    if len(ingr[0]):
        for item in ingr[0]:
            if recipe.ingredients[item] > fridge.ingredients[item]:
                shopping_list.update({item: recipe.ingredients[item] - fridge.ingredients[item]})
    return shopping_list

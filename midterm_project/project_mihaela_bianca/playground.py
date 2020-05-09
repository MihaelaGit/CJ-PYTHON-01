import random


# class PrettyPrinter:
#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwargs = kwargs
#     def __iter__(self):
#         return self.kwargs
#     def __str__(self):
#         message='ceva '
#         dash = '*' * 30
#         result = ' {} \n{} \n{} \n '.format(dash, message, dash)
#         for index, ingred in enumerate(self.kwargs, start=1):
#             result += '\n{}  {} :{} \n '.format(index, ingred, self.kwargs[ingred])
#         result += '\n {}'.format(dash)
#         return result

class Recipe:

    def __init__(self, name, ingredients):
        """
        Ingredients should be a dictionary
        {egg:3, milk:3, flour:2, sugar:1}
        """
        self.name = name
        self.ingredients = ingredients
        if len(self.ingredients) < 4:
            raise Exception('The ingredients number should be  at least 4 !')

    def __iter__(self):
        return self.ingredients

    def __str__(self):
        dash = '*' * 30
        result = ' {} \n{} \n{} \n '.format(dash, 'Famous ' + self.name, dash)

        for index, ingredients in enumerate(self.ingredients, start=1):
            result += '\n{}  {} :{} \n '.format(index, ingredients, self.ingredients[ingredients])
        result += '\n {}'.format(dash)
        return result

    def display(self):
        print('{} = \n {} \n '.format(self.name + '_ingredients', self.ingredients))




class RecipesBox(Recipe):

    def __init__(self, recipes_list):
        """
             RecipesBox should be a list with the recipe's names
             ['Fries', 'Banana bread', 'Cheesecake']
        """
        self.recipes_list = recipes_list

    def __iter__(self):
        return self.recipes_list

    def add_recipe(self, name):

        self.recipes_list.append(name)
        return self.recipes_list

    def delete_recipe(self, name):
        if len(self.recipes_list) >= 6:
            self.recipes_list.remove(name)
            return self.recipes_list
        else:
            raise ValueError('The recipe cannot be deleted from the RecipeBox!')

    def pick(self):
        return random.choice(self.recipes_list)
        # print('The random recipe is {}'.format(random.choice(self.recipes_list)))

    def __str__(self):
        return 'The recipes are : \n {}'.format(str(self.recipes_list))


class Fridge:
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

    def check_ingredient(self, name):
        if name in self.ingredients.keys():
            return 'The ingredient {} is in the  fridge!'.format(name)
        else:
            raise ValueError('The ingredient {} is not in the  fridge!'.format(name))

    def check_recipe(self, recipe_name):

        if recipe_name == Recipe(name,ingredients):
            for ingredient in recipe.ingredients:
                return check_ingredient(ingredient)



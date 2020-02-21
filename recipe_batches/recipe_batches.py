#!/usr/bin/python

import math

# function will take in two dictionaries
# one dictionary will be my ingredients I currently have
# the other dictionary will be the recpie it takes to make something
# I need to find out how many times I can make a recipe based on my ingredients
# I believe I'll need atleast 2 loops.
# The ingredients dictionary depends on the recipe dictionary to make sure it has all the same keys regardless of value of the keys
# Need to check each Key and see it maches the recipe dictionary
# somehow check how many times our value of our ingredients goes into the recipes
# Then output a round number for how many times we can make that recipe


def recipe_batches(recipe, ingredients):
    # Keep track of how many recipes we can make with our ingredients
    bakes = []

    # check first to see if we have all the right keys in the recipe dictionary with our ingredients dictionary
    for item in recipe:
        # if we don't have the ingredient then we just can't make the recipe
        if item not in ingredients:
            return 0
        # If the ingredient exists, we divide it by the amount needed in the recipe. If its greater than 0, then we determine what is needed for the bakes
        if ingredients[item] // recipe[item] > 0:
            # then just divide to find the amount we need for the recipe
            bakes.append(ingredients[item] // recipe[item])
        else:
            # this only happens when there is not enough ingredients for the recipe:
            return 0
    return min(bakes)

    # for k in recipe.items():
    #     print(k)
    #     if k in list(ingredients.items()):
    #         print(True)
    #     else:
    #         print(False)
    # for key in list(recipe.keys()):
    #     if key in list(ingredients.keys()):


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
# {'milk': 100, 'butter': 50, 'flour': 5}
# {'milk': 132, 'butter': 48, 'flour': 51}

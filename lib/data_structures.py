spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    '''contains function get_names() that retrieves names from list of foods.'''
    result = []
    for food in spicy_foods:
        result.append(food["name"])
    return result
# return [food["name"] for food in spicy_foods]   cleaner approach
def get_spiciest_foods(spicy_foods):
    '''contains function get_spiciest_foods() that returns foods with a heat_level over 5.'''
    result = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            result.append(food)
    return result
    # return [food for food in spicy_food if food["heat_level"] > 5] cleaner approach

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        # Explicit \n to match the test exactly
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}\n", end="")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food["heat_level"]
    return total // len(spicy_foods)  # integer division since test expects 6, not 6.0

    # return sum(food["heat_level"] for food in spicy_foods) // len(spicy_foods)   cleaner approach

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods 

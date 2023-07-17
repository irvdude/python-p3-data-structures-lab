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
    food_names = []

    for food in spicy_foods:
        food_names.append(food["name"])

    return food_names
    pass


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []

    for spiciest in spicy_foods:
        if spiciest["heat_level"] > 5:
            spiciest_foods.append(spiciest)

    return spiciest_foods
    pass


def print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        print(
            foods["name"]
            + " ("
            + foods["cuisine"]
            + ") "
            + "| "
            + "Heat Level: "
            + foods["heat_level"] * "🌶"
        )
    pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
        if foods["cuisine"] == cuisine:
            return foods

    pass


def print_spiciest_foods(spicy_foods):
    for foods in spicy_foods:
        if foods["heat_level"] > 5:
            print(
                foods["name"]
                + " ("
                + foods["cuisine"]
                + ") "
                + "| "
                + "Heat Level: "
                + foods["heat_level"] * "🌶"
            )
    pass


def get_average_heat_level(spicy_foods):
    # Use list comprehensions to extract heat_levels from array and assign to var
    heat_level = [food["heat_level"] for food in spicy_foods]
    # sum is equal to extracted heat levels using sum function
    sum_of_levels = sum(heat_level)
    # avg is calculated by taking sum and dividing it by count of all elements
    avg_heat_level = sum_of_levels / len(spicy_foods)
    # retrun avg
    return avg_heat_level

    pass


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

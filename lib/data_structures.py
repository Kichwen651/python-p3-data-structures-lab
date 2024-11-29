# List of spicy foods
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

# Function to get the names of all spicy foods
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# Function to get the spiciest foods (heat level over 5)
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# Function to print the names and heat levels of all spicy foods with 🌶 emojis
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]  # Create a string with 'heat_level' number of 🌶 emojis
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

# Function to get all spicy foods by a specific cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Iterate through the list of spicy foods
    for food in spicy_foods:
        # Check if the cuisine matches
        if food["cuisine"]== cuisine:
            return food  # Return the first match
    else:
     return None  # If no match is found, return None

# Function to print the spiciest foods
def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    for food in spiciest:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

# Function to get the average heat level of all spicy foods
def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)

# Function to create a new spicy food and add it to the list
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

    


import json
import os

RECIPES_FILE = 'recipes.json'

def load_recipes():
    if not os.path.exists(RECIPES_FILE):
        return {}
    with open(RECIPES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_recipes(recipes):
    with open(RECIPES_FILE, 'w', encoding='utf-8') as f:
        json.dump(recipes, f, ensure_ascii=False, indent=4)

def add_recipe(recipes, name, ingredients):
    recipes[name] = ingredients
    save_recipes(recipes)

def list_recipes(recipes):
    for name, ingredients in recipes.items():
        print(f"- {name}: {', '.join(ingredients)}")

def delete_recipe(recipes, name):
    if name in recipes:
        del recipes[name]
        save_recipes(recipes)
        print(f"Recipe '{name}' removed.")
    else:
        print(f"Recipe '{name}' not found.")

if __name__ == "__main__":
    recipes = load_recipes()
    while True:
        print("\n1) Add Recipe")
        print("2) List Recipes")
        print("3) Remove Recipe")
        print("4) Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            ingredients = [ing.strip() for ing in ingredients]
            add_recipe(recipes, name, ingredients)
        elif choice == '2':
            list_recipes(recipes)
        elif choice == '3':
            name = input("Enter recipe name to remove: ")
            delete_recipe(recipes, name)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

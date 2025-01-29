import os
import pytest
from recipes import load_recipes, add_recipe, delete_recipe

TEST_FILE = 'test_recipes.json'

@pytest.fixture
def setup_test_env(monkeypatch):
    monkeypatch.setattr('recipes.RECIPES_FILE', TEST_FILE)
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_and_delete_recipe(setup_test_env):
    # Initially empty
    recipes = load_recipes()
    assert len(recipes) == 0

    # Add recipe
    add_recipe(recipes, "Pasta", ["Noodles", "Tomato Sauce"])
    recipes = load_recipes()
    assert "Pasta" in recipes
    assert recipes["Pasta"] == ["Noodles", "Tomato Sauce"]

    # Remove recipe
    delete_recipe(recipes, "Pasta")
    recipes = load_recipes()
    assert "Pasta" not in recipes
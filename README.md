# lol8

## Run using docker/podman
```
    docker build -t recipe-app .

    docker run -it --rm recipe-app

    To run tests:
    docker run -it --rm recipe-app pytest test_recipes.py
```
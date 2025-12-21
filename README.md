# Conway-s-Game-of-Life-rebuilt

This is my attempt at building Conway's game of life in multiple languages.

My first attempt is to do it in Python using Pygame and other libraries. I do plan on showcasing these on my website.

## Running with Python

To run the Python version I recommend that you set up a python virtual environment, you can do this with the following command

`python<version> -m venv /path/to/virtual/environment`

After that you can use it to run the program and pip installs to get the libraries.

### Installing dependencies

The following commands should install any dependencies and ensure you are ready to run the program.

`pip install --upgrade pip` - This will update pip to the version compatible with the virtual environment.

`pip install pygame pygame-menu pygbag numpy importlib` - This will install the dependencies needed for the project.

### Running the program

Running the program is fairly simple.

Starting the program can be done with the following command:

`python<version> -m src.main`

Once running the menu is fairly simple and some parts do not work at the moment. However once in game the right mouse will remove a cell and a left click will create a cell. To start the simulation you press the return button, this will prevent you from making new cells. the same button will stop the simulation in place. To clear the screen and stop the simulation if running simply press C. Escape will pause the game but the simulation will not stop. To exit press escape and follow prompts to quit the game.

# Conway-s-Game-of-Life-rebuilt

This is my attempt at building Conway's game of life in multiple languages.

My first attempt is to do it in Python using Pygame and other libraries. I do plan on showcasing these on my website.

## Setting up Python

To run the Python version of this program, I recommend that you set up a python virtual environment. The current recommended Python version is Python 3.13 by Pygame. You can set up the virtual environment with the following command:

`python3.13 -m venv /path/to/virtual/environment`


After that you can use it to run the program and pip installs to get the libraries.

### Installing dependencies

The following commands should install any dependencies and ensure you are ready to run the program.

`pip install --upgrade pip`
 - This will update pip to the version compatible with the virtual environment.

`pip install pygame pygame-menu numpy`
 - This will install the dependencies needed for the project.

### Running the program

Running the program is fairly simple. Starting the program can be done with the following command:

`python -m src.main`


### Basic Controls

Once running, the menu is fairly simple and some parts are still a work in progress. This can be navagated by using the Left mouse and clicking on the buttons on-screen to navigate.

Once in the game:

- Use Right mouse will remove a cell
- Use Left mouse will create a cell. 
- Use Return/ Enter to start/stop the simulation
   - NOTE: This will prevent you from making new cells while the simulation is running. 
- Use C to clear the screen and stop the simulation. 
- Use Escape to pause the game 
    - NOTE: The simulation will not stop. 
- To exit press escape and follow prompts to quit the game.

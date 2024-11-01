US States Game
This is an interactive game using Python's turtle graphics library, where players try to guess the names of all 50 US states. For each correct guess, the state name is displayed on a map of the United States at the state's approximate location.

Features
Allows users to input guesses through a dialog box.
Displays each guessed state name on the map in its correct location.
Counts the number of correct guesses.
Exits the game when the user types "exit."
Requirements
Python 3.x
turtle library (comes pre-installed with Python)
pandas library
Installation
Clone the repository or download the script and the necessary files.

Install the pandas library if it's not already installed:

bash
Copy code
pip install pandas
Make sure the following files are in the same directory as the Python script:

50_states.csv: A CSV file containing data on US states, including their names and coordinates on the map.
blank_states_img.gif: An image file of a blank map of the US to serve as the game background.
How to Play
Run the script:

bash
Copy code
python us_states_game.py
A window with a blank map of the United States will appear.

A prompt will appear asking you to guess the name of a state.

Enter the name of a US state and press "OK."

If your guess is correct, the name of the state will appear on the map at the correct location.
The game keeps track of how many states you've guessed correctly.
You can type "exit" at any time to close the game.

Code Explanation
The 50_states.csv file contains:

state: The name of each state.
x: The x-coordinate of each state on the map.
y: The y-coordinate of each state on the map.
Game Loop:

The game loop runs as long as is_game_on is True.
For each guess, the program checks if the guessed name matches a state name.
If correct, it writes the state name at its (x, y) position on the map.
If "exit" is entered, the game loop ends.
Known Issues
If a user repeatedly guesses the same state, it will still count toward the total score.
Some locations may overlap on the map when state names are displayed.
Example CSV Structure (50_states.csv)
state	x	y
Alabama	-75	50
Alaska	-130	-200
Arizona	-100	-100
Note: The actual coordinates will depend on your map's scaling and layout.
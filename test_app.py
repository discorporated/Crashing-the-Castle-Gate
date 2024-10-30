"""
Crashing the Castle Gate: A simple Python terminal-based game with an ASCII welcome screen.
The player will be able to start the game, view credits, or exit.
"""
import sys
import os
import time
import keyboard

# Constants
MIN_TERMINAL_HEIGHT = 25
MIN_TERMINAL_WIDTH = 60

# Clear terminal function
def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    size = os.get_terminal_size()
    return size.lines, size.columns
# Get terminal size
def get_terminal_size():
    """Get the current terminal size."""
    return os.get_terminal_size().lines, os.get_terminal_size().columns

# Check terminal size
def check_terminal_size():
    """Check if the terminal size is big enough for the game."""
    height, width = get_terminal_size()
    if height < MIN_TERMINAL_HEIGHT or width < MIN_TERMINAL_WIDTH:
        print(f"Terminal size is too small! Requires at least {MIN_TERMINAL_HEIGHT} lines "
              f"and {MIN_TERMINAL_WIDTH} columns.")
        return False
    return True

# ASCII welcome screen
def display_welcome_screen():
    """Displays the welcome screen ASCII art."""
    clear_terminal()
    print("Welcome to Crashing the Castle Gate!")
    # Insert the large ASCII art here.
    # Copy and paste the ASCII art file content below:
    print("""
                .:. :: ::::...........:::........:::::::.....::::::::::::..:::..........................................................
C               ..: .:.::::............::::::::::::..::::::::::::::------:::::...................:::--:.......................:.::::::::
R               ..:. ::.::::.........:.::::::::::.::...::::::::::----==-===-::::::..::.......::::::::::...:::......:::::::::::::::---:::
A               ::.: .-..::::.........:::::::::::::::::::---:::-======-.-==++==---------==-::--------::::---:::::---------::::::::::...:
S               ::.:. -:.-:.::::.........:::::---:::::::::---:---====+..---=--------------=======++++**##*++===++***+++===------::......
H               .::::..-::-::::::...........:.:-==---:---:----===-.-++..===========----=====++**##%%%@@@@@@%%%%%%%##**+++===---:::......
I               .::-:: .-::-::::::::.........:::--===-------===+==.:::..-========++++++*******###%%%%@@@%%%#%%%##**+=---------::::......
N               ..::-:: ::..::-:::::::......::::-:-==++====-=+++=.....-:-++=====+++****++*****#**####%%%%%%###*++===----------::::......
G               :...:::..:::.:::--::::......::-:--:--+*+++++++++=.....-::-=+++===+++++++++*******#########*#*++====--------:---::.......
                .::.::::..:--::::---:::::....--:--::--=**+***+*-....:::..-:*#+++==+++++++++*******###*+=++++====-------------=::........
T                ::..:::..:--::::----::-:::..:-::--:::-===***-*-.......::::+*-*+++++++***+++**##%%#%#==========------------:==-:........
H                .::.:::: .-::-:-:--------:::::::--:----==+*+..........:..::.=##**++++*##########%%*+=====-=----::-------:::---:........
E                 .::.-::..:::-==----------:::::::----====++=.........::..::::=%%#******##%%%%%*++=========----::----:---::-::-.........
                   .-..-:. .:-:=+-:--:--------::::::---===+=:...............--==#*+######%%@%#*+==========---::--===-:-::::-:::.........
C               .   :=.:::...::-==--:::::----::::::::--===-.................--::::*%%###%%#*+++==========-------+*+=---:.:-::::.........
A               ... .=:.:.:..::::-:-:.:...::::::::::::----:................::--:::=%@*#%#**++++=++++===-----====++---::::--:::.......::-
S               .... ::::..:::.-::-:-:.::.....::::::::::::...................----::=+-##****+++++++===---==+++===-:::::-::::......::---:
T                .....:-::....::--::--:.:::...::-:::::::.....................:=-:-:..:+%#*#******=----====++++==-::::::::.......::---:..
L                 .....:::.....:.-::----:::::::::::::::......................:-----:::-*--#*****+-::==++**+=++-:::::::::......::--:.....
E               .........:......::::--===--:::::::::::::.................:::::---==--::::-+##**+=---=**+=+====-::::::.......:::.........
                ................::::::------::::-:::::::::.................:::--=====-::::-###*===++***-:::--::::--:.....::--:..........
G               ... ...............:::::-====-:::---:::::::::::....::..........:-===----::-=***+****=-=-:::-:::::::....:--=-:.........::
A               ..... .........:..  .::--:--===---:..::::::---::::::::::::::--=--:..:----:::=******+----------:::::::::---:.............
T                 ...............:....::-::---==-.  ..:--:.:-----::::::::==-::...:..:::---:--=+***+=---------::::::::::::............... 
E                  ....... .:............::::.::.  . .::---::---------:..:---:::::::::---=---::+++======----:::::::::::::............... 
                       ......................       . ..:------=====-..... ...:::--=-----===-::-========----:::::::::::::...............
    """)
    print("\n1. Start Game")
    print("2. Credits")
    print("3. Exit")
    print("\nPlease choose an option:")

# Display credits
def display_credits():
    """Displays game credits."""
    clear_terminal()
    print("Crashing the Castle Gate\n")
    print("Created by: discorporated")
    print("MIT License, 2024")
    print("Game Concept: Inspired by your favorite gothic settings.")
    print("\nPress any key to return to the menu.")
    keyboard.read_event()  # Wait for key press to go back to menu
    display_welcome_screen()

# Game menu
def game_menu():
    """Game menu to choose between start, credits, or exit."""
    while True:
        display_welcome_screen()
        # Wait for user input for menu selection
        while True:
            if keyboard.is_pressed('1'):
                start_the_game()
                break
            elif keyboard.is_pressed('2'):
                display_credits()
                break
            elif keyboard.is_pressed('3'):
                print("Exiting the game...")
                time.sleep(1)
                sys.exit()
            time.sleep(0.1)

# Game loop: Displays ASCII and waits for player input
def game_loop():
    """Main game loop to handle player input."""
    while True:
        clear_terminal()

        # Display the ASCII art (the game scene, like castle, etc.)
        print("Game Scene: Display ASCII here.")
        # Display prompt below the scene
        print("\nPress 'q' to quit or any other key to continue...")

        # Wait for the player's input
        if keyboard.is_pressed('q'):
            print("Exiting the game...")
            time.sleep(1)
            break

        time.sleep(0.1)  # Short delay to avoid input over-triggering

# Start the game
def start_the_game():
    """Function to start the game after terminal size check."""
    if not check_terminal_size():
        time.sleep(3)
        sys.exit()  # Exit if the terminal is too small
    print("Starting the game...")
    time.sleep(1)
    clear_terminal()

    # Start the simplified game loop (no AI, just ASCII and player input)
    game_loop()

# === TESTS SECTION ===
# These are pytest-compatible tests
def hello_world():
    """Function returning 'Hello World'."""
    return "Hello World"

def test_hello_world():
    """Test hello_world function."""
    assert hello_world() == "Hello World"

# Entry point for running the game or tests
if __name__ == "__main__":
    clear_terminal()
    print("Welcome to Torrent!")
    time.sleep(1)
    game_menu()

# EOF

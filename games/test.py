"""
import curses

def get_arrow_key(stdscr):
    key = stdscr.getch()
    if key == curses.KEY_UP:
        return "UP"
    elif key == curses.KEY_DOWN:
        return "DOWN"
    elif key == ord('q'):
        return "QUIT"
    else:
        return None

# Example usage
print("Press the arrow keys (Up or Down). Press 'q' to quit.")

# Initialize curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

try:
    while True:
        user_input = get_arrow_key(stdscr)

        if user_input == "UP":
            print("Up arrow pressed.")
        elif user_input == "DOWN":
            print("Down arrow pressed.")
        elif user_input == "QUIT":
            break
        else:
            print("Invalid input. Press the arrow keys (Up or Down) or 'q' to quit.")

finally:
    # End curses mode
    curses.endwin()
"""

"""
import os
import sys

def get_arrow_key():
    print("Press the arrow keys (Up or Down). Press 'q' to quit.")

    while True:
        try:
            # Use termios to configure terminal settings
            os.system("stty -echo raw")
            key = ord(sys.stdin.read(1))

            if key == 27:  # Escape sequence for arrow keys
                key = ord(sys.stdin.read(2))  # Read the next two characters

                if key == 65:
                    return "UP"
                elif key == 66:
                    return "DOWN"
            elif key == ord('q'):
                return "QUIT"
        finally:
            # Reset terminal settings
            os.system("stty echo -raw")

# Example usage
while True:
    user_input = get_arrow_key()

    if user_input == "UP":
        print("Up arrow pressed.")
    elif user_input == "DOWN":
        print("Down arrow pressed.")
    elif user_input == "QUIT":
        break
    else:
        print("Invalid input. Press the arrow keys (Up or Down) or 'q' to quit.")
"""

import random
import getpass
import socket

username = getpass.getuser()
hostname = socket.gethostname()

print(f"Let's play a game {username}!")

while True:
    low = 1
    high = int(input('You think of a number, and I\'ll guess it!\n> The number is between 1 and ... [you decide]: '))

    print("Great! Now write:\n- 'l' if the guess is too low,\n- 'h' if it's too high, or\n- 'f' if it's correct!\n")

    previous_guess = None

    while True:
        random_guess = random.randint(low, high)

        # Generate a new random guess that is different from the previous one
        while random_guess == previous_guess:
            random_guess = random.randint(low, high)

        feedback = input(f"Is {random_guess} your number? ")

        if feedback == 'l':
            low = random_guess + 1
        elif feedback == 'h':
            high = random_guess - 1
        elif feedback == 'f':
            break

        # Set the current guess as the previous guess for the next iteration
        previous_guess = random_guess

    play_again = input('haha gg\nDo you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break


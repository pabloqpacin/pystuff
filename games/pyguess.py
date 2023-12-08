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

        while random_guess == previous_guess:
            random_guess = random.randint(low, high)

        feedback = input(f"Is {random_guess} your number? ")

        if feedback == 'l':
            low = random_guess
        elif feedback == 'h':
            high = random_guess - 1
        elif feedback == 'f':
            break

        previous_guess = random_guess

    play_again = input('haha gg\nDo you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break

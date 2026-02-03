import random


def guess_the_number(lower_bound: int = 1, upper_bound: int = 100):
    """
    Play a number guessing game where the user tries to guess
    a randomly generated number between lower_bound and upper_bound.
    """

    number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        try:
            # Enter your guess
            user_input = int(
                input(f"Enter a number between {lower_bound} and {upper_bound}: ")
            )
        except ValueError:
            print("Please enter a valid integer")
            continue

        attempts += 1

        # See if your guess is too high or too low
        if user_input < number:
            print(f"My number is greater than {user_input}")
        elif user_input > number:
            print(f"My number is less than {user_input}")
        else:
            # The app will tell you when you are right, and how many guesses you had
            print(f"Well done! It took you {attempts} attempts to guess this number")
            break

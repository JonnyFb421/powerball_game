""" Powerball simulator game """
from random import randrange


def number_is_valid(number, is_powerball):
    """
    Determines the number is within the acceptable range
    :param number: (string) Number to validate
    :param is_powerball: (boolean) True if number is powerball
    :return: Boolean - True if number is valid
    """
    if is_powerball:
        return 1 <= number <= 26
    else:
        return 1 <= number <= 69


def get_numbers():
    """
    Prompt the user to get their lottery numbers
    :return: List of integers
    """
    number_of_lotto_numbers = 3
    user_lotto_numbers = []
    for i in range(number_of_lotto_numbers):
        is_powerball = False
        if i == number_of_lotto_numbers - 1:
            is_powerball = True
            number = int(input(f"Select a powerball number: "))
        else:
            number = int(input(f"Select a number: "))
        while not number_is_valid(number, is_powerball):
            if is_powerball:
                number = int(input(f"Your Powerball input '{number}' is not valid.  Please select a number 1-26 "))
            else:
                number = int(input(f"Your input '{number}' is not valid.  Please select a number 1-70"))
        user_lotto_numbers.append(number)
    return user_lotto_numbers


def get_lotto_numbers():
    """
    Generate list of random lottery numbers
    :return: List of integers
    """
    number_of_lotto_numbers = 3
    lotto_numbers = []
    for i in range(number_of_lotto_numbers):
        while True:
            if i == number_of_lotto_numbers - 1:
                lotto_numbers.append(randrange(1, 26))
                break
            else:
                new_number = randrange(1, 70)
                if new_number not in lotto_numbers:
                    lotto_numbers.append(new_number)
                    break
    return lotto_numbers


def lottery_game():
    """
    Starts the lottery game
    Prints amount of years it took to complete
    """
    user_numbers = get_numbers()
    number_of_drawings = 0
    while user_numbers != get_lotto_numbers():
        number_of_drawings += 1
    years = round(((number_of_drawings / 2) / 52), 2)
    print(f"Full match took {years} years")


if __name__ == '__main__':
    lottery_game()

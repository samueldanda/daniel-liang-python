import random
import sys


def main():
    play_game()


def play_game():
    seed = get_seed()
    number_of_misses = 0
    finished_game = False
    progres = '*' * len(seed)
    chars_remaining = len(seed)

    while not finished_game:
        character = prompt_guess_input(progres)[0]

        if character in progres:
            print("\t{} is already in the word".format(character))
        elif character in seed:
            progres = get_progres(seed, progres, character)
            chars_remaining = get_remaining_count(progres)
        else:
            number_of_misses += 1
            print("\t{} is not in the word".format(character))

        finished_game = True if chars_remaining == 0 else False

    print(
        "The word is {}. You missed {} {}".format(seed, number_of_misses, "times" if number_of_misses > 1 else "time"))

    choice = ''
    while choice != 'y' or choice != 'n':
        choice = prompt_play_again_choice()
        if choice == 'y':
            print("\n\n")
            play_game()
        elif choice == 'n':
            sys.exit()


def get_progres(seed, progres, character):
    progres_list = list(progres)
    for i in range(len(seed)):
        if seed[i] == character:
            progres_list[i] = character

    return ''.join(progres_list)


def get_remaining_count(progres):

    remaining_count = 0
    for i in range(len(progres)):
        if progres[i] == '*':
            remaining_count += 1

    return remaining_count


def prompt_play_again_choice():
    return input("\nDo you want to guess another word? Enter y or n > ")


def prompt_guess_input(progres):
    return input("(Guess) Enter a letter in word {} > ".format(progres))


def get_seed():
    words = [
        "apple", "banana", "carrot", "dog", "elephant", "flower", "guitar", "hat", "ice cream", "jacket",
        "kangaroo", "lion", "monkey", "notebook", "orange", "penguin", "queen", "rabbit", "snake", "tiger",
        "umbrella", "violin", "watermelon", "xylophone", "yacht", "zebra", "airplane", "ball", "cat", "dragon",
        "elephant", "fish", "grape", "horse", "igloo", "jellyfish", "kite", "lemon", "mango", "nest", "ocean",
        "piano", "quilt", "rose", "sun", "turtle", "umbrella", "volcano", "whale", "xylophone", "yogurt", "zeppelin"
    ]

    return words[random.randint(0, len(words) - 1)]


main()

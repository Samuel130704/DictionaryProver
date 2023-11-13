import numpy as np

import itertools

import json


def get_user_input():
    # read the letters which should be compared to the databank
    letters = list()
    inp = ""

    print("Type 'Stop' to finish")
    while inp.upper() != "STOP":
        inp = input("Type in a letter: ")
        if ((len(inp) < 2) and inp.isalpha()) or inp.upper() == "STOP":
            letters.append(inp)
        else:
            print("Invalid input")

    letters = throw_out_similar(letters)
    print(letters[:-1])

    # read which letters must be contained in the words the user gets
    print("Which letters must be contained?")
    required_letters = list()
    inp_required = ""

    while inp_required.upper() != "STOP":
        inp_required = input("Type in a letter: ")
        if ((len(inp_required) < 2) and inp_required.isalpha() and np.isin(inp_required, letters)) or inp_required.upper() == "STOP":
            required_letters.append(inp_required)
        else:
            print("Invalid input")

    required_letters = throw_out_similar(required_letters)
    print(required_letters[:-1])

    # get a boolean which tells you if letters can occur multiple times
    print("Can letters occur multiple times? Yes or No")
    multiple_occasion = True
    inp_occasion = True

    while inp_occasion:
        validation = input()
        if validation.upper() == "YES":
            inp_occasion = False
        elif validation.upper() == "NO":
            multiple_occasion = False
            inp_occasion = False
        else:
            print("Invalid input")

    print(multiple_occasion)

    # read the maximal amount of letters which the words, the users gets back, can have
    print("What is the maximal amount of letters?")

    cnt_max_letters = 0
    inp_cnt_max_letters = True
    while inp_cnt_max_letters:
        cnt_max_letters = input()
        if cnt_max_letters.isdigit():
            inp_cnt_max_letters = False
        else:
            print("Invalid input")

    print(cnt_max_letters)

    # same but with the minimal amount a word can have
    print("What is the minimal amount of letters?")

    cnt_min_letters = 0
    inp_cnt_min_letters = True
    while inp_cnt_min_letters:
        cnt_min_letters = input()
        if cnt_min_letters.isdigit():
            inp_cnt_min_letters = False
        else:
            print("Invalid input")

    print(cnt_min_letters)

    # store the above date in a list and return it for further process
    all_user_inputs = [letters[:-1], required_letters[:-1], multiple_occasion, cnt_max_letters, cnt_min_letters]
    print(all_user_inputs)

    return all_user_inputs


def get_all_combinations(user_inputs):
    max_letters = int(user_inputs[3])
    min_letters = int(user_inputs[4])
    letters = user_inputs[0]

    if not user_inputs[2]:

        # the for loop creates all permutations of the letters from the user inputs, the control variable times controls the amount of letters in the permutation
        all_permutations = list()

        for times in range(min_letters, max_letters + 1):
            all_permutations.extend(list(itertools.permutations(letters, r=times)))

        print(all_permutations)

        # sorting out the permutations which do not contain the required letters the user wanted
        required_letters = user_inputs[1]
        permutations_to_delete = list()

        for permutations in all_permutations:
            for letters in required_letters:
                cnt_permutations = permutations.count(letters)
                if cnt_permutations == 0:
                    permutations_to_delete.append(permutations)
                    break

        print(permutations_to_delete)

        for items in permutations_to_delete:
            for all_permutation in all_permutations:
                print(items)
                print("--")
                print(all_permutation)
                if items == all_permutation:
                    all_permutations.remove(all_permutation)
                    break

        print(all_permutations)
        return all_permutations
    elif user_inputs[2]:

        # creating all possibilities if a letter can occur multiple times
        all_possibilities = list()

        for items in range(min_letters, max_letters + 1):
            all_possibilities.extend(list(itertools.product(letters, repeat=items)))

        print(all_possibilities)

        # sorting out the permutations which do not contain the required letters the user wanted
        required_letters = user_inputs[1]
        possibilities_to_delete = list()

        for possibilities in all_possibilities:
            for letters in required_letters:
                cnt_possibilities = possibilities.count(letters)
                if cnt_possibilities == 0:
                    possibilities_to_delete.append(possibilities)
                    break

        print(possibilities_to_delete)

        for items in possibilities_to_delete:
            for all_possibility in all_possibilities:
                print(items)
                print("--")
                print(all_possibility)
                if items == all_possibility:
                    all_possibilities.remove(all_possibility)
                    break

        print(all_possibilities)
        return all_possibilities


def get_words_from_dictionary():
    with open("wordlist.json") as f:
        letters_dict = json.load(f)

    return letters_dict


def compare_dictionary_to_combinations(dictionary, possible_words):
    english_dictionary = dictionary
    list_of_words = possible_words
    altered_words_list = list()
    occurring_words = list()

    # configuring the list of words ,so it can actually compare words
    for tuples in list_of_words:
        summ = ""
        for elements in tuples:
            summ += elements
        altered_words_list.append(summ)

    # len(), del d[k], k in d, k not in d operations for
    for words in altered_words_list:
        if words in english_dictionary:
            occurring_words.append(words)

    print(occurring_words)
    return occurring_words


def display_possible_words(words_to_display):
    for words in words_to_display:
        print("One Possibility:" + " " + words)


def throw_out_similar(unsorted_list):
    seen_letters = set()
    sorted_letters = list()

    for letters in unsorted_list:
        if letters not in seen_letters:
            sorted_letters.append(letters)
            seen_letters.add(letters)

    return sorted_letters


if __name__ == '__main__':
    inputs_from_user = get_user_input()
    all_possible_words = get_all_combinations(inputs_from_user)
    letters_dictionary = get_words_from_dictionary()
    existing_words = compare_dictionary_to_combinations(letters_dictionary, all_possible_words)
    display_possible_words(existing_words)

import DictionaryCompare as dic
import UserInterface as user

if __name__ == '__main__':
    user_inputs = user.read_inputs()
    all_possible_words = dic.get_all_combinations(user_inputs)
    letters_dictionary = dic.get_words_from_dictionary()
    existing_words = dic.compare_dictionary_to_combinations(letters_dictionary, all_possible_words)
    dic.display_possible_words(existing_words)

    # for items in button.keys():
    #     print(items, ":", button[items])
    #

    # inputs_from_user = dic.get_user_input()
    # all_possible_words = dic.get_all_combinations(inputs_from_user)
    # letters_dictionary = dic.get_words_from_dictionary()
    # existing_words = dic.compare_dictionary_to_combinations(letters_dictionary, all_possible_words)
    # dic.display_possible_words(existing_words)

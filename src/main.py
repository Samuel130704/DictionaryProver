import tkinter as tk

import DictionaryCompare as dic

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Dictionary-Comparison")
    root.geometry("1000x500")
    root.minsize(width=400,height=300)

    label1 = tk.Label(root, text="Dictionary")
    label1.pack()
    root.mainloop()

    # inputs_from_user = dic.get_user_input()
    # all_possible_words = dic.get_all_combinations(inputs_from_user)
    # letters_dictionary = dic.get_words_from_dictionary()
    # existing_words = dic.compare_dictionary_to_combinations(letters_dictionary, all_possible_words)
    # dic.display_possible_words(existing_words)

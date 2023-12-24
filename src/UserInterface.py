import tkinter as tk
from tkinter import ttk
import DictionaryCompare as dic

root = tk.Tk()
root.title("Dictionary Prover")
root.geometry("1000x500")

letters = list()
new_letters = list()

req_letters = list()
all_user_inputs = list()


def save_letters():
    inp = let_inp.get()

    if len(inp) < 2 and inp.isalpha():
        letters.append(inp)
        let_lbl2.configure(text=inp)
        let_inp.delete(0, 'end')
    else:
        let_lbl2.configure(text="Invalid Input")
        let_inp.delete(0, 'end')

    new_letters = dic.throw_out_similar(letters)
    return new_letters


def save_req_letters():
    inp = req_let_inp.get()

    if len(inp) < 2 and inp.isalpha():
        req_letters.append(inp)
        req_let_lbl2.configure(text=inp)
        req_let_inp.delete(0, 'end')
    else:
        req_let_lbl2.configure(text="Invalid Input")
        req_let_inp.delete(0, 'end')

    new_req_letters = dic.throw_out_similar(req_letters)
    return new_req_letters


def get_scale_max():
    cur_value = int(max_let_scale.get())
    max_let_lbl2.configure(text=cur_value)
    return cur_value


def get_scale_min():
    cur_value = int(min_let_scale.get())
    min_let_lbl2.configure(text=cur_value)
    return cur_value


def sel():
    selection = bool(var.get())
    return selection


let_frm = ttk.Frame()
req_let_frm = ttk.Frame()
occ_frm = ttk.Frame()
max_let_frm = ttk.Frame()
min_let_frm = ttk.Frame()
fin_btn_frm = ttk.Frame()

let_lbl1 = ttk.Label(master=let_frm, text="Type the letters you want in your words")
let_lbl1.pack()
let_inp = ttk.Entry(master=let_frm)
let_inp.pack()
let_btn = ttk.Button(master=let_frm, text="Press to confirm the letters", command=save_letters)
let_btn.pack()
let_lbl2 = ttk.Label(master=let_frm)
let_lbl2.pack()

req_let_lbl1 = ttk.Label(master=req_let_frm, text="Type the letters that must be contained")
req_let_lbl1.pack()
req_let_inp = ttk.Entry(master=req_let_frm)
req_let_inp.pack()
req_let_btn = ttk.Button(master=req_let_frm, text="Press to confirm the letters", command=save_req_letters)
req_let_btn.pack()
req_let_lbl2 = ttk.Label(master=req_let_frm)
req_let_lbl2.pack()

var = tk.IntVar()
occ_lbl1 = ttk.Label(master=occ_frm, text="Can letters occur multiple times?")
occ_lbl1.pack()
occ_btn1 = ttk.Radiobutton(master=occ_frm, text="Yes", variable=var, value=True, command=sel)
occ_btn1.pack()
occ_btn2 = ttk.Radiobutton(master=occ_frm, text="No", variable=var, value=False, command=sel)
occ_btn2.pack()

max_let_lbl1 = ttk.Label(master=max_let_frm, text="Whats the maximum amount of letters")
max_let_lbl1.pack()
max_let_scale = ttk.Scale(master=max_let_frm, from_=0, to=20)
max_let_scale.pack()
max_let_lbl2 = ttk.Label(master=max_let_frm)
max_let_lbl2.pack()
max_let_btn = ttk.Button(master=max_let_frm, text="Show value", command=get_scale_max)
max_let_btn.pack()

min_let_lbl1 = ttk.Label(master=min_let_frm, text="Whats the minimum amount of letters")
min_let_lbl1.pack()
min_let_scale = ttk.Scale(master=min_let_frm, from_=0, to=20)
min_let_scale.pack()
min_let_lbl2 = ttk.Label(master=min_let_frm)
min_let_lbl2.pack()
min_let_btn = ttk.Button(master=min_let_frm, text="Show value", command=get_scale_min)
min_let_btn.pack()


def get_all_user_inputs():
    all_user_inputs.append(save_letters())
    all_user_inputs.append(save_req_letters())
    all_user_inputs.append(sel())
    all_user_inputs.append(get_scale_max())
    all_user_inputs.append(get_scale_min())
    print(all_user_inputs)
    all_possible_words = dic.get_all_combinations(all_user_inputs)
    letters_dictionary = dic.get_words_from_dictionary()
    existing_words = dic.compare_dictionary_to_combinations(letters_dictionary, all_possible_words)
    dic.display_possible_words(existing_words)

    for words in existing_words:
        fin_lbl1.insert('end', words)


fin_btn = ttk.Button(master=fin_btn_frm, text="Finish the input", command=get_all_user_inputs)
fin_btn.pack()
fin_lbl1 = tk.Listbox(master=fin_btn_frm)
fin_lbl1.pack()

let_frm.grid()
req_let_frm.grid()
occ_frm.grid()
max_let_frm.grid()
min_let_frm.grid()
fin_btn_frm.grid()


def read_inputs():
    root.mainloop()

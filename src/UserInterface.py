import tkinter as tk
from tkinter import ttk
import DictionaryCompare as dic

root = tk.Tk()
root.title("Dictionary Prover")
root.geometry("1000x500")

letters = list()
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


def get_letters():
    new_letters = dic.throw_out_similar(letters)
    let_lbl2.configure(text="")
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


def get_req_letters():
    new_req_letters = dic.throw_out_similar(req_letters)
    req_let_lbl2.configure(text="")
    return new_req_letters


def get_max_scale():
    cur_value = int(max_let_scale.get())
    max_let_lbl2.configure(text=cur_value)
    return cur_value


def get_min_scale():
    cur_value = int(min_let_scale.get())
    min_let_lbl2.configure(text=cur_value)
    return cur_value


def sel():
    selection = bool(var.get())
    return selection


let_frm = ttk.Frame(padding=15)
req_let_frm = ttk.Frame(padding=15)
occ_frm = ttk.Frame(padding=15)
max_let_frm = ttk.Frame(padding=15)
min_let_frm = ttk.Frame(padding=15)
fin_btn_frm = ttk.Frame(padding=15)

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
max_let_btn = ttk.Button(master=max_let_frm, text="Show value", command=get_max_scale)
max_let_btn.pack()

min_let_lbl1 = ttk.Label(master=min_let_frm, text="Whats the minimum amount of letters")
min_let_lbl1.pack()
min_let_scale = ttk.Scale(master=min_let_frm, from_=0, to=20)
min_let_scale.pack()
min_let_lbl2 = ttk.Label(master=min_let_frm)
min_let_lbl2.pack()
min_let_btn = ttk.Button(master=min_let_frm, text="Show value", command=get_min_scale)
min_let_btn.pack()


def get_all_user_inputs():
    all_user_inputs.append(get_letters())
    all_user_inputs.append(get_req_letters())
    all_user_inputs.append(sel())
    all_user_inputs.append(get_max_scale())
    all_user_inputs.append(get_min_scale())
    print(all_user_inputs)

    all_possible_words = dic.get_all_combinations(all_user_inputs)
    letters_dictionary = dic.get_words_from_dictionary()
    existing_words = dic.compare_dictionary_to_combinations(letters_dictionary, all_possible_words)

    for words in existing_words:
        fin_lbx.insert('end', words)


def delete_user_inputs():
    fin_lbx.delete(0, 'end')
    letters.clear()
    req_letters.clear()
    all_user_inputs.clear()


fin_btn = ttk.Button(master=fin_btn_frm, text="Finish the input", command=get_all_user_inputs)
fin_btn.pack()
fin_lbx = tk.Listbox(master=fin_btn_frm)
fin_lbx.pack()
fin_btn2 = ttk.Button(master=fin_btn_frm, text="Start again", command=delete_user_inputs)
fin_btn2.pack()

let_frm.grid(row=0, column=0)
req_let_frm.grid(row=0, column=1)
occ_frm.grid(row=0, column=2)
max_let_frm.grid(row=1, column=1)
min_let_frm.grid(row=1, column=2)
fin_btn_frm.grid(row=3, column=1)


def read_inputs():
    root.mainloop()

# for items in fin_lbx.keys():
#     print(items, ":", fin_lbx[items])

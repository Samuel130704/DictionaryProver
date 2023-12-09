import tkinter as tk
from tkinter import ttk
import DictionaryCompare as dic


def read_inputs():
    root = tk.Tk()
    root.geometry("1000x500")
    letters = list()

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
        print(new_letters)

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

    let_frm.pack()

    root.mainloop()

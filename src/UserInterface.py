import tkinter as tk
from tkinter import ttk
import DictionaryCompare as dic


def read_inputs():
    root = tk.Tk()
    root.geometry("1000x500")
    letters = list()

    def save_input():
        inp = input1.get()

        if len(inp) < 2 and inp.isalpha():
            letters.append(inp)
            label2.configure(text=inp)
            input1.delete(0, 'end')
        else:
            label2.configure(text="Invalid Input")
            input1.delete(0, 'end')

        new_letters = dic.throw_out_similar(letters)
        print(new_letters)

    def next_input():
        frame1.pack_forget()
        frame2.pack()

    frame1 = ttk.Frame()
    frame2 = ttk.Frame()

    label1 = ttk.Label(master=frame1, text="Type in a letter")
    label1.pack()
    label2 = ttk.Label(master=frame1)
    label2.pack()

    input1 = ttk.Entry(master=frame1)
    input1.pack()

    button1 = ttk.Button(master=frame1, text="Press to insert the letter", command=save_input)
    button1.pack()
    button2 = ttk.Button(master=frame2, text="Press to end the input", command=next_input)
    button2.pack()

    frame1.pack()
    frame2.pack()

    root.mainloop()

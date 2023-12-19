from tkinter import *
import tkinter as tk
import random
def dice():
    y = random.choice([1,2,3,4,5,6])
    return y

def open_win():
    if dice() >= 1:
        duplicate_win = tk.Toplevel(win)
        duplicate_win.title("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
        tk.Label(duplicate_win, text="HAHAHAHHAHAHAHA", font=('Candara 100')).pack(pady=20)
        duplicate_win.protocol("WM_DELETE_WINDOW", open_win)
        
    if dice() >= 2:
        duplicate_win = tk.Toplevel(win)
        duplicate_win.title("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
        tk.Label(duplicate_win, text="HAHAHAHHAHAHAHA", font=('Candara 100')).pack(pady=20)
        duplicate_win.protocol("WM_DELETE_WINDOW", open_win)

    if dice() >= 3:
        duplicate_win = tk.Toplevel(win)
        duplicate_win.title("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
        tk.Label(duplicate_win, text="HAHAHAHHAHAHAHA", font=('Candara 100')).pack(pady=20)
        duplicate_win.protocol("WM_DELETE_WINDOW", open_win)
    
    if dice() >= 4:
        duplicate_win = tk.Toplevel(win)
        duplicate_win.title("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
        tk.Label(duplicate_win, text="HAHAHAHHAHAHAHA", font=('Candara 100')).pack(pady=20)
        duplicate_win.protocol("WM_DELETE_WINDOW", open_win)
    
    if dice() >= 5:
        duplicate_win = tk.Toplevel(win)
        duplicate_win.title("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
        tk.Label(duplicate_win, text="HAHAHAHHAHAHAHA", font=('Candara 100')).pack(pady=20)
        duplicate_win.protocol("WM_DELETE_WINDOW", open_win)

    if dice() >= 6:
        duplicate_win = tk.Toplevel(win)
        duplicate_win.title("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
        tk.Label(duplicate_win, text="HAHAHAHHAHAHAHA", font=('Candara 100')).pack(pady=20)
        duplicate_win.protocol("WM_DELETE_WINDOW", open_win)

while True:
    win = tk.Tk()
    win.title("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
    label = tk.Label(win, text="HAHAHAHHAHAHAHA", font=('Candara 100')).pack(pady=20)
    win.protocol("WM_DELETE_WINDOW", open_win)
    win.mainloop()
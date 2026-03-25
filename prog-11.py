
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""
entry_text = tk.StringVar()

def press(num):
    global expression
    expression += str(num)
    entry_text.set(expression)
def equal():
    global expression
    try:
        result = str(eval(expression))
        entry_text.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        expression = ""
        entry_text.set("")
    except:
        messagebox.showerror("Error", "Invalid input")
        expression = ""
        entry_text.set("")

def clear():
    global expression
    expression = ""
    entry_text.set("")
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 18), justify="right")
entry.pack(fill="both", padx=10, pady=10)
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','C','=','+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            action = equal
        elif btn == "C":
            action = clear
        else:
            action = lambda x=btn: press(x)

        tk.Button(frame, text=btn, font=("Arial", 14),
                  command=action).pack(side="left", expand=True, fill="both")

root.mainloop()

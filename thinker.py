
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Base GUI")
root.geometry("300x200")
num1 = tk.Label(root,text="Enter a number")
num1.pack()
entry1 = tk.Entry(root)
entry1.pack()
num2 = tk.Label(root,text="Enter another number")
num2.pack()
entry2 = tk.Entry(root)
entry2.pack()
def fun():
    a = int(entry1.get())
    b = int(entry2.get())
    result = a+b
    result_label.config(text="Result : "+str(result))
button = tk.Button(root,text="ADD",command=fun)
button.pack()
result_label = tk.Label(root,text = "Result : ")
result_label.pack()
root.mainloop()

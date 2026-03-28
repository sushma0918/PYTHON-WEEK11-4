#24331A05G8
import tkinter as tk
root = tk.Tk()
var1 = tk.IntVar()
tk.Checkbutton(root, text="Option 1", variable=var1).pack()
var2 = tk.IntVar()
tk.Radiobutton(root, text="Male", variable=var2, value=1).pack()
tk.Radiobutton(root, text="Female", variable=var2, value=2).pack()
root.mainloop()
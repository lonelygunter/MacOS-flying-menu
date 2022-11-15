import tkinter as tk
from tkinter import ttk
import datetime as dt

# create a tkinter root window
root = tk.Tk()

# root window title, dimension, position and font
# root.title("*:༅｡:*ﾟ:*:༅｡༅:*ﾟ:*:✼✿  ← Control center →  ✿✼:*ﾟ:༅｡༅:*･ﾟﾟ･✼:*ﾟ:༅｡")
# root.geometry('500x300')
# root.geometry('+933+33')
fontLabel = ("Menlo Regular", 12)

# variables
current_time = dt.datetime.now().time()

# set a label
label = ttk.Label(root, text = "WiFi:")
label.grid(column = 2, row = 0)
label.configure(font = fontLabel)
label.place(relx = 0.5, rely = 0.5, anchor = 'center')
label.bind('<Configure>', lambda e: label.config(wraplength=label.winfo_width()))

# delete title bar and reposition window
root.overrideredirect(True)
root.bind('<B1-Motion>', lambda e: tk.event(e, Mode=True))
root.bind('<ButtonRelease-1>', lambda e: tk.standard_bind())
root.geometry('%dx%d+%d+%d' % (500, 200, 933, 33))

# close window after 1000 ms
root.after(1000,lambda:root.destroy())

# end
root.mainloop()
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas


window = Tk()

vm_button = Button(window, text="Verification Muster")
vm_button.grid(row=0, column=1)

mm_button = Button(window, text="Monitor Mass")
mm_button.grid(row=1, column=1)

cftpo_button = Button(window, text="CFTPO")
cftpo_button.grid(row=2, column=1)

help_button = Button(window, text="Help")
help_button.grid(row=6, column=0)

contact_button = Button(window, text="Contact")
contact_button.grid(row=6, column=2)

d = IntVar()
today = Radiobutton(text="Today", variable=d, value=0)
today.grid(row=3, column=1)
date_other = Radiobutton(text="Other", variable=d, value=1)
date_other.grid(row=4, column=0)

date = Entry(window)
date.grid(row=4, column=1)

continue_button = Button(window, text="Continue")
continue_button.grid(row=5, column=1)

window.mainloop()

def OpenFile():
    name = askopenfilename(filetypes=(("xlsx File", "*.xlsx"), ("All Files", "*.*")), title="Choose a file.")
    print(name)
    # Using try in case user types in unknown file or closes without choosing a file.
    try:
        print(pandas.read_excel(name))
    except:
        print("No file exists")


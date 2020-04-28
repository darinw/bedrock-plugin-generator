import tkinter as tk
import os

window = tk.Tk()
window.title("Bedrock Plugin Generator")
window.geometry('500x300')

# DO THIS CELLO!
# https://www.delftstack.com/howto/python-tkinter/how-to-set-window-icon-in-tkinter/


var1 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=40, textvariable=var1)
l.pack()

def print_selection():
    value = listbox.get(listbox.curselection())   
    var1.set(value)  


listbox = tk.Listbox(window, width=40)
listbox.pack()
listbox.insert(tk.END, "a list entry")

#  this will allow you to read the files within the behavoir pack.
#  it will be things like 'bedrock.json' or 'grass.json'
#  from there we will read the file, make a modification and save it into a '_generated_packs' folder 
for idx, fileName in enumerate(os.listdir("templateBehaviorPack")):
    listbox.insert(tk.END, fileName)


b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

window.mainloop()
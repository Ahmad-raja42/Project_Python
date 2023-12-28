# let's import the tkinter module
import tkinter

# let's use the tk() class of the tkinter module
root = tkinter.Tk()

# changing properties
root.title('Basic GUI')
root.geometry("600x480")
root.minsize(200 , 200)

# let's define value variable
value =0
#let's write a function for button 1
def increase_number():
    global value
    value = value + 1
    mylabel.config(text = value)
#let's write a function for button 2
def decrease_number():
    global value
    value = value - 1
    mylabel.config(text = value)
# let's add components/widgets
# let's add a label
mylabel = tkinter.Label(root, text=0, bg='green')
mylabel.pack(fill='x')
# let's add a button
button_1 = tkinter.Button(text='increase', command=increase_number)
button_1.pack()
# let's add another button
button_2 = tkinter.Button(text='decrease', command=decrease_number)
button_2.pack()
# adding the mainloop
root.mainloop()

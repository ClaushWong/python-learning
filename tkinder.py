import Tkinter

def println():
    x = inputBox.get()
    #Replace current label into new label
    label["text"] = x
    label.pack()

def bye():
    #Close the window
    window.destroy()

#create window
window = Tkinter.Tk()
window.title("MotherFucker")

#create a button
button1 = Tkinter.Button(window,text="Button1",command=println)
button1.pack()

button2 = Tkinter.Button(window,text="Button2",command=bye)
button2.pack()

#Create a line of text
label = Tkinter.Label(window,text="Press this button to be suprised.")
label.pack()

#Create an input box
inputBox = Tkinter.Entry(window)
inputBox.pack()

#Show the window
window.mainloop()


from Tkinter import *

window = Tk()
window.title("Tkinter Testing 1")

info = {}

def data():
    user_name = window1Entry.get()
    user_id = window2Entry.get()
    user_age = window3Entry.get()
    x = user_name
    y = user_id
    z = user_age
    info[x] = y + "," + z
    refresh()
    window1Entry.delete(0,"end")
    window2Entry.delete(0,"end")
    window3Entry.delete(0,"end")

def refresh():
    listbox1.delete(0,"end")
    for x in info:
        listbox1.insert("end",x)

def dataInfo():
    getInfoID = listbox1.get("active")
    getInfo = info[getInfoID]
    splitInfo = getInfo.split(",")
    y_ID = splitInfo[0]
    z_age = splitInfo[1]
    textNull1["text"] = "User ID : " + str(y_ID)
    textNull2["text"] = "User Age : " +  str(z_age)

textLine4 = Label(window,text="Welcome to SIS")
textLine4.pack()

listbox1 = Listbox(window)
listbox1.pack()

textLine1 = Label(window,text="Insert your name")
textLine1.pack()

window1Entry = Entry(window)
window1Entry.pack()

textLine2 = Label(window,text="Insert your ID")
textLine2.pack()

window2Entry = Entry(window)
window2Entry.pack()

textLine3 = Label(window,text="Insert your age")
textLine3.pack()

window3Entry = Entry(window)
window3Entry.pack()

textNull = Label(window,text="")
textNull.pack()

textNull1 = Label(window,text="")
textNull1.pack()

textNull2 = Label(window,text="")
textNull2.pack()

button1 = Button(window,text="Save Data",command=data)
button1.pack()

button2 = Button(window,text="RefreshData",command=refresh)
button2.pack()

button3 = Button(window,text="Data Info", command=dataInfo)
button3.pack()

window.mainloop()

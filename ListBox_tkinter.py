from tkinter import *

form =Tk()
form.geometry("700x500")

lbx =Listbox(form)
lbx.insert(0,"cairo")
lbx.insert(1,"giza")
lbx.insert(2,"london")


def f():
    print(lbx.get(ACTIVE))
lbx.pack()
Button(form ,text = "ok" ,command =f).pack()


form.mainloop()

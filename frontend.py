from tkinter import *
import backend

def get_selected_row(event) :
    global selected_Tuple
    index=list1.curselection() [0]
    selected_Tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_Tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_Tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_Tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_Tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
            
def search_command():   
    list1.delete(0,END)
    for row in backend.search(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()):
        list1.insert(END,row)

def Add_command():
    backend.insert(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()))

def delete_command():
    backend.delete(selected_Tuple[0])

def update_command():
    backend.UPDATE(selected_Tuple[0],title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
   
window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

Author_text = StringVar()
e2 = Entry(window, textvariable=Author_text)
e2.grid(row=0, column=3)

Year_text = StringVar()
e3 = Entry(window, textvariable=Year_text)
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>> ', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky="ns")  

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=Add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12,command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12,command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12,command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()

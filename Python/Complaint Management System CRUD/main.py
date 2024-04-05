from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
db = Database("complaints.db")

root = Tk() #userdefined class
root.title("Complaint Management System") #window title
root.geometry("1540x1080+0+0") #window size 1920x1080+xaxis+yaxis
root.state("zoomed") #Form maximized
root.config(bg="#2c3e50") #Form bg color

#Global Variables
name = StringVar()
division = StringVar()
date = StringVar()
email = StringVar()
complaint = StringVar()

# Entries Frame
entries_frame = Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title = Label(entries_frame,text="Complaint Management System",font=("Aries",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=4,padx=100,pady=20)

lblName = Label(entries_frame,text="Name",font=("Aries",14),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName = Entry(entries_frame,textvariable=name,font=("Aries",14),width=20)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblDiv = Label(entries_frame,text="Division",font=("Aries",14),bg="#535c68",fg="white")
lblDiv.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtDiv = Entry(entries_frame,textvariable=division,font=("Aries",14),width=20)
txtDiv.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lblDate = Label(entries_frame,text="Date",font=("Aries",14),bg="#535c68",fg="white")
lblDate.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtDate = Entry(entries_frame,textvariable=date,font=("Aries",14),width=20)
txtDate.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblEmail = Label(entries_frame,text="Email",font=("Aries",14),bg="#535c68",fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtEmail = Entry(entries_frame,textvariable=email,font=("Aries",14),width=20)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lblComp = Label(entries_frame,text="Complaint",font=("Aries",14),bg="#535c68",fg="white")
lblComp.grid(row=3,column=0,padx=10,pady=10,sticky="w")
txtComp = Text(entries_frame,font=("Aries",14),width=51,height=5)
txtComp.grid(row=3,column=1,columnspan=3,padx=10,pady=10,sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    division.set(row[2])
    date.set(row[3])
    email.set(row[4])
    txtComp.delete(1.0,END)
    txtComp.insert(END, row[5])
def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END,values=row)
def add_comp():
    if txtName.get() == "" or txtDiv.get() == "" or txtDate.get() == "" or txtEmail.get() == "" or txtComp.get(1.0, END) == "":
        messagebox.showerror("Error","Please Fill all Details")
        return
    db.insert(txtName.get(), txtDiv.get(), txtDate.get(), txtEmail.get(), txtComp.get(1.0,END))
    messagebox.showinfo("Success","Complaint Registered")
    clearAll()
    displayAll()
def update_comp():
    if txtName.get() == "" or txtDiv.get() == "" or txtDate.get() == "" or txtEmail.get() == "" or txtComp.get(1.0,
                                                                                                               END) == "":
        messagebox.showerror("Error", "Please Fill all Details")
        return
    db.update(row[0],txtName.get(), txtDiv.get(), txtDate.get(), txtEmail.get(), txtComp.get(1.0, END))
    messagebox.showinfo("Success", "Complaint Updated")
    clearAll()
    displayAll()

def delete_comp():
    db.remove(row[0])
    messagebox.showinfo("Success", "Complaint Deleted")
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    division.set("")
    date.set("")
    email.set("")
    txtComp.delete(1.0,END)

btn_frame = Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=4,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnAdd = (Button(btn_frame,command=add_comp,text="Submit", width=12, font=("Aries",15,"bold"),bg="#16a085",fg="white",bd=0)
          .grid(row=0,column=0,padx=10))

btnEdit = (Button(btn_frame,command=update_comp,text="Update", width=12, font=("Aries",15,"bold"),bg="#2980b9",fg="white",bd=0)
          .grid(row=0, column=1,padx=10))

btnDelete = (Button(btn_frame,command=delete_comp,text="Delete", width=12, font=("Aries",15,"bold"),bg="#c0392b",fg="white",bd=0)
          .grid(row=0, column=2,padx=10))

btnClear = (Button(btn_frame,command=clearAll,text="Clear", width=12, font=("Aries",15,"bold"),bg="#f39c12",fg="white",bd=0)
          .grid(row=0, column=3,padx=10))


# Table Frame
tree_frame = Frame(root, bg="white")
tree_frame.place(x=20, y=380, width =1500, height=400)
style = ttk.Style()

style.configure("mystyle.Treeview.Heading", font=('Aries', 16)) # Modify Heading style
style.configure("mystyle.Treeview", font=('Aries', 15),rowheight=50) #Modify Font of the body
tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6),style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=1)
tv.heading("2", text="Name")
tv.heading("3", text="Division")
tv.column("3", width=10)
tv.heading("4", text="Date")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Complaint")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayAll()
displayAll()
root.mainloop() #window reload until closed
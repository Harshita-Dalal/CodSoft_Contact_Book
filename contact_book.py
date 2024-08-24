
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg='#343a40')  # changed background color
root.title('PythonGeeks Contact Book')
root.resizable(0, 0)

contactlist = [
    ['Alice Brown', '1234567890', 'alice.brown@example.com'],
    ['Bob Smith', '0987654321', 'bob.smith@example.com'],
    ['Charlie Davis', '5551234567', 'charlie.davis@example.com'],
    ['David Lee', '7890123456', 'david.lee@example.com'],
    ['Eva Martin', '3456789012', 'eva.martin@example.com'],
    ['Frank Wilson', '9012345678', 'frank.wilson@example.com'],
    ['George Taylor', '2345678901', 'george.taylor@example.com'],
    ['Helen White', '5678901234', 'helen.white@example.com'],
    ['Ivan Jackson', '8901234567', 'ivan.jackson@example.com']
]

Name = StringVar()
Number = StringVar()
Email = StringVar()

frame = Frame(root, bg='#343a40')  # changed frame background color
frame.pack(side=RIGHT, fill=Y)

scroll = Scrollbar(frame, orient=VERTICAL, width=15)  # changed scrollbar width
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected():
    print("hello",len(select.curselection()))
    if len(select.curselection())==0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def EntryReset():
    Name.set("")
    Number.set("")
    Email.set("")


def AddContact():
    if Name.get() != "" and Number.get() != "" and Email.get() != "":
        contactlist.append([Name.get(), Number.get(), Email.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")

    else:
        messagebox.showerror("Error", "Please fill the information")


def UpdateDetail():
    if Name.get() and Number.get() and Email.get():
        contactlist[Selected()] = [Name.get(), Number.get(), Email.get()]

        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        EntryReset()
        Select_set()

    elif not (Name.get()) and not (Number.get()) and not (Email.get()) and not (len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill the information")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)


def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result == True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


def VIEW():
    NAME, PHONE, EMAIL = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Email.set(EMAIL)


def EXIT():
    root.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone, email in contactlist:
        select.insert(END, name)


Select_set()

Label(root, text='Name', font=("Times new roman", 22, "bold"), bg='#343a40', fg='white').place(x=30, y=20)  # changed label background and text color
Entry(root, textvariable=Name, width=30, bg='#f0f0f0', fg='black').place(x=200, y=30)  # changed entry background and text color
Label(root, text='Contact No.', font=("Times new roman", 20, "bold"), bg='#343a40', fg='white').place(x=30, y=70)


Entry(root, textvariable=Number, width=30, bg='#f0f0f0', fg='black').place(x=200, y=80)
Label(root, text='Email', font=("Times new roman", 20, "bold"), bg='#343a40', fg='white').place(x=30, y=120)
Entry(root, textvariable=Email, width=30, bg='#f0f0f0', fg='black').place(x=200, y=130)

Button(root, text=" ADD ➕", font='Helvetica 18 bold', bg='#34c759', fg='white', command=AddContact, padx=20).place(x=50, y=170)  # changed button background and text color
Button(root, text="EDIT ✂️", font='Helvetica 18 bold', bg='#34c759', fg='white', command=UpdateDetail, padx=20).place(x=50, y=230)
Button(root, text="DELETE 🗑️", font='Helvetica 18 bold', bg='#e74c3c', fg='white', command=Delete_Entry, padx=20).place(x=50, y=290)  # changed button background and text color
Button(root, text="VIEW 🔍", font='Helvetica 18 bold', bg='#34c759', fg='white', command=VIEW, padx=20).place(x=50, y=350)
Button(root, text="RESET ↩️", font='Helvetica 18 bold', bg='#34c759', fg='white', command=EntryReset, padx=20).place(x=50, y=410)
Button(root, text="EXIT ❌", font='Helvetica 24 bold', bg='tomato', fg='white', command=EXIT, padx=20).place(x=250, y=470)

root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
import pymysql
import mysql.connector
from tkinter import messagebox
from tkinter import ttk



def try_login():               # this my login function
    if name_entry.get()==default_name and password_entry.get() == default_password:
       messagebox.showinfo("LOGIN SUCCESSFULLY","WELCOME")
    else:
       messagebox.showwarning("login failed","Please try again" )


def cancel_login():        # exit function
    log.destroy()


default_name=("AI-DS")      #DEFAULT LOGIN ENTRY
default_password=("aids2025")


log=Tk()                   #this login ui
log.title("LOGIN window")
log.geometry("400x400")



LABEL_1 = Label(log,text="USER NAME")
LABEL_1.place(x=50,y=100)
LABEL_2 = Label(log,text="PASSWORD")
LABEL_2.place(x=50,y=150)

BUTTON_1=ttk. Button(text="login",command=try_login)
BUTTON_1.place(x=50,y=200)
BUTTON_1=ttk. Button(text="cancel",command=cancel_login)
BUTTON_1.place(x=200,y=200)

name_entry=Entry(log,width=30)
name_entry.place(x=150,y=100)
password_entry=ttk. Entry(log,width=30,show="*")
password_entry.place(x=150,y=150)

log. mainloop()

con = mysql.connector.connect(host="localhost", user="root", password="System#123", database="db")
# root is the username here
cur = con.cursor()  # cur -> cursor

root = Tk()
root.title("EMS")
root.minsize(width=400, height=400)
root.geometry("700x700")

same = True
n =1.5

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(190,240 , image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)


def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into " + bookTable + " values ('" + bid + "','" + title + "','" + author + "','" + status + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()

def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("E-book Management System")
    root.minsize(width=600, height=600)
    root.geometry("600x500")



    con = mysql.connector.connect(host="localhost", user="root", password="System#123", database="db")
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="lightpink1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Cambria', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(labelFrame, text="Status(Free/Pay) : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#ecddec', fg='red', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f1e3f7', fg='blue4', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def View():
    root = Tk()
    root.title("E-book Management System")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    bookTable="books"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="lightskyblue")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="magenta", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Book lists", bg='black', fg='white', font=('Cambria', 15))

    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('BID', 'Title', 'Author', 'Status'),
          bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " +bookTable


    cur= con.cursor()
    cur.execute(getBooks)
    #con.commit()

    for i in cur:
        Label(labelFrame, text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black',
                  fg='white').place(relx=0.07, rely=y)
        y += 0.05


    quitBtn = Button(root, text="Quit", bg='#f1e3f7', fg='blue4', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()



def deleteBook():
    bookTable="books"
    bid = bookInfo1.get()

    deleteSql = "delete from " + bookTable + " where bid = '" + bid + "'"

    try:
        cur.execute(deleteSql)
        con.commit()

        messagebox.showinfo('Success', "Book Record Deleted Successfully")

    except:
        messagebox.showinfo("Please check Book ID")

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()


def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("E-book Management System")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="plum3")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Cambria', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#ecddec', fg='red', command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f1e3f7', fg='blue4', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()



headingFrame1 = Frame(root, bg="violetred4", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n E-Book Management System", bg='black',
                                     fg='thistle1', font=('Comic Sans MS', 20))
headingLabel.place(relx=0, rely=0, relwidth=1,relheight=1)

btn1 = Button(root, text="Add Book Info", bg='black', fg='khaki1', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='khaki1', command=delete)
btn2.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='khaki1', command=View)
btn3.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

root.mainloop()

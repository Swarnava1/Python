from tkinter import *
import mysql.connector
class login:

    def __init__(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="tinderb1")
        self.mycursor=self.conn.cursor()

        self.root = Tk()

        self.root.title("Tinder Login")

        self.root.minsize(300, 300)
        self.root.maxsize(300, 300)

        Label(self.root, text='Enter Email').grid(row=0, column=0)
        self.emailInput = Entry(self.root)
        self.emailInput.grid(row=0, column=1)

        Label(self.root, text="Enter Password").grid(row=1, column=0)
        self.passwordInput = Entry(self.root)
        self.passwordInput.grid(row=1, column=1)

        Button(self.root, text='Login Here', command=lambda: self.validate()).grid(row=2, column=0)

        self.root.mainloop()

    def validate(self):
        emailInput=self.emailInput.get()
        passwordInput=self.passwordInput.get()
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(emailInput,passwordInput))

        user_info=self.mycursor.fetchall()
        if len(user_info)>0:
            print("Welcome")
        else:
            print("Incorrect")

obj=login()
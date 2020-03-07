import mysql.connector


class tinder:
    def __init__(self):

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="tinderb1")
        self.mycursor = self.conn.cursor()

        self.program_menu()

    def program_menu(self):

        program_input = input("""Hi! Welcome to Tinder
        1.Enter 1 to login
        2.Enter 2 to register
        3.Enter anything else to exit\n""")

        if program_input == "1":
            self.login()
        elif program_input == "2":
            self.register()
        else:
            print("Bye")


    def register(self):
        print("Welcome to the registration page")

        name = input("Enter name\n")
        email = input("Enter email\n")
        password = input("Enter password\n")
        age = int(input("Enter age\n"))
        gender = input("Enter gender\n")
        city = input("Enter city\n")

        self.mycursor.execute(
            """INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `age`, `gender`, `city`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                name, email, password, age, gender, city))

        self.conn.commit()

        print("Registration Successful")

    def login(self):

        email = input("Enter your email\n")
        password = input("Enter your password\n")

        self.mycursor.execute(
            """SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))

        user_list = self.mycursor.fetchall()

        # print(user_list)

        if len(user_list) > 0:
            print("Welcome")
            self.current_user_id = user_list[0][0]
            self.user_menu()


        else:
            print("Incorrect email/password")
            self.program_menu()

    def user_menu(self):

        user_input = input("""HI how would you like to proceed?
        1. View all users
        2. View who proposed you
        3. View your proposals
        4. View your matches
        5. Anything else to logout\n""")

        if user_input == "1":
            self.view_all_users()
        elif user_input == "2":
            self.view_proposed()
        elif user_input == "3":
            self.view_proposals()
        elif user_input == "4":
            self.view_matches()
        else:
            self.logout()

    def view_all_users(self):

        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))
        all_users = self.mycursor.fetchall()
        # print(all_users)

        for i in all_users:
            print(i[0], "|", i[1], "|", i[4], "|", i[5], "|", i[6])
            print("--------------------------------------------------------------")

        self.juliet_id=int(input("Enter the ID of the user you would like to propose\n"))
        self.propose(self.juliet_id)

    def propose(self,juliet_id):
        self.mycursor.execute("""INSERT INTO `proposals` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES (NULL, '{}', '{}')""".format(self.current_user_id,juliet_id))

        self.conn.commit()
        print("Proposal sent successful.Fingers Crossed!")

        self.user_menu()

    def view_proposed(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`romeo_id` WHERE p.`juliet_id`='{}'""".format(self.current_user_id))

        who_proposed=self.mycursor.fetchall()

        for i in who_proposed:
            print(i[4],"|",i[5],"|",i[7],"|",i[8],"|",i[9],"|")
            print("-------------------------------------------------------------")

        self.user_menu()

    def view_proposals(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE p.`romeo_id`='{}'""".format(self.current_user_id))
        who_proposed = self.mycursor.fetchall()
        for i in who_proposed:
            print(i[4], "|", i[5], "|", i[7], "|", i[8], "|", i[9], "|")
            print("---------------------------------------------")

        self.user_menu()

    def view_matches(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE p.`juliet_id` IN (SELECT `romeo_id` FROM `proposals` WHERE `juliet_id` LIKE '{}') AND p.`romeo_id` LIKE '{}'""".format(self.current_user_id,self.current_user_id))
        who_proposed = self.mycursor.fetchall()
        for i in who_proposed:
            print(i[4], "|", i[5], "|", i[7], "|", i[8], "|", i[9], "|")
            print("---------------------------------------------")

        self.user_menu()

    def logout(self):
        self.current_user_id=0
        print("Logged out!")
        self.program_menu()

obj1 = tinder()
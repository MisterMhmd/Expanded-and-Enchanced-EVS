import mysql.connector


db = mysql.connector.connect(host="localhost", user="root", password="1234",database="studentcouncil")
my_cursor = db.cursor()

def Officials():
    print("AdmiNo\tStuName\t Class\tPosition\tVotes")
    my_cursor.execute("SELECT * FROM HEADBOY")
    for i in my_cursor:
        print(i)
    my_cursor.execute("SELECT * FROM sportscaptain")
    for i in my_cursor:
        print(i)
    my_cursor.execute("SELECT * FROM culturalsecretary")
    for i in my_cursor:
        print(i)
    my_cursor.execute("SELECT * FROM studenteditor")
    for i in my_cursor:
        print(i)
    my_cursor.execute("SELECT * FROM sapphirehousecaptain")
    for i in my_cursor:
        print(i)
    my_cursor.execute("SELECT * FROM topazhousecaptain")
    for i in my_cursor:
        print(i)
    my_cursor.execute("SELECT * FROM amberhousecaptain")
    for i in my_cursor:
        print(i)
    my_cursor.execute("SELECT * FROM rubyhousecaptain")
    for i in my_cursor:
        print(i)


def Voting():
    def headboy():
        print("Choose your candidate!")
        print("1. Thomas  2. Andrew")
        head_boy = input("Choose your candidate: ")
        if head_boy.lower() == "thomas" or head_boy == "1":
            my_cursor.execute(f"UPDATE headboy set votes= votes + 1 where AdmiNo=8678")
            db.commit()
        elif head_boy.lower() == "andrew" or head_boy == "2":
            my_cursor.execute(f"UPDATE headboy set votes= votes + 1 where AdmiNo=6987")
            db.commit()
        else:
            print("You've inputted the wrong candidate name! try again")
    def sportscaptain():
        print("Choose your candidate!")
        print("1. taha  2. Joel  3.Charlie")
        captain = input("Choose your candidate: ")
        if captain.lower() == "taha" or captain == "1":
            my_cursor.execute(f"UPDATE sportscaptain set votes= votes + 1 where AdmiNo=9087")
            db.commit()
        elif captain.lower() == "joel" or captain == "2":
            my_cursor.execute(f"UPDATE sportscaptain set votes= votes + 1 where AdmiNo=8957")
            db.commit()
        elif captain.lower() == "charlie" or captain == "3":
            my_cursor.execute(f"UPDATE sportscaptain set votes= votes + 1 where AdmiNo=9857")
            db.commit()
        else:
            print("You've inputted the wrong candidate name! try again")

    def culturalsecretary():
        print("Choose your candidate!")
        print("1. Sharaheel  2. Zaid  3.Abdulrahman")
        cultural = input("Choose your candidate: ")
        if cultural.lower() == "sharaheel" or cultural == "1":
            my_cursor.execute(f"UPDATE culturalsecretary set votes= votes + 1 where AdmiNo=7395")
            db.commit()
        elif cultural.lower() == "zaid" or cultural == "2":
            my_cursor.execute(f"UPDATE culturalsecretary set votes= votes + 1 where AdmiNo=5869")
            db.commit()
        elif cultural.lower() == "abdulrahman" or cultural == "3":
            my_cursor.execute(f"UPDATE culturalsecretary set votes= votes + 1 where AdmiNo=9079")
            db.commit()
        else:
            print("You've inputted the wrong candidate name! try again")
    def studenteditor():
        print("Choose your candidate!")
        print("1. Khadija  2. Khalid  3.Mariam")
        editor = input("Choose your candidate: ")
        if editor.lower() == "khadija" or editor == "1":
            my_cursor.execute(f"UPDATE studenteditor set votes= votes + 1 where AdmiNo=9645")
            db.commit()
        elif editor.lower() == "khalid" or editor == "2":
            my_cursor.execute(f"UPDATE studenteditor set votes= votes + 1 where AdmiNo=9342")
            db.commit()
        elif editor.lower() == "mariam" or editor == "3":
            my_cursor.execute(f"UPDATE studenteditor set votes= votes + 1 where AdmiNo=9543")
            db.commit()
        else:
            print("You've inputted the wrong candidate name! try again")

    def Sapphire():
        print("Choose your candidate!")
        print("1. James  2. Michael  3.Sarah")
        sapphire = input("Choose your candidate: ")
        if sapphire.lower() == "james" or sapphire == "1":
            my_cursor.execute(f"UPDATE sapphirehousecaptain set votes= votes + 1 where AdmiNo=8364")
            db.commit()
        elif sapphire.lower() == "michael" or sapphire == "2":
            my_cursor.execute(f"UPDATE sapphirehousecaptain set votes= votes + 1 where AdmiNo=9231")
            db.commit()
        elif sapphire.lower() == "sarah" or sapphire == "3":
            my_cursor.execute(f"UPDATE sapphirehousecaptain set votes= votes + 1 where AdmiNo=5489")
            db.commit()
        else:
            print("You've inputted the wrong candidate name! try again")

    def Topaz():
        print("Choose your candidate!")
        print("1. mohammad  2. jordan  3.ali")
        topaz = input("Choose your candidate: ")
        if topaz.lower() == "mohammad" or topaz == "1":
            my_cursor.execute(f"UPDATE topazhousecaptain set votes= votes + 1 where AdmiNo=9400")
            db.commit()
        elif topaz.lower() == "jordan" or topaz == "2":
            my_cursor.execute(f"UPDATE topazhousecaptain set votes= votes + 1 where AdmiNo=9615")
            db.commit()
        elif topaz.lower() == "ali" or topaz == "3":
            my_cursor.execute(f"UPDATE topazhousecaptain set votes= votes + 1 where AdmiNo=9503")
            db.commit()
        else:
            print("You've inputted the wrong candidate name! try again")

    def Amber():
        print("Choose your candidate!")
        print("1. abdullah  2. dawood  3.peter")
        amber = input("Choose your candidate: ")
        if amber.lower() == "abdullah" or amber == "1":
            my_cursor.execute(f"UPDATE amberhousecaptain set votes= votes + 1 where AdmiNo=8470")
            db.commit()
        elif amber.lower() == "dawood" or amber == "2":
            my_cursor.execute(f"UPDATE amberhousecaptain set votes= votes + 1 where AdmiNo=9230")
            db.commit()
        elif amber.lower() == "peter" or amber == "3":
            my_cursor.execute(f"UPDATE amberhousecaptain set votes= votes + 1 where AdmiNo=9685")
            db.commit()
        else:
            print("You've inputted the wrong candidate name! try again")

    def Ruby():
        print("Choose your candidate!")
        print("1. joe  2. stewy  3.Ahmed")
        ruby = input("Choose your candidate: ")
        if ruby.lower() == "joe" or ruby == "1":
            my_cursor.execute(f"UPDATE rubyhousecaptain set votes= votes + 1 where AdmiNo=8219")
            db.commit()
        elif ruby.lower() == "stewy" or ruby == "2":
            my_cursor.execute(f"UPDATE rubyhousecaptain set votes= votes + 1 where AdmiNo=9034")
            db.commit()
        elif ruby.lower() == "ahmed" or ruby == "3":
            my_cursor.execute(f"UPDATE rubyhousecaptain set votes= votes + 1 where AdmiNo=8972")
            db.commit()
        else:
            print("You've inputted the wrong candidate name! try again")
    print("Welcome to our Electronic voting system! This is a demo and will be improved as time goes on!")
    print("Let's start")
    headboy()
    sportscaptain()
    culturalsecretary()
    studenteditor()
    house_Choice = input("Enter your house name: ")
    if house_Choice.lower() == "ruby":
        Ruby()
    elif house_Choice.lower() == "amber":
        Amber()
    elif house_Choice.lower() == "topaz":
        Topaz()
    elif house_Choice.lower() == "sapphire":
        Sapphire()


while True:
    access = input("Student or teacher?: ")
    if access.lower() == "student":
        Voting()
    elif access.lower() == "teacher":
            password = input("Enter the password: ")
            if password == "admin1234":
                Officials()
            else:
                print("Access denied")





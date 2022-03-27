import mysql.connector
import time

db = mysql.connector.connect(host="localhost", user="root", password="1234", database="studentcouncil")
my_cursor = db.cursor()


def database_creation():
    print("Creating a new database...")
    my_cursor.execute("CREATE DATABASE STUDENTCOUNCIL;")
    time.sleep(1)
    db.commit()
    print("Database Created successfully!")
    my_cursor.execute("USE STUDENTCOUNCIL;")
    db.commit()
    my_cursor.execute('''Create table headboy(
                      AdmiNo INT,
                      Name VARCHAR(30),
                      Class VARCHAR(5),
                      Position VARCHAR(50),
                      Votes INT
                      );''')
    db.commit()
    hbnum = int(input("How many headboy candidates are there?: "))
    for i in range(0, hbnum):
        admino = int(input("Write the candidate's admissions number: "))
        name = input("Candidate's name: ")
        grade = input("Candidate's class: ")
        position = "HeadBoy"
        votes = 0
        my_cursor.execute(f"INSERT INTO HEADBOY VALUES {(admino, name, grade, position, votes)}")
        db.commit()
    my_cursor.execute('''Create table sportscaptain(
                          AdmiNo INT,
                          Name VARCHAR(30),
                          Class VARCHAR(5),
                          Position VARCHAR(50),
                          Votes INT
                          );''')
    db.commit()
    scnum = int(input("How many sports captain candidates are there?: "))
    for i in range(0, scnum):
        admino = int(input("Write the candidate's admissions number: "))
        name = input("Write the candidate's Name: ")
        grade = input("Write the candidates class: ")
        position = "SportsCaptain"
        votes = 0
        my_cursor.execute(f"INSERT INTO sportscaptain VALUES {(admino, name, grade, position, votes)}")
        db.commit()
    my_cursor.execute('''Create table culturalsecretary(
                        AdmiNo INT,
                        Name VARCHAR(30),
                        Class VARCHAR(5),
                        Position VARCHAR(50),
                        Votes INT
                        );''')
    db.commit()
    cltsnum = int(input("How many Cultural Secretary candidates are there?: "))
    for i in range(0, cltsnum):
        admino = int(input("Write the candidate's admissions number: "))
        name = input("Write the candidate's Name: ")
        grade = input("Write the candidates class: ")
        position = "CulturalSecretary"
        votes = 0
        my_cursor.execute(f"INSERT INTO culturalsecretary VALUES {(admino, name, grade, position, votes)}")
        db.commit()
    my_cursor.execute('''Create table studenteditor(
                           AdmiNo INT,
                           Name VARCHAR(30),
                           Class VARCHAR(5),
                           Position VARCHAR(50),
                           Votes INT
                           );''')
    db.commit()
    senum = int(input("How many Student Editor candidates are there?: "))
    for i in range(0, senum):
        admino = int(input("Write the candidate's admissions number: "))
        name = input("Write the candidate's Name: ")
        grade = input("Write the candidates class: ")
        position = "StudentEditor"
        votes = 0
        my_cursor.execute(f"INSERT INTO StudentEditor VALUES {(admino, name, grade, position, votes)}")
        db.commit()
    my_cursor.execute('''Create table sapphirehousecaptain(
                           AdmiNo INT,
                           Name VARCHAR(30),
                           Class VARCHAR(5),
                           Position VARCHAR(50),
                           Votes INT
                           );''')
    db.commit()
    shcnum = int(input("How many sapphire house candidates are there?: "))
    for i in range(0, shcnum):
        admino = int(input("Write the candidate's admissions number: "))
        name = input("Write the candidate's Name: ")
        grade = input("Write the candidates class: ")
        position = "SapphireHouseCaptain"
        votes = 0
        my_cursor.execute(f"INSERT INTO sapphirehousecaptain VALUES {(admino, name, grade, position, votes)}")
        db.commit()
    my_cursor.execute('''Create table topazhousecaptain(
                           AdmiNo INT,
                           Name VARCHAR(30),
                           Class VARCHAR(5),
                           Position VARCHAR(50),
                           Votes INT
                           );''')
    db.commit()
    thcnum = int(input("How many Topaz House candidates are there?: "))
    for i in range(0, thcnum):
        admino = int(input("Write the candidate's admissions number: "))
        name = input("Write the candidate's Name: ")
        grade = input("Write the candidates class: ")
        position = "TopazHouseCaptain"
        votes = 0
        my_cursor.execute(f"INSERT INTO topazhousecaptain VALUES {(admino, name, grade, position, votes)}")
        db.commit()
    my_cursor.execute('''Create table amberhousecaptain(
                           AdmiNo INT,
                           Name VARCHAR(30),
                           Class VARCHAR(5),
                           Position VARCHAR(50),
                           Votes INT
                           );''')
    db.commit()
    ahcnum = int(input("How many Amber House candidates are there?: "))
    for i in range(0, ahcnum):
        admino = int(input("Write the candidate's admissions number: "))
        name = input("Write the candidate's Name: ")
        grade = input("Write the candidates class: ")
        position = "AmberHouseCaptain"
        votes = 0
        my_cursor.execute(f"INSERT INTO amberhousecaptain VALUES {(admino, name, grade, position, votes)}")
        db.commit()
    my_cursor.execute('''Create table rubyhousecaptain(
                           AdmiNo INT,
                           Name VARCHAR(30),
                           Class VARCHAR(5),
                           Position VARCHAR(50),
                           Votes INT
                           );''')
    db.commit()
    rhcnum = int(input("How many Ruby House candidates are there?: "))
    for i in range(0, rhcnum):
        admino = int(input("Write the candidate's admissions number: "))
        name = input("Write the candidate's Name: ")
        grade = input("Write the candidates class: ")
        position = "RubyHouseCaptain"
        votes = 0
        my_cursor.execute(f"INSERT INTO rubyhousecaptain VALUES {(admino, name, grade, position, votes)}")
        db.commit()
    print("Values have been successfully added to the studentcouncil database!")


def officials():
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


def voting():
    def headboy():
        my_cursor.execute("Select Name,AdmiNo from headboy;")
        names = my_cursor.fetchall()
        cannum = len(names)
        print("Candidates for the headboy Position are:")
        for i in range(0, cannum):
            print(f"{i+1}.{names[i][0]}", end=' ')
        head_boy = input("\n Pick your Candidate!: ")
        for i in range(0, cannum):
            if head_boy.lower() == f"{names[i][0].lower()}" or head_boy == str(i+1):
                my_cursor.execute(f"UPDATE headboy set votes= votes + 1 where AdmiNo={names[i][1]}")
                db.commit()
                break
        else:
            print("You've inputted the wrong candidate name! try again")

    def sportscaptain():
        my_cursor.execute("Select Name,AdmiNo from sportscaptain;")
        names = my_cursor.fetchall()
        cannum = len(names)
        print("Candidates for the Sports Captain Position are:")
        for i in range(0, cannum):
            print(f"{i + 1}.{names[i][0]}", end=' ')
        head_boy = input("\n Pick your Candidate!: ")
        for i in range(0, cannum):
            if head_boy.lower() == f"{names[i][0].lower()}" or head_boy == str(i + 1):
                my_cursor.execute(f"UPDATE SportsCaptain set votes= votes + 1 where AdmiNo={names[i][1]}")
                db.commit()
                break
        else:
            print("You've inputted the wrong candidate name! try again")

    def culturalsecretary():
        my_cursor.execute("Select Name,AdmiNo from culturalsecretary;")
        names = my_cursor.fetchall()
        cannum = len(names)
        print("Candidates for the Cultural Secretary position are: ")
        for i in range(0, cannum):
            print(f"{i + 1}.{names[i][0]}", end=' ')
        head_boy = input("\n Pick your Candidate!: ")
        for i in range(0, cannum):
            if head_boy.lower() == f"{names[i][0].lower()}" or head_boy == str(i + 1):
                my_cursor.execute(f"UPDATE culturalsecretary set votes= votes + 1 where AdmiNo={names[i][1]}")
                db.commit()
                break
        else:
            print("You've inputted the wrong candidate name! try again")

    def studenteditor():
        my_cursor.execute("Select Name,AdmiNo from studenteditor;")
        names = my_cursor.fetchall()
        print("Candidates for the Student Editor Position are:")
        cannum = len(names)
        for i in range(0, cannum):
            print(f"{i + 1}.{names[i][0]}", end=' ')
        head_boy = input("\n pick your Candidate!: ")
        for i in range(0, cannum):
            if head_boy.lower() == f"{names[i][0].lower()}" or head_boy == str(i + 1):
                my_cursor.execute(f"UPDATE studenteditor set votes= votes + 1 where AdmiNo={names[i][1]}")
                db.commit()
                break
        else:
            print("You've inputted the wrong candidate name! try again")

    def sapphire():
        my_cursor.execute("Select Name,AdmiNo from sapphirehousecaptain;")
        names = my_cursor.fetchall()
        cannum = len(names)
        print("Candidates for the Sapphire House Captain Position are:")
        for i in range(0, cannum):
            print(f"{i + 1}.{names[i][0]}", end=' ')
        head_boy = input("\n Choose your Candidate!: ")
        for i in range(0, cannum):
            if head_boy.lower() == f"{names[i][0].lower()}" or head_boy == str(i + 1):
                my_cursor.execute(f"UPDATE sapphirehousecaptain set votes= votes + 1 where AdmiNo={names[i][1]}")
                db.commit()
                break
        else:
            print("You've inputted the wrong candidate name! try again")

    def topaz():
        my_cursor.execute("Select Name,AdmiNo from topazhousecaptain;")
        names = my_cursor.fetchall()
        cannum = len(names)
        print("Candidates for the Topaz House Captain Position are:")
        for i in range(0, cannum):
            print(f"{i + 1}.{names[i][0]}", end=' ')
        head_boy = input("\n Pick your Candidate!: ")
        for i in range(0, cannum):
            if head_boy.lower() == f"{names[i][0].lower()}" or head_boy == str(i + 1):
                my_cursor.execute(f"UPDATE topazhousecaptain set votes= votes + 1 where AdmiNo={names[i][1]}")
                db.commit()
                break
        else:
            print("You've inputted the wrong candidate name! try again")

    def amber():
        my_cursor.execute("Select Name,AdmiNo from amberhousecaptain;")
        names = my_cursor.fetchall()
        cannum = len(names)
        print("Candidates for the Amber House Captain Position are:")
        for i in range(0, cannum):
            print(f"{i + 1}.{names[i][0]}", end=' ')
        head_boy = input("\n Pick your Candidate!: ")
        for i in range(0, cannum):
            if head_boy.lower() == f"{names[i][0].lower()}" or head_boy == str(i + 1):
                my_cursor.execute(f"UPDATE amberhousecaptain set votes= votes + 1 where AdmiNo={names[i][1]}")
                db.commit()
                break
        else:
            print("You've inputted the wrong candidate name! try again")

    def ruby():
        my_cursor.execute("Select Name,AdmiNo from rubyhousecaptain;")
        names = my_cursor.fetchall()
        cannum = len(names)
        print("Candidates for the Ruby House Captain Position are:")
        for i in range(0, cannum):
            print(f"{i + 1}.{names[i][0]}", end=' ')
        head_boy = input("\n Choose your Candidate!: ")
        for i in range(0, cannum):
            if head_boy.lower() == f"{names[i][0].lower()}" or head_boy == str(i + 1):
                my_cursor.execute(f"UPDATE rubyhousecaptain set votes= votes + 1 where AdmiNo={names[i][1]}")
                db.commit()
                break
        else:
            print("You've inputted the wrong candidate name! try again")
    print("#############################################################ELECTRONIC VOTING SYSTEM####################################################################")
    headboy()
    sportscaptain()
    culturalsecretary()
    studenteditor()
    house_choice = input("Enter your house name: ")
    if house_choice.lower() == "ruby":
        ruby()
    elif house_choice.lower() == "amber":
        amber()
    elif house_choice.lower() == "topaz":
        topaz()
    elif house_choice.lower() == "sapphire":
        sapphire()


def database_deletion():
    confirm = input("Are you sure you want to create a new table? This will erase the current database?(y/n): ")
    if confirm.lower() == "y":
        confirmation = input("Please confirm: ")
        if confirmation.lower() == "confirm":
            print("Deleting tables...")
            my_cursor.execute("DROP DATABASE STUDENTCOUNCIL;")
            db.commit()
            print("database deleted successfully!")
            time.sleep(2)
            database_creation()
        else:
            print("going back to the menu... user decided to abort")
    elif confirm.lower() == "n":
        print("aborting...")
    else:
        print("Unknown command! Please try again!")


while True:
    access = input("Student or teacher?: ")
    if access.lower() == "student":
        voting()
    elif access.lower() == "teacher":
        password = input("Enter the password: ")
        if password == "admin1234":
            choice = input("Would you like to create a new student candidate role or show the votes?(create/show): ")
            if choice.lower() == "show":
                officials()
            elif choice.lower() == "create":
                database_deletion()
    else:
        print("Access denied")

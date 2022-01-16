Headboy = {"Thomas": 0, "Andrew": 0}
SportsCaptain = {"Taha": 0, "Joel": 0, "Charlie": 0}
CulturalSecretary = {"Sharaheel": 0, "Zaid": 0, "Abdulrahman": 0}
StudentEditor = {"Khadija": 0, "Khalid": 0, "Mariam": 0}
SapphireCaptain = {"James": 0, "Michael": 0,"Sarah": 0}
TopazCaptain = {"Mohammad": 0, "Jordan": 0, "Ali": 0}
AmberCaptain = {"Abdullah": 0, "Dawood": 0, "Peter": 0}
RubyCaptain = {"Joe": 0, "Stewy": 0, "Ahmed": 0}


def Officials():
    with open("Votes.txt", "r") as file:
        read = file.read()
        print(read)

def insertvotes():
    space = "\n"
    file = open("Votes.txt", "w")
    file.write(str(Headboy))
    file.write(space)
    file.write(str(SportsCaptain))
    file.write(space)
    file.write(str(CulturalSecretary))
    file.write(space)
    file.write(str(StudentEditor))
    file.write(space)
    file.write(str(RubyCaptain))
    file.write(space)
    file.write(str(AmberCaptain))
    file.write(space)
    file.write(str(TopazCaptain))
    file.write(space)
    file.write(str(SapphireCaptain))
    file.close()

def Voting():
    def headboy():
        print("Choose your candidate!")
        print("1. Thomas  2. Andrew")
        head_boy = input("Choose your candidate: ")
        if head_boy.lower() == "thomas" or head_boy == "1":
            Headboy["Thomas"] += 1
        elif head_boy.lower() == "andrew" or head_boy == "2":
            Headboy["Andrew"] += 1
        elif head_boy.lower() == "sarah" or head_boy == "3":
            Headboy["Sarah"] += 1
        else:
            print("You've inputted the wrong candidate name! try again")
    def sportscaptain():
        print("Choose your candidate!")
        print("1. taha  2. Joel  3.Charlie")
        captain = input("Choose your candidate: ")
        if captain.lower() == "taha" or captain == "1":
            SportsCaptain["Taha"] += 1
        elif captain.lower() == "joel" or captain == "2":
            SportsCaptain["Joel"] += 1
        elif captain.lower() == "charlie" or captain == "3":
            SportsCaptain["Charlie"] += 1
        else:
            print("You've inputted the wrong candidate name! try again")

    def culturalsecretary():
        print("Choose your candidate!")
        print("1. Sharaheel  2. Zaid  3.Abdulrahman")
        cultural = input("Choose your candidate: ")
        if cultural.lower() == "sharaheel" or cultural == "1":
            CulturalSecretary["Sharaheel"] += 1
        elif cultural.lower() == "zaid" or cultural == "2":
            CulturalSecretary["Zaid"] += 1
        elif cultural.lower() == "abdulrahman" or cultural == "3":
            CulturalSecretary["Abdulrahman"] += 1
        else:
            print("You've inputted the wrong candidate name! try again")
    def studenteditor():
        print("Choose your candidate!")
        print("1. Khadija  2. Khalid  3.Mariam")
        editor = input("Choose your candidate: ")
        if editor.lower() == "khadija" or editor == "1":
            StudentEditor["Khadija"] += 1
        elif editor.lower() == "khalid" or editor == "2":
            StudentEditor["Khalid"] += 1
        elif editor.lower() == "mariam" or editor == "3":
            StudentEditor["Mariam"] += 1
        else:
            print("You've inputted the wrong candidate name! try again")

    def Sapphire():
        print("Choose your candidate!")
        print("1. James  2. Michael  3.Sarah")
        sapphire = input("Choose your candidate: ")
        if sapphire.lower() == "james" or sapphire == "1":
            SapphireCaptain["James"] += 1
        elif sapphire.lower() == "michael" or sapphire == "2":
            SapphireCaptain["Michael"] += 1
        elif sapphire.lower() == "sarah" or sapphire == "3":
            SapphireCaptain["Sarah"] += 1
        else:
            print("You've inputted the wrong candidate name! try again")

    def Topaz():
        print("Choose your candidate!")
        print("1. mohammad  2. jordan  3.ali")
        topaz = input("Choose your candidate: ")
        if topaz.lower() == "mohammad" or topaz == "1":
            TopazCaptain["Mohammad"] += 1
        elif topaz.lower() == "jordan" or topaz == "2":
            TopazCaptain["Jordan"] += 1
        elif topaz.lower() == "ali" or topaz == "3":
            TopazCaptain["Ali"] += 1
        else:
            print("You've inputted the wrong candidate name! try again")

    def Amber():
        print("Choose your candidate!")
        print("1. abdullah  2. dawood  3.peter")
        amber = input("Choose your candidate: ")
        if amber.lower() == "abdullah" or amber == "1":
            AmberCaptain["Abdullah"] += 1
        elif amber.lower() == "dawood" or amber == "2":
            AmberCaptain["Dawood"] += 1
        elif amber.lower() == "peter" or amber == "3":
            AmberCaptain["Peter"] += 1
        else:
            print("You've inputted the wrong candidate name! try again")

    def Ruby():
        print("Choose your candidate!")
        print("1. joe  2. stewy  3.Ahmed")
        ruby = input("Choose your candidate: ")
        if ruby.lower() == "joe" or ruby == "1":
            RubyCaptain["Joe"] += 1
        elif ruby.lower() == "stewy" or ruby == "2":
            RubyCaptain["Stewy"] += 1
        elif ruby.lower() == "ahmed" or ruby == "3":
            RubyCaptain["Ahmed"] += 1
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
    insertvotes()


while True:
    access = input("Student or teacher?: ")
    if access.lower() == "student":
        Voting()
    elif access.lower() == "teacher":
            password = input("Enter the password: ")
            if password == "Admin2020":
                Officials()
            else:
                print("Access denied")





""" HEALTH MANAGEMENT SYSTEM
3 clients : Harry, Rohan, Hammad
Total 6 files : 3 files - Exercise & 3 files - Food (2 files for each. so, total 6 files)
Write a fnc that when executed takes as input client name

Do you want to LOG or RETRIEVE :
1) Log
2) Retrieve

Of whom you want to LOG/RETRIEVE :
1) Harry
2) Rohan
3) Hammad

What do you want to LOG/RETRIEVE :
1) Exercise
2) Diet

Type which exercise you have done : Squats, Burpes, Crunches, seated shoulder press, cable crossover
Type which diet you have taken : Chhapati, Ladyfinger, Potato
Your input has been successfully recorded at GETTIME.
"""

def gettime():
    import datetime
    return datetime.datetime.now()


def log():

    def gotoharry():

        def gotoexercise():
            with open("HMS_F1_Harry_Exercise.txt", "a") as file1:
                value1 = input("\nType, Which exercise you have done : ")
                if value1.isprintable():   # WANT SOLUTION : need a better function or a logic which checks for alphabets and either check spaces or not to get TRUE.
                    file1.write(str([str(gettime())]) + " : " + value1 + "\n")
                    print("Your input has been successfully recorded at %s." %gettime())
                else:
                    print("\nWrong Input! Please, Enter valid input...", end="\n\n")
                    gotoexercise()

        def gotodiet():
            with open("HMS_F2_Harry_Diet.txt", "a") as file2:
                value2 = input("\nType, What diet you have taken : ")
                file2.write(str([str(gettime())]) + " : " + value2 + "\n")
                print("Your input has been successfully recorded at %s." % gettime())

        print("Hi! Harry")

        while True:
            inp4 = input("What do you want to LOG \n1) Exercise \n2) Diet \nEnter the number : ")

            if inp4 == "1":
                gotoexercise()
                break
            elif inp4 == "2":
                gotodiet()
                break
            else:
                print("\nWrong Input! Please, Enter valid input...", end="\n\n")
                continue

    def gotorohan():

        def gotoexercise():
            with open("HMS_F1_Rohan_Exercise.txt", "a") as file3:
                value3 = input("\nType, Which exercise you have done : ")
                file3.write(str([str(gettime())]) + " : " + value3 + "\n")
                print("Your input has been successfully recorded at %s." %gettime())

        def gotodiet():
            with open("HMS_F2_Rohan_Diet.txt", "a") as file4:
                value4 = input("\nType, What diet you have taken : ")
                file4.write(str([str(gettime())]) + " : " + value4 + "\n")
                print("Your input has been successfully recorded at %s." % gettime())

        print("Hi! Rohan")

        while True:
            inp4 = input("What do you want to LOG \n1) Exercise \n2) Diet \nEnter the number : ")

            if inp4 == "1":
                gotoexercise()
                break
            elif inp4 == "2":
                gotodiet()
                break
            else:
                print("\nWrong Input! Please, Enter valid input...", end="\n\n")
                continue

    def gotohammad():

        def gotoexercise():
            with open("HMS_F1_Hammad_Exercise.txt", "a") as file5:
                value5 = input("\nType, Which exercise you have done : ")
                file5.write(str([str(gettime())]) + " : " + value5 + "\n")
                print("Your input has been successfully recorded at %s." %gettime())

        def gotodiet():
            with open("HMS_F2_Hammad_Diet.txt", "a") as file6:
                value6 = input("\nType, What diet you have taken : ")
                file6.write(str([str(gettime())]) + " : " + value6 + "\n")
                print("Your input has been successfully recorded at %s." % gettime())

        print("Hi! Hammad")

        while True:
            inp4 = input("What do you want to LOG \n1) Exercise \n2) Diet \nEnter the number : ")

            if inp4 == "1":
                gotoexercise()
                break
            elif inp4 == "2":
                gotodiet()
                break
            else:
                print("\nWrong Input! Please, Enter valid input...", end="\n\n")
                continue

    while True:
        print("\nOf whom you want to LOG the value \n1) Harry \n2) Rohan \n3) Hammad")
        inp2 = input("Enter the number : ")
        print()

        if inp2 == "1":
            gotoharry()
            break
        elif inp2 == "2":
            gotorohan()
            break
        elif inp2 == "3":
            gotohammad()
            break
        else:
            print("Wrong Input! Please, Enter valid input...", end="\n\n")
            continue


def retrieve():

    def gotoharry():

        def gotoexercise():
            try:
                with open("HMS_F1_Harry_Exercise.txt", "r") as f:
                    print(f.read())
            except Exception as e:
                print("\nException occurs! \nReason : %s" %e)

        def gotodiet():
            try:
                with open("HMS_F2_Harry_Diet.txt", "r") as f:
                    print(f.read())
            except Exception as e:
                print("\nException occurs! \nReason : %s" %e)

        print("Hi! Harry")

        while True:
            inp5 = input("What do you want to RETRIEVE \n1) Exercise \n2) Diet \nEnter the number : ")
            print()

            if inp5 == "1":
                gotoexercise()
                break
            elif inp5 == "2":
                gotodiet()
                break
            else:
                print("\nWrong Input! Please, Enter valid input...")
                continue

    def gotorohan():

        def gotoexercise():
            try:
                with open("HMS_F1_Rohan_Exercise.txt", "r") as f:
                    print(f.read())
            except Exception as e:
                print("\nException occurs! \nReason : %s" % e)

        def gotodiet():
            try:
                with open("HMS_F2_Rohan_Diet.txt", "r") as f:
                    print(f.read())
            except Exception as e:
                print("\nException occurs! \nReason : %s" % e)

        print("Hi! Rohan")

        while True:
            inp5 = input("What do you want to RETRIEVE \n1) Exercise \n2) Diet \nEnter the number : ")
            print()

            if inp5 == "1":
                gotoexercise()
                break
            elif inp5 == "2":
                gotodiet()
                break
            else:
                print("\nWrong Input! Please, Enter valid input...", end="\n\n")
                continue

    def gotohammad():

        def gotoexercise():
            try:
                with open("HMS_F1_Hammad_Exercise.txt", "r") as f:
                    print(f.read())
            except Exception as e:
                print("\nException occurs! \nReason : %s" % e)

        def gotodiet():
            try:
                with open("HMS_F2_Hammad_Diet.txt", "r") as f:
                    print(f.read())
            except Exception as e:
                print("\nException occurs! \nReason : %s" % e)

        print("Hi! Hammad")

        while True:
            inp5 = input("What do you want to RETRIEVE \n1) Exercise \n2) Diet \nEnter the number : ")
            print()

            if inp5 == "1":
                gotoexercise()
                break
            elif inp5 == "2":
                gotodiet()
                break
            else:
                print("\nWrong Input! Please, Enter valid input...", end="\n\n")
                continue

    while True:
        print("\nOf whom you want to RETRIEVE the details\n1) Harry \n2) Rohan \n3) Hammad")
        inp3 = input("Enter the number : ")
        print()

        if inp3 == "1":
            gotoharry()
            break
        elif inp3 == "2":
            gotorohan()
            break
        elif inp3 == "3":
            gotohammad()
            break
        else:
            print("Wrong Input! Please, Enter valid input...", end="\n\n")
            continue

print("\nWELCOME TO OUR HEALTH MANAGEMENT SYSTEM\n")

while True:
    print("Do you want to LOG or RETRIEVE the data? \n1) Log \n2) Retrieve")
    inp1 = input("Enter the number : ")

    if inp1 == "1":
        log()
        break
    elif inp1 == "2":
        retrieve()
        break
    else:
        print("\nWrong Input! Please, Enter valid input...", end="\n\n")
        continue

while True:
    print("\nDo you want to LOG or RETRIEVE the data again? \n1) YES \n2) NO")
    inp = input("Enter the number : ")

    if inp == "1":
        while True:
            print("\nDo you want to LOG or RETRIEVE the data? \n1) Log \n2) Retrieve")
            inp1 = input("Enter the number : ")
            if inp1 == "1":
                log()
                break
            elif inp1 == "2":
                retrieve()
                break
            else:
                print("\nWrong Input! Please, Enter valid input...", end="\n\n")
                continue

    elif inp == "2":
        exit()
    else:
        print("\nWrong Input!", end="\n\n")
        exit()
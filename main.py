from passenger import Passenger
from aeroplane import Aeroplane

aeroplane_List = []

print("--------Welcome to the Aeroplane Management System--------")

while True:
    Choice = int(input("Press 1 to view Aeroplane list, Press 2 to add new aeroplane, Press 3 to add passenger to existing aeroplane, Press 4 to view passenger in an aeroplane\n"))

    if Choice == 1:
        if not aeroplane_List:
            print("There's no aeroplane in the system")
        else:
            for aeroplane in aeroplane_List:
                print(f"Aeroplane Number: {aeroplane.get_Aeroplane_Num()} \n")

    elif Choice == 2:

        aeroplane_Num = int(input("Please eneter the aeroplane number: "))
        print(aeroplane_Num)

        aeroplane_Variable_Name = "aeroplane" + str(aeroplane_Num)
        aeroplane_Variable_Name = Aeroplane(aeroplane_Num)

        aeroplane_List.append(aeroplane_Variable_Name)

    elif Choice == 3:

        for aeroplane in aeroplane_List:
            print(f"Aeroplane Num: {aeroplane.get_Aeroplane_Num()}")

        choose_Aeroplane = int(input("Choose which aeroplane number: "))
        
        name = str(input("Enter passenger's name: "))
        age = int(input("Enter passenger's age: "))
        seat_Number = int(input("Enter seat number: "))
        passenger_Class = str(input("Enter passenger's class: "))

        passenger_Name_Variable = "Passenger" + name

        passenger_Name_Variable = Passenger(seat_Number, passenger_Class, name, age)

        for aeroplane in aeroplane_List:
            if choose_Aeroplane == aeroplane.get_Aeroplane_Num():
                aeroplane.add_Passenger(passenger_Name_Variable)

    elif Choice == 4:
        for aeroplane in aeroplane_List:
            print(aeroplane.get_Aeroplane_Num())

        which_Aeroplane = int(input("Enter Aeroplane Number: "))

        for aeroplane in aeroplane_List:
            if which_Aeroplane == aeroplane.get_Aeroplane_Num():
                print(aeroplane)

    elif Choice == 0:
        print("Stop the service")
        break
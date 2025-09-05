from passenger import Passenger

class Aeroplane:
    
    def __init__(self, aeroplane_Num):
        self.__aeroplane_Num= aeroplane_Num
        self.__passenger = []


    def __str__(self):
        result = f"Aeroplane Number: {self.__aeroplane_Num} \n Passengers: \n"
        if not self.__passenger:
            result += "No Passenger"
        else:
            for p in self.__passenger:
                result += str(p) + "\n"

        return result

    def get_Aeroplane_Num(self):
        return self.__aeroplane_Num
    
    def set_Aeroplane_Num(self, new_Aeroplan_Num):
        self.__aeroplane_Num = new_Aeroplan_Num

    # add and remove passenger function
        
    def add_Passenger(self, passenger: Passenger):
        self.__passenger.append(passenger)

    def remove_Passenger(self, passenger: Passenger):
        for passenger in self.__passenger:
            self.__passenger.remove(passenger)
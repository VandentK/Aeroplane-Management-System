from human import Human

class Passenger(Human):
    def __init__(self, seat_Num, passenger_Class, name, age):
        super().__init__(name, age)
        self.__seat_Num = seat_Num #where they sit in the aeroplane
        self.__passenger_Class = passenger_Class #Business Class/Economic class

    #Playing around with the __str__ function
    def __str__(self):
        return f"Seat Number: {self.__seat_Num}, Passenger Class: {self.__passenger_Class}, Name: {self.get_Name()}, Age: {self.get_Age()}"
    
    #getter and setter for the seat number
    
    def get_Seat_Num(self):
        return self.__seat_Num

    def set_Seat_Num(self, new_Seat_Num):
        self.__seat_Num = new_Seat_Num

    
    #getter and setter for the passenger class

    def get_Passenger_Class(self):
        return self.__passenger_Class 
    
    def set_Passenger_Class(self, new_Passenger_Class):
        self.__passenger_Class = new_Passenger_Class

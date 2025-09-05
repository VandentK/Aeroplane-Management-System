class Human:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"

    #getter and setter for name
    
    def get_Name(self):
        return self.__name
    
    def set_Name(self, new_Name):
        self.__name = new_Name

    #getter and setter for age

    def get_Age(self):
        return self.__age
    
    def set_Age(self, new_Age):
        self.__age = new_Age
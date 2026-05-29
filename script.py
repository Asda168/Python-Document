# name = "Asda"
# age  = 21
# def main():
#     print(name.upper(), age)
#
# if __name__ == "__main__":
#     main()

class Dog:
    def __init__(self, name, color):
        self.name   = name
        self.color  = color



class Car:
    def model(self):
        return "Honda SUV"


def __main_dog__():
    dog = Dog("KIKI", "Gray")
    print(dog.name.title(), dog.color.title())

def __main_car__():
    car = Car()
    print(car.model().upper())

def __main__():
    __main_dog__(),
    __main_car__()

if __name__ == "__main__":
    __main__()





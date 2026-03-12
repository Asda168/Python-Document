class Microwave:
    # __init__ runs automatically when you create a new object
    # self refers to the specific object being created
    def __init__(self, brand: str, power: str) -> None:
        self.brand = brand #stores the value as an instance attribute
        self.power = power
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave {self.brand} is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave {self.brand} is now turned on.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave {self.brand} is now turned off.')
        else:
            print(f'Microwave {self.brand} is already turned off.')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds')
        else:
            print(f'A mystical force whispers: "Turn on your microwave first..."')

data: Microwave = Microwave('Iphone', 'AC')
print(data)
print(data.brand)
print(data.power)

msg: Microwave = Microwave('Honda', '125cc')
print(data.power, msg.power)

msg.turn_on()
msg.run(30)
msg.turn_off()
msg.run(10)
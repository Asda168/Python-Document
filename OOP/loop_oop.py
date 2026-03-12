class Star:
    def __init__(self, number: int = 5):
        self.number = number

    def _build_range(self, row: int) -> str:
        x = ' ' * (self.number - row)
        y = ' # ' * row
        return f'{x}{y}'

    def _generate_row(self) -> list:
        return [self._build_range(row) for row in range(1, self.number + 1)]  # return a list, not print a generator

    def display(self) -> None:
        for row in self._generate_row():
            print(row)

if __name__ == '__main__':
    Star(number=5).display()


#******************[ Return Vs Print ]******************#
 # print() outputs a value to the screen for humans to read.
 # The function itself returns None.

 # return sends a value back from a function to the caller
 # so it can be used in code.
class DiamondPattern:
    def __init__(self, size: int = 5):
        self.size = size

    def _build_row(self, row: int) -> str:
        spaces = ' ' * (self.size - row)
        stars = ' * ' * row
        return f"{spaces}{stars}"

    def generate(self) -> list[str]:
        return [self._build_row(row) for row in range(1, self.size + 1)]

    def display(self) -> None:
        for row in self.generate():
            print(row)


if __name__ == "__main__":
    DiamondPattern(size=5).display()
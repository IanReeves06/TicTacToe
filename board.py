class Board:
    SIZE = 3

    def __init__(self) -> None:
        self.fields = [
            [" " for _ in range(self.SIZE)]
            for _ in range(self.SIZE)
        ]

    def place(self, row: int, column: int, symbol: str) -> None:
        if self.fields[row][column] != " ":
            raise ValueError("Dieses Feld ist bereits belegt.")

        self.fields[row][column] = symbol

    def is_full(self) -> bool:
        return all(
            field != " "
            for row in self.fields
            for field in row
        )

    def has_winner(self, symbol: str) -> bool:
        rows = self.fields

        columns = [
            [self.fields[row][column] for row in range(self.SIZE)]
            for column in range(self.SIZE)
        ]

        diagonals = [
            [self.fields[index][index] for index in range(self.SIZE)],
            [
                self.fields[index][self.SIZE - 1 - index]
                for index in range(self.SIZE)
            ]
        ]

        return any(
            all(field == symbol for field in line)
            for line in rows + columns + diagonals
        )

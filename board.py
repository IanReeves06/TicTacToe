from typing import Optional

from stone import Stone


class Board:
    """Verwaltet das Spielfeld."""

    SIZE = 3

    def __init__(self) -> None:
        self._fields: list[list[Optional[Stone]]] = [
            [None for _ in range(self.SIZE)]
            for _ in range(self.SIZE)
        ]

    def place_stone(self, row: int, column: int, stone: Stone) -> None:
        """Legt einen Stein auf das Spielfeld."""

        if not self.is_valid_position(row, column):
            raise ValueError("Die Position liegt außerhalb des Spielfeldes.")

        if not self.is_field_empty(row, column):
            raise ValueError("Dieses Feld ist bereits belegt.")

        self._fields[row][column] = stone

    def get_field(self, row: int, column: int) -> Optional[Stone]:
        """Gibt den Inhalt eines Feldes zurück."""

        return self._fields[row][column]

    def is_field_empty(self, row: int, column: int) -> bool:
        """Prüft, ob ein Feld frei ist."""

        return self._fields[row][column] is None

    def is_valid_position(self, row: int, column: int) -> bool:
        """Prüft, ob eine Position auf dem Spielfeld liegt."""

        return 0 <= row < self.SIZE and 0 <= column < self.SIZE

    def is_full(self) -> bool:
        """Prüft, ob alle Felder belegt sind."""

        return all(
            field is not None
            for row in self._fields
            for field in row
        )

    def get_winner(self) -> Optional[Stone]:
        """Gibt den Gewinnerstein zurück."""

        for line in self._get_all_lines():
            first_stone = line[0]

            if first_stone is not None and all(
                stone == first_stone for stone in line
            ):
                return first_stone

        return None

    def _get_all_lines(self) -> list[list[Optional[Stone]]]:
        """Erstellt alle Reihen, Spalten und Diagonalen."""

        lines: list[list[Optional[Stone]]] = []

        lines.extend(self._fields)

        for column_index in range(self.SIZE):
            lines.append([
                self._fields[row_index][column_index]
                for row_index in range(self.SIZE)
            ])

        lines.append([
            self._fields[index][index]
            for index in range(self.SIZE)
        ])

        lines.append([
            self._fields[index][self.SIZE - 1 - index]
            for index in range(self.SIZE)
        ])

        return lines

from board import Board
from player import Player


class ConsolePrinter:
    """Übernimmt alle Ausgaben auf der Konsole."""

    def print_welcome(self) -> None:
        print("=" * 31)
        print("         TIC-TAC-TOE")
        print("=" * 31)
        print("Gib eine Reihe und eine Spalte ein.")
        print("Erlaubte Werte: 1 bis 3")
        print("Beispiel: 2 3")

    def print_board(self, board: Board) -> None:
        print()
        print("    1   2   3")
        print("  +---+---+---+")

        for row in range(Board.SIZE):
            symbols = []

            for column in range(Board.SIZE):
                stone = board.get_field(row, column)
                symbols.append(str(stone) if stone is not None else " ")

            print(f"{row + 1} | " + " | ".join(symbols) + " |")
            print("  +---+---+---+")

        print()

    def print_turn(self, player: Player) -> None:
        print(f"{player.name} ist am Zug und spielt mit {player.stone}.")

    def print_error(self, message: str) -> None:
        print(f"Fehler: {message}")

    def print_winner(self, player: Player) -> None:
        print(f"{player.name} hat mit {player.stone} gewonnen!")

    def print_draw(self) -> None:
        print("Das Spiel endet unentschieden.")

    def print_goodbye(self) -> None:
        print("Das Spiel ist beendet.")

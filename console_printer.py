from board import Board
from player import Player


class ConsolePrinter:
    def print_board(self, board: Board) -> None:
        print()
        print("    1   2   3")

        for index, row in enumerate(board.fields, start=1):
            print(f"{index}   " + " | ".join(row))

            if index < Board.SIZE:
                print("   ---+---+---")

        print()

    def print_turn(self, player: Player) -> None:
        print(f"{player.name} ist am Zug ({player.symbol}).")

    def print_error(self, message: str) -> None:
        print(f"Fehler: {message}")

    def print_winner(self, player: Player) -> None:
        print(f"{player.name} hat gewonnen!")

    def print_draw(self) -> None:
        print("Unentschieden.")

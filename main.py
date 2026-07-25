from board import Board
from console_printer import ConsolePrinter
from game import TicTacToeGame
from player import Player


def main() -> None:
    players = [
        Player("Spieler 1", "X"),
        Player("Spieler 2", "O")
    ]

    game = TicTacToeGame(
        Board(),
        players,
        ConsolePrinter()
    )

    game.start()


if __name__ == "__main__":
    main()

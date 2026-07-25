from board import Board
from console_printer import ConsolePrinter
from game import TicTacToeGame
from player import Player
from stone import Stone


def read_player_name(player_number: int) -> str:
    """Liest den Namen eines Spielers ein."""

    name = input(f"Name von Spieler {player_number}: ").strip()
    return name if name else f"Spieler {player_number}"


def main() -> None:
    player_one = Player(
        name=read_player_name(1),
        stone=Stone("X")
    )

    player_two = Player(
        name=read_player_name(2),
        stone=Stone("O")
    )

    game = TicTacToeGame(
        board=Board(),
        players=[player_one, player_two],
        printer=ConsolePrinter()
    )

    game.start()


if __name__ == "__main__":
    main()

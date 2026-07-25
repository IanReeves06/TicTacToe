from board import Board
from console_printer import ConsolePrinter
from player import Player
from stone import Stone


class TicTacToeGame:
    """Steuert den Spielablauf."""

    def __init__(
        self,
        board: Board,
        players: list[Player],
        printer: ConsolePrinter
    ) -> None:
        if len(players) != 2:
            raise ValueError("Tic-Tac-Toe benötigt genau zwei Spieler.")

        if players[0].stone == players[1].stone:
            raise ValueError(
                "Die Spieler benötigen unterschiedliche Spielsteine."
            )

        self._board = board
        self._players = players
        self._printer = printer
        self._current_player_index = 0

    def start(self) -> None:
        """Startet das Spiel."""

        self._printer.print_welcome()
        self._printer.print_board(self._board)

        while True:
            current_player = self._get_current_player()
            self._printer.print_turn(current_player)

            row, column = self._read_position()

            self._board.place_stone(
                row,
                column,
                current_player.stone
            )

            self._printer.print_board(self._board)

            winner_stone = self._board.get_winner()

            if winner_stone is not None:
                winner = self._find_player_by_stone(winner_stone)
                self._printer.print_winner(winner)
                break

            if self._board.is_full():
                self._printer.print_draw()
                break

            self._switch_player()

        self._printer.print_goodbye()

    def _read_position(self) -> tuple[int, int]:
        """Liest Reihe und Spalte von der Konsole ein."""

        while True:
            try:
                user_input = input("Reihe und Spalte: ").strip()
                parts = user_input.split()

                if len(parts) != 2:
                    raise ValueError(
                        "Bitte zwei Zahlen eingeben, zum Beispiel: 2 3"
                    )

                row = int(parts[0]) - 1
                column = int(parts[1]) - 1

                if not self._board.is_valid_position(row, column):
                    raise ValueError(
                        "Reihe und Spalte müssen zwischen 1 und 3 liegen."
                    )

                if not self._board.is_field_empty(row, column):
                    raise ValueError("Dieses Feld ist bereits belegt.")

                return row, column

            except ValueError as error:
                self._printer.print_error(str(error))

    def _get_current_player(self) -> Player:
        return self._players[self._current_player_index]

    def _switch_player(self) -> None:
        self._current_player_index = (
            self._current_player_index + 1
        ) % len(self._players)

    def _find_player_by_stone(self, stone: Stone) -> Player:
        for player in self._players:
            if player.stone == stone:
                return player

        raise RuntimeError(
            "Zum Gewinnerstein wurde kein Spieler gefunden."
        )

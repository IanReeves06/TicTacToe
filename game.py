from board import Board
from console_printer import ConsolePrinter
from player import Player


class TicTacToeGame:
    def __init__(
        self,
        board: Board,
        players: list[Player],
        printer: ConsolePrinter
    ) -> None:
        self.board = board
        self.players = players
        self.printer = printer
        self.current_player = 0

    def start(self) -> None:
        while True:
            player = self.players[self.current_player]

            self.printer.print_board(self.board)
            self.printer.print_turn(player)

            try:
                row, column = self.read_position()
                self.board.place(row, column, player.symbol)
            except ValueError as error:
                self.printer.print_error(str(error))
                continue

            if self.board.has_winner(player.symbol):
                self.printer.print_board(self.board)
                self.printer.print_winner(player)
                break

            if self.board.is_full():
                self.printer.print_board(self.board)
                self.printer.print_draw()
                break

            self.current_player = 1 - self.current_player

    def read_position(self) -> tuple[int, int]:
        values = input(
            "Reihe und Spalte, zum Beispiel 2 3: "
        ).split()

        if len(values) != 2:
            raise ValueError("Bitte genau zwei Zahlen eingeben.")

        row = int(values[0]) - 1
        column = int(values[1]) - 1

        if not 0 <= row < Board.SIZE or not 0 <= column < Board.SIZE:
            raise ValueError("Die Zahlen müssen zwischen 1 und 3 liegen.")

        return row, column

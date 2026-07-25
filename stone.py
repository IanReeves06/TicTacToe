from dataclasses import dataclass


@dataclass(frozen=True)
class Stone:
    """Repräsentiert einen Spielstein."""

    symbol: str

    def __post_init__(self) -> None:
        normalized_symbol = self.symbol.upper()

        if normalized_symbol not in ("X", "O"):
            raise ValueError("Ein Spielstein muss X oder O sein.")

        object.__setattr__(self, "symbol", normalized_symbol)

    def __str__(self) -> str:
        return self.symbol

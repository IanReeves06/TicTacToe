from dataclasses import dataclass

from stone import Stone


@dataclass
class Player:
    """Repräsentiert einen Spieler."""

    name: str
    stone: Stone

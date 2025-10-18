from __future__ import annotations


class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive

    def __repr__(self) -> str:
        return f"Deck({self.row}, {self.column})"


class Ship:
    def __init__(self, start: tuple[int, int],
                 end: tuple[int, int],
                 is_drowned: bool = False
                 ) -> None:

        self.is_drowned = is_drowned
        self.decks = []

        x_coord_first, y_coord_first = start
        x_coord_second, y_coord_second = end
        if x_coord_first == x_coord_second and y_coord_first == y_coord_second:
            self.decks.append(Deck(x_coord_first, y_coord_first))

        elif y_coord_second > y_coord_first:
            for i in range(y_coord_first, y_coord_second + 1):
                self.decks.append(Deck(x_coord_first, i))

        elif x_coord_second > x_coord_first:
            for i in range(x_coord_first, x_coord_second + 1):
                self.decks.append(Deck(i, y_coord_first))

    def __repr__(self) -> str:
        return f"List Decks: ({self.decks}), Is_drowned: ({self.is_drowned}))"

    def get_deck(self, row: int, column: int) -> Deck | None:
        # Find object ship in list ships (decks)
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck
        return None

    def fire(self, row: int, column: int) -> None:
        deck = self.get_deck(row, column)
        if deck:
            deck.is_alive = False

            if all(not deck.is_alive for deck in self.decks):
                self.is_drowned = True


class Battleship:
    def __init__(self,
                 ships: list[tuple[tuple[int, int], tuple[int, int]]]) -> None:

        self.field = {}
        for start, end in ships:
            ship_object = Ship(start, end)
            for deck in ship_object.decks:
                self.field[(deck.row, deck.column)] = ship_object

    def fire(self, location: tuple) -> str:
        if location not in self.field:
            return "Miss!"
        else:
            ship_object = self.field[location]
            ship_object.fire(*location)
            if ship_object.is_drowned is True:
                return "Sunk!"
            else:
                return "Hit!"

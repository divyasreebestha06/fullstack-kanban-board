from dataclasses import dataclass
from typing import List, Dict

@dataclass
class KanbanCard:
    id: int
    title: str
    column: str # "TODO", "IN_PROGRESS", "DONE"

class KanbanBoard:
    COLUMNS = ["TODO", "IN_PROGRESS", "DONE"]

    def __init__(self):
        self.cards: Dict[int, KanbanCard] = {}
        self.counter = 1

    def add_card(self, title: str, column: str = "TODO") -> KanbanCard:
        if column not in self.COLUMNS:
            raise ValueError(f"Invalid column: {column}")
        card = KanbanCard(self.counter, title, column)
        self.cards[self.counter] = card
        self.counter += 1
        return card

    def move_card(self, card_id: int, target_column: str) -> bool:
        if target_column not in self.COLUMNS or card_id not in self.cards:
            return False
        self.cards[card_id].column = target_column
        return True

    def get_board(self) -> Dict[str, List[dict]]:
        board = {col: [] for col in self.COLUMNS}
        for c in self.cards.values():
            board[c.column].append(c.__dict__)
        return board

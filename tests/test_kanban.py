import unittest
from backend.models import KanbanBoard

class TestKanban(unittest.TestCase):
    def test_board_lifecycle(self):
        b = KanbanBoard()
        card = b.add_card("Write Documentation", "TODO")
        self.assertEqual(card.column, "TODO")
        moved = b.move_card(card.id, "IN_PROGRESS")
        self.assertTrue(moved)
        self.assertEqual(b.cards[card.id].column, "IN_PROGRESS")
        invalid = b.move_card(card.id, "INVALID_COL")
        self.assertFalse(invalid)

if __name__ == "__main__":
    unittest.main()

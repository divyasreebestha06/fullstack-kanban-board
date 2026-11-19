from backend.models import KanbanBoard

board = KanbanBoard()

def handle_get_board():
    return board.get_board(), 200

def handle_create_card(data: dict):
    title = data.get("title")
    if not title:
        return {"error": "Title required"}, 400
    card = board.add_card(title, data.get("column", "TODO"))
    return card.__dict__, 201

def handle_move_card(card_id: int, data: dict):
    target = data.get("column")
    if not board.move_card(card_id, target):
        return {"error": "Invalid move"}, 400
    return {"message": "Card moved successfully"}, 200

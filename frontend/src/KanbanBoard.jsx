import React, { useState } from 'react';

export default function KanbanBoard() {
  const [board, setBoard] = useState({
    TODO: [{ id: 1, title: 'Design Database Schema' }],
    IN_PROGRESS: [{ id: 2, title: 'Implement Auth API' }],
    DONE: [{ id: 3, title: 'Setup GitHub Repo' }]
  });

  return (
    <div className="kanban-container">
      <h2>Agile Sprint Board</h2>
      <div className="columns">
        {Object.entries(board).map(([col, cards]) => (
          <div key={col} className="column">
            <h3>{col}</h3>
            {cards.map(card => <div key={card.id} className="card">{card.title}</div>)}
          </div>
        ))}
      </div>
    </div>
  );
}

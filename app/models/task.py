from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional


@dataclass
class Task:
    id: str
    title: str
    due_date: Optional[date] = None
    created_at: datetime = field(default_factory=datetime.now)
    status: str = "pending"

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        due_date = data.get("due_date")
        if due_date:
            due_date = date.fromisoformat(due_date)
        return cls(
            id=data["id"],
            title=data["title"],
            due_date=due_date,
            created_at=datetime.fromisoformat(data["created_at"]),
            status=data.get("status", "pending"),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "created_at": self.created_at.isoformat(),
            "status": self.status,
        }

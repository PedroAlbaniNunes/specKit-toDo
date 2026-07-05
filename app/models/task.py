from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    id: str
    title: str
    reminder_at: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)
    status: str = "pending"

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        reminder_at = data.get("reminder_at")
        if reminder_at:
            reminder_at = datetime.fromisoformat(reminder_at)
        return cls(
            id=data["id"],
            title=data["title"],
            reminder_at=reminder_at,
            created_at=datetime.fromisoformat(data["created_at"]),
            status=data.get("status", "pending"),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "reminder_at": self.reminder_at.isoformat() if self.reminder_at else None,
            "created_at": self.created_at.isoformat(),
            "status": self.status,
        }

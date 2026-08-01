from dataclasses import asdict, dataclass, field
from datetime import datetime


@dataclass
class Transaction:
    amount: float
    transaction_type: str
    category: str
    description: str = ""
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data["amount"],
            transaction_type=data["transaction_type"],
            category=data.get("category", "other"),
            description=data.get("description", ""),
            created_at=data.get(
                "created_at",
                datetime.now().isoformat(timespec="seconds"),
            ),
        )

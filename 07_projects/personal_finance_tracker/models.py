from dataclasses import asdict, dataclass


@dataclass
class Transaction:
    amount: float
    transaction_type: str
    category: str
    description: str = ""

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data["amount"],
            transaction_type=data["transaction_type"],
            category=data.get("category", "other"),
            description=data.get("description", ""),
        )

from dataclasses import asdict, dataclass


@dataclass
class Transaction:
    amount: float
    transaction_type: str
    category: str
    description: str = ""

    def to_dict(self):
        return asdict(self)

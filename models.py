from dataclasses import dataclass, asdict

@dataclass
class Task:
    id: int
    description: str
    completed: bool = False

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

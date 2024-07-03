from dataclasses import dataclass

@dataclass
class Team:
    ID: int
    year: int
    teamCode: str
    name: str

    def __hash__(self):
        return hash(self.ID)





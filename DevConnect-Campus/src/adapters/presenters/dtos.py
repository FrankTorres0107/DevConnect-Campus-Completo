from dataclasses import dataclass

@dataclass
class ApplyRequestDTO:
    student_id: str
    vacancy_id: str

@dataclass
class AcceptRequestDTO:
    leader_id: str

@dataclass
class PublishProjectRequestDTO:
    leader_id: str
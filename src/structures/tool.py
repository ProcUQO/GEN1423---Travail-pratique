from dataclasses import dataclass

class Tool:
    assemblyType: str
    pressList: list
    canBeInterlock: bool
    description: str
    displayCode: str
    customerCode: str
    totalStack: float
    copyNumber: int

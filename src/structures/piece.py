from dataclasses import dataclass

class Piece:
    copyNumber: int
    location: str
    status: str
    type_: str # type is a reserved keyword
    diameter: float
    height: float
    nitrogen: bool
    surfaceNitrogen: bool
    toBeManufactured: bool
    customerCode: str
from dataclasses import dataclass

class Profile:
    customerCodePrefix: str
    customerCode: str
    description : str
    creationDate : str
    alloy : str
    mandrelQuantity : int
    cavityQuantity : int
    interlock : bool
    zsc : float
    doubleLayoutAngle : float
    hasElectrode : bool
    hasMicrofinish	: bool

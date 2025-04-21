from dataclasses import dataclass

class Requisition:
    requisitionStatus : str
    description : str
    receptionDate : str
    customerPurchaseNumber : str
    contact : str
    toolNumber : str
    cavityQuantity : int
    doubleLayout : bool

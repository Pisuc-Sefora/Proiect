from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Tranzactie(Entitate):
    idMasina: str
    idCardClient: str
    sumaPiese: float
    sumaManopera: float
    data: str
    ora: str
    reducere: int

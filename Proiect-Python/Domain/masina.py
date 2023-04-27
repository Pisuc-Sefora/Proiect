from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Masina(Entitate):
    '''
    descrie o masina
    '''
    model: str
    an: str
    nrKm: str
    inGarantie: str
    
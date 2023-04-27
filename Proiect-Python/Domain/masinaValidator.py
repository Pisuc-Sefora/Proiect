from Domain.masina import Masina


class MasinaValidator:
    def valideaza(self, masina: Masina):
        erori = []
        if int(masina.nrKm) < 0:
            erori.append("Nr. de km trebuie sa fie stricti pozitivi")
        if int(masina.an) < 0:
            erori.append("Anul achizitiei trebuie sa fie strict pozitiv")
        if len(erori) > 0:
            raise ValueError(erori)

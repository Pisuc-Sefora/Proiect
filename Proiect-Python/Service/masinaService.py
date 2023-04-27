from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.masina import Masina
from Domain.masinaValidator import MasinaValidator
from Domain.modifyOperation import ModifyOperation
from Repository.repository import Repository
import random
from Service.undoRedoService import UndoRedoService


class MasinaService:
    def __init__(self,
                 masinaRepository: Repository,
                 masinaValidator: MasinaValidator,
                 undoRedoService: UndoRedoService):
        self.__masinaRepository = masinaRepository
        self.__masinaValidator = masinaValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__masinaRepository.read()

    def adauga(self, idMasina, model, anAchizitie, nrKm, inGarantie):
        masina = Masina(idMasina, model, anAchizitie, nrKm, inGarantie)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.adauga(masina)
        self.__undoRedoService.addUndoOperation(
            AddOperation(self.__masinaRepository, masina))

    def sterge(self, idMasina):
        masina = self.__masinaRepository.read(idMasina)
        self.__masinaRepository.sterge(idMasina)
        self.__undoRedoService.addUndoOperation(
            DeleteOperation(self.__masinaRepository, masina))

    def modifica(self, idMasina, model, anAchizitie, nrKm, inGarantie):
        masinaVeche = self.__masinaRepository.read(idMasina)
        masina = Masina(idMasina, model, anAchizitie, nrKm, inGarantie)
        self.__masinaRepository.modifica(masina)
        self.__undoRedoService.addUndoOperation(
            ModifyOperation(self.__masinaRepository, masinaVeche, masina))

    def searchFullTextMasina(self, text):
        lst = []
        for i in self.__masinaRepository.read():
            if text in i.idEntitate:
                lst.append(i)
            elif text in i.model:
                lst.append(i)
            elif text in i.an:
                lst.append(i)
            elif text in i.nrKm:
                lst.append(i)
            elif text in i.inGarantie:
                lst.append(i)
        return lst

    def actualizareGarantie(self):
        list(filter(lambda i: self.modifica(
            i.idEntitate, i.model, i.an, i.nrKm, "Da")
        if 2021 - int(i.an) <= 3 and int(i.nrKm) <= 60000
        else self.modifica(i.idEntitate, i.model, i.an, i.nrKm, "Nu"),
                    self.__masinaRepository.read()))

    def getMasinaById(self, idMasina):
        return self.__masinaRepository.read(idMasina)

    def generareMasini(self, n):
        modele = ["audi a4", "mercedes", "tesla", "nissan", "bw",
                  "renault megane", "renault scenic", "impreza sedan",
                  "crosstrec", "alfa romeo", "toyota", "volvo"]
        for i in range(n):
            model = random.choice(modele)
            an = random.randint(2000, 2021)
            nrKm = random.randint(0, 620000)
            if random.randint(1, 10) % 2:
                inGarantie = "Da"
            else:
                inGarantie = "Nu"
            n = random.randint(1, 10000)
            while True == True:
                ok = True
                for x in self.__masinaRepository.read():
                    if x.idEntitate == n:
                        ok = False
                        break
                if ok == True:
                    break
                else:
                    n = random.randint(1, 10000)
            idMasina = n
            self.adauga(str(idMasina), str(model), str(an), str(nrKm),
                        inGarantie)

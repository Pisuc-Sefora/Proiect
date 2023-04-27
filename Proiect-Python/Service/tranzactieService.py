from Domain.deleteOperation import DeleteOperation
from Domain.tranzactie import Tranzactie
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class TranzactieService:
    def __init__(self,
                 tranzactieRepository: Repository,
                 masinaRepository: Repository,
                 cardClientRepository: Repository):
        self.__tranzactieRepository = tranzactieRepository
        self.__masinaRepository = masinaRepository
        self.__cardClientRepository = cardClientRepository


    def getAll(self):
        return self.__tranzactieRepository.read()

    def adauga(self,
               idTranzactie,
               idMasina,
               idCardClient,
               sumaPiese,
               sumaManopera,
               data,
               ora):
        if self.__masinaRepository.read(idMasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        if self.__cardClientRepository.read(idCardClient) is None:
            raise KeyError("Nu exista niciun card client cu id-ul dat!")
        reducere = 0
        if idCardClient != "":
            reducere = 10
        masina = self.__masinaRepository.read(idMasina)
        if masina.inGarantie == "Da":
            sumaPiese = 0

        tranzactie = Tranzactie(
            idTranzactie,
            idMasina,
            idCardClient,
            sumaPiese,
            sumaManopera,
            data,
            ora,
            reducere
        )
        self.__tranzactieRepository.adauga(tranzactie)

    def sterge(self, idTranzactie):
        self.__tranzactieRepository.sterge(idTranzactie)

    def modifica(self,
                 idTranzactie,
                 idMasina,
                 idCardClient,
                 sumaPiese,
                 sumaManopera,
                 data,
                 ora):
        if self.__masinaRepository.read(idMasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        if self.__cardClientRepository.read(idCardClient) is None:
            raise KeyError("Nu exista niciun card client cu id-ul dat!")
        reducere = 0
        if idCardClient != "":
            reducere = 10

        tranzactie = Tranzactie(
            idTranzactie,
            idMasina,
            idCardClient,
            sumaPiese,
            sumaManopera,
            data,
            ora,
            reducere
        )
        self.__tranzactieRepository.modifica(tranzactie)

    def searchFullTextTranzactii(self, text):
        lst = []
        def respectareConditii(i):
            if text in i.idEntitate:
                return i
            elif text in i.idMasina:
                return i
            elif text in i.idCardClient:
                return i
            elif text in str(i.sumaPiese):
                return i
            elif text in str(i.sumaManopera):
                return i
            elif text in i.data:
                return i
            elif text in i.ora:
                return i
            elif text in str(i.reducere):
                return i
        return list(filter(respectareConditii,
                           self.__tranzactieRepository.read()))

    def afisareTranzactiiInInterval(self, iStart, iEnd):
         return list(filter(lambda i: i if iStart <= i.sumaPiese
                                          and iEnd >= i.sumaPiese
                else print(""),self.__tranzactieRepository.read()))

    def masiniOrdonateDescrescatorDupaSumaManoperei(self):
        manoperaMasini = {}
        for masina in self.__masinaRepository.read():
            manoperaMasini[masina.idEntitate] = 0
        for tranzactii in self.__tranzactieRepository.read():
            manoperaMasini[tranzactii.idMasina] += tranzactii.sumaManopera
        lst = [[x, manoperaMasini[x]] for x in manoperaMasini]
        lst = TranzactieService.bubblesort(lst, key = lambda i: i[1],
                                           reverse = True)
        rezultat = []
        for key in lst:
            rezultat.append(self.__masinaRepository.read(key[0]))
        return rezultat

    @staticmethod
    def bubblesort(lst, key, reverse):
        f = key
        if reverse == True:
            for i in range(len(lst) - 1):
                for j in range(i+1, len(lst)):
                    if f(lst[i]) < f(lst[j]):
                        aux = lst[i]
                        lst[i] = lst[j]
                        lst[j] = aux
        else:
            for i in range(len(lst) - 1):
                for j in range(i + 1, len(lst)):
                    if f(lst[i]) > f(lst[j]):
                        aux = lst[i]
                        lst[i] = lst[j]
                        lst[j] = aux
        return lst

    def carduriClientOrdonateDescrescatorReduceri(self):
        reduceri = {}
        for cardC in self.__cardClientRepository.read():
            reduceri[cardC.idEntitate] = 0
        for tranzactii in self.__tranzactieRepository.read():
            reduceri[tranzactii.idCardClient] = tranzactii.reducere

        lst = list(map(lambda x: [x, reduceri[x]], reduceri))
        fnc = lambda i: i[1]
        lst = TranzactieService.quicksort(lst, fnc, True)
        rezultat = []
        for key in lst:
            rezultat.append(self.__cardClientRepository.read(key[0]))
        return rezultat

    @staticmethod
    def quicksort(lst, key, reverse):
        if reverse == False:
            if len(lst) == 0:
                return lst
            pivot = lst[0]
            pivots = [x for x in lst if key(x) == key(pivot)]
            small = TranzactieService.quicksort(
                [x for x in lst if key(x) < key(pivot)], key, reverse)
            large = TranzactieService.quicksort(
                [x for x in lst if key(x) > key(pivot)], key, reverse)
            return small + pivots + large
        else:
            if len(lst) == 0:
                return lst
            pivot = lst[0]
            pivots = [x for x in lst if key(x) == key(pivot)]
            small = TranzactieService.quicksort(
                [x for x in lst if key(x) > key(pivot)], key, reverse)
            large = TranzactieService.quicksort(
                [x for x in lst if key(x) < key(pivot)], key, reverse)
            return small + pivots + large

    def stergereTranzactiiInIntervalZile(self, iStart, iEnd):

        list(filter(lambda i: self.sterge(i.idEntitate)
        if self.comparareDate(i.data,iStart) == \
                    True and self.comparareDate(iEnd, i.data) ==
                            True else i, self.__tranzactieRepository.read()))



    def comparareDate(self, data1, data2):
        #if data1<=data2: False
        #if data1>data2:True
        data1 = data1.split(".")
        data2 = data2.split(".")
        if data1[2]<data2[2]:
            return False
        elif data1[1]<data2[1]:
            return False
        elif data1[0]<data1[0]:
            return False
        return True

    def stergereMasinaCascada(self, idMasina):
        self.__masinaRepository.sterge(idMasina)
        lst = []
        for i in self.__tranzactieRepository.read():
            if i.idMasina == idMasina:
                lst.append(i.idEntitate)
        for i in lst:
            self.__tranzactieRepository.sterge(i)

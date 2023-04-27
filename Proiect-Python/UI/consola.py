from Service.cardClientService import CardClientService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService


class Consola:
    def __init__(self,
                 masinaService: MasinaService,
                 cardClientService: CardClientService,
                 tranzactieService: TranzactieService,
                 undoRedoService: UndoRedoService):
        self.__masinaService = masinaService
        self.__cardClientService = cardClientService
        self.__tranzactieService = tranzactieService
        self.__undoRedoService = undoRedoService

    def runMenu(self):
        while True:
            print("1. CRUD masini")
            print("2. CRUD carduri")
            print("3. CRUD tranzitii")
            print("4. Search full text")
            print("5. Afișarea mașinilor ordonate descrescător "
                  "după suma obținută pe manoperă")
            print("6. Afișarea cardurilor client ordonate descrescător "
                  "după valoarea reducerilor obținute")
            print("7. Ștergerea tuturor tranzacțiilor "
                  "dintr-un anumit interval de zile")
            print("8. Actualizarea garanției la fiecare mașină")
            print("u. Undo")
            print("r. Redo")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.runCRUDMasiniMenu()
            elif optiune == "2":
                self.runCRUDCarduriMenu()
            elif optiune == "3":
                self.runCRUDTranzitiiMenu()
            elif optiune == "4":
                self.runSearchFullText()
            elif optiune == "5":
                self.runMasiniOrdonateDescrescatorDupaSumaManoperei()
            elif optiune == "6":
                self.runCarduriClientOrdonateDescrescatorReduceri()
            elif optiune == "7":
                self.runStergereTranzactiiInIntervalZile()
            elif optiune == "8":
                self.runActualizareGarantie()
            elif optiune == "u":
                self.__undoRedoService.undo()
            elif optiune == "r":
                self.__undoRedoService.redo()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runSearchFullText(self):
        text = input("Introduce-ti textul pe care vreti sa il cautati: ")
        lst_masina = \
            self.__masinaService.searchFullTextMasina(text)
        lst_cardClient = \
            self.__cardClientService.searchFullTextCardClient(text)
        lst_tranzactii = \
            self.__tranzactieService.searchFullTextTranzactii(text)
        if len(lst_masina) != 0:
            print("Rezultate gasite in masini: ")
            for i in lst_masina:
                print(i)
        if len(lst_cardClient) != 0:
            print("Rezultate gasite in carduri clienti: ")
            for i in lst_cardClient:
                print(i)
        if len(lst_tranzactii) != 0:
            print("Rezultate gasite in tranzactii: ")
            for i in lst_tranzactii:
                print(i)
        if len(lst_masina) == 0 and \
                len(lst_cardClient) == 0 and \
                len(lst_tranzactii) == 0:
            print("Nu s-a gasit nici un rezultat.")



    def runCRUDMasiniMenu(self):
        while True:
            print("1. Adauga masina")
            print("2. Sterge masina")
            print("3. Modifica masina")
            print("4. Metoda generare masini")
            print("5. Stergere cascada")
            print("a. Afiseaza toate masinile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaMasina()
            elif optiune == "2":
                self.uiStergeMasina()
            elif optiune == "3":
                self.uiModificaMasina()
            elif optiune == "4":
                self.uiGenerareMasini()
            elif optiune == "5":
                self.uistergereMasinaCascada()
            elif optiune == "a":
                self.showAllMasini()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDCarduriMenu(self):
        while True:
            print("1. Adauga card")
            print("2. Sterge card")
            print("3. Modifica card")
            print("a. Afiseaza toate cardurile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaCardClient()
            elif optiune == "2":
                self.uiStergeCardClient()
            elif optiune == "3":
                self.uiModificaCardClient()
            elif optiune == "a":
                self.showAllCardClient()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii: ")
            model = input("Dati modelul masinii: ")
            anAchizitie = input("Dati anul de achizitie al masinii: ")
            nrKm = input("Dati nr de km al masinii: ")
            inGarantie = input("Dati garantia masinii: ")

            self.__masinaService.adauga(
                idMasina, model, anAchizitie, nrKm, inGarantie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de sters: ")

            self.__masinaService.sterge(idMasina)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de modificat: ")
            model = input("Dati noul model al masinii: ")
            anAchizitie = input("Dati noul an de achizitie al masinii: ")
            nrKm = input("Dati noul nr de km al masinii: ")
            inGarantie = input("Dati noua garantia a masinii: ")

            self.__masinaService.modifica(
                idMasina, model, anAchizitie, nrKm, inGarantie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllMasini(self):
        for masina in self.__masinaService.getAll():
            print(masina)

    def uiAdaugaCardClient(self):
        try:
            idCardClient = input("Dati id-ul cardului: ")
            nume = input("Dati numele: ")
            prenume = input("Dati prenumele: ")
            CNP = input("Dati CNP-ul: ")
            dataNasterii = input("Dati data nasterii: ")
            dataInregistrarii = input("Dati data inregistrarii: ")

            self.__cardClientService.adauga(
                idCardClient,
                nume,
                prenume,
                CNP,
                dataNasterii,
                dataInregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeCardClient(self):
        try:
            idCardClient = input("Dati id-ul cardului de sters: ")

            self.__cardClientService.sterge(idCardClient)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaCardClient(self):
        try:
            idCardClient = input("Dati id-ul cardului de modificat: ")
            nume = input("Dati noul nume: ")
            prenume = input("Dati noul prenume: ")
            CNP = input("Dati noul CNP: ")
            dataNasterii = input("Dati noua data a nasterii: ")
            dataInregistrarii = input("Dati noua data a inregistrarii: ")

            self.__cardClientService.modifica(
                idCardClient,
                nume,
                prenume,
                CNP,
                dataNasterii,
                dataInregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllCardClient(self):
        for cardClient in self.__cardClientService.getAll():
            print(cardClient)

    def runCRUDTranzitiiMenu(self):
        while True:
            print("1. Adauga tranzactie")
            print("2. Sterge tranzactie")
            print("3. Modifica tranzactie")
            print("4. Afisare tranzactii cu suma intr-un anumit interval")
            print("a. Afiseaza toate tranzactiile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaTranzactie()
            elif optiune == "2":
                self.uiStergeTranzactie()
            elif optiune == "3":
                self.uiModificaTranzactie()
            elif optiune == "4":
                self.uiAfisareTranzactiiInInterval()
            elif optiune == "a":
                self.showAllTranziti()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaTranzactie(self):
        try:
            idTranzactie = input("Dati id-ul tranzactiei: ")
            idMasina = input("Dati id-ul masinii: ")
            idCardClient = input("Dati id-ul card client: ")
            sumaPiese = float(input("Dati suma piselor: "))
            sumaManopera = float(input("Dati suma manoperei: "))
            data = input("Dati data: ")
            ora = input("Dati ora: ")

            self.__tranzactieService.adauga(
                idTranzactie,
                idMasina,
                idCardClient,
                sumaPiese,
                sumaManopera,
                data,
                ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeTranzactie(self):
        try:
            idTranzactie = input("Dati id-ul tranzactiei de sters: ")

            self.__tranzactieService.sterge(idTranzactie)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaTranzactie(self):
        try:
            idTranzactie = input("Dati id-ul tranzactiei de modificat: ")
            idMasina = input("Dati noul id masinii: ")
            idCardClient = input("Dati noul id card client: ")
            sumaPiese = float(input("Dati noua suma a piselor: "))
            sumaManopera = float(input("Dati noua suma a manoperei: "))
            data = float(input("Dati noua data: "))
            ora = input("Dati noua ora: ")

            self.__tranzactieService.modifica(
                idTranzactie,
                idMasina,
                idCardClient,
                sumaPiese,
                sumaManopera,
                data,
                ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllTranziti(self):
        for tranzactie in self.__tranzactieService.getAll():
            print(tranzactie)

    def uiAfisareTranzactiiInInterval(self):
        iStart = float(input("Dati valoare de inceput al intervalului: "))
        iEnd = float(input("Dati valoare de sfarsit al intervalului: "))
        lst = self.__tranzactieService.\
            afisareTranzactiiInInterval(iStart, iEnd)
        if len(lst) != 0:
            for i in lst:
                print(i)
        else:
            print("Nu s-a gasit nici o tranzactie cu suma in interval")

    def runMasiniOrdonateDescrescatorDupaSumaManoperei(self):
        lst = self.__tranzactieService.\
            masiniOrdonateDescrescatorDupaSumaManoperei()
        for i in lst:
            print(i)

    def runCarduriClientOrdonateDescrescatorReduceri(self):
        lst = self.__tranzactieService.\
            carduriClientOrdonateDescrescatorReduceri()
        for i in lst:
            print(i)

    def runStergereTranzactiiInIntervalZile(self):
        iStart = input("Dati data de inceput al intervalului: ")
        iEnd = input("Dati data de sfarsit al intervalului: ")
        self.__tranzactieService.\
            stergereTranzactiiInIntervalZile(iStart, iEnd)

    def runActualizareGarantie(self):
        self.__masinaService.actualizareGarantie()

    def uiGenerareMasini(self):
        n = int(input("Dati nr de masini care doriti sa fie generate: "))
        self.__masinaService.generareMasini(n)

    def uistergereMasinaCascada(self):
        n = input("Dati id-ul masini de sters: ")
        self.__tranzactieService.stergereMasinaCascada(n)

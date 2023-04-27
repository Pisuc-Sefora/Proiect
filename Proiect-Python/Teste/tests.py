from Domain.cardClientValidator import CardClientValidator
from Domain.masina import Masina
from Domain.masinaValidator import MasinaValidator
from Service.cardClientService import CardClientService
from Repository.repositoryJson import RepositoryJson
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService


def runAllTests():
    testAdaugaMasina()
    testStergeMasina()
    testModificaMasina()
    testActualizareGarantie()
    testAdaugaCardClient()
    testStergeCardClient()
    testModificaCardClient()
    testAdaugaTranzactie()
    testModificaTranzactie()
    testStergeTranzactie()
    testStergereTranzactiiInIntervalZile()
    testAfisareTranzactiiInInterval()
    testMasiniOrdonateDescrescatorDupaSumaManoperei()
    testCarduriClientOrdonateDescrescatorReduceri()
    testSearchFullText()

def clearFile(filename):
    with open(filename, "w") as f:
        pass

def testAdaugaMasina():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    masina = masinaService.getAll()
    assert len(masina) == 2
    assert masina[0].idEntitate == "1"
    assert masina[0].model == "Bw"
    assert masina[0].an == "2021"
    assert masina[0].nrKm == "10000"
    assert masina[0].inGarantie == "Da"
    assert masina[1].idEntitate == "2"
    assert masina[1].model == "Mercedes"
    assert masina[1].an == "2017"
    assert masina[1].nrKm == "670000"
    assert masina[1].inGarantie == "Nu"


def testStergeMasina():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")
    nrMasini = len(masinaService.getAll())
    masinaService.sterge("2")
    masina = masinaService.getAll()
    assert len(masina) == nrMasini - 1

def testModificaMasina():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)
    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    masinaService.modifica("1", "Nissan", "2019", "390000", "Da")
    masina = masinaService.getAll()
    assert masina[0].idEntitate == "1"
    assert masina[0].model == "Nissan"
    assert masina[0].an == "2019"
    assert masina[0].nrKm == "390000"
    assert masina[0].inGarantie == "Da"

def testActualizareGarantie():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Da")

    masinaService.actualizareGarantie()

    assert masinaService.getMasinaById("1").inGarantie == "Da"
    assert masinaService.getMasinaById("2").inGarantie == "Nu"

def testAdaugaCardClient():
    clearFile("test-masini.json")
    masinaRepository = RepositoryJson("test-masini.json")

    masinaRepository.create(Masina("1", "Bw", "2021", "10000", "Da"))
    masinaRepository.create(Masina("2", "Mercedes", "2017", "670000", "Nu"))

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    cardClient = cardClientService.getAll()
    assert len(cardClient) == 2
    assert cardClient[0].idEntitate == "1"
    assert cardClient[0].nume == "Pop"
    assert cardClient[0].prenume == "Ana"
    assert cardClient[0].CNP == "2098357102878"
    assert cardClient[0].dataNasterii == "02.02.2002"
    assert cardClient[0].dataInregistrarii == "12.12.2020"
    assert cardClient[1].idEntitate == "2"
    assert cardClient[1].nume == "Rus"
    assert cardClient[1].prenume == "Andrei"
    assert cardClient[1].CNP == "6020874109145"
    assert cardClient[1].dataNasterii == "03.12.1998"
    assert cardClient[1].dataInregistrarii == "12.12.2021"

def testStergeCardClient():
    clearFile("test-masini.json")
    masinaRepository = RepositoryJson("test-masini.json")

    masinaRepository.create(Masina("1", "Bw", "2021", "10000", "Da"))
    masinaRepository.create(Masina("2", "Mercedes", "2017", "670000", "Nu"))
    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")
    nrCardClient = len(cardClientService.getAll())
    cardClientService.sterge("1")
    cardClient = cardClientService.getAll()
    assert len(cardClient) == nrCardClient - 1

def testModificaCardClient():
    clearFile("test-masini.json")
    masinaRepository = RepositoryJson("test-masini.json")

    masinaRepository.create(Masina("1", "Bw", "2021", "10000", "Da"))
    masinaRepository.create(Masina("2", "Mercedes", "2017", "670000", "Nu"))

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")
    cardClientService.modifica("1", "Mich", "Marius", "2010487264921",
                               "01.01.2001", "22.09.2021")
    cardClient = cardClientService.getAll()
    assert cardClient[0].idEntitate == "1"
    assert cardClient[0].nume == "Mich"
    assert cardClient[0].prenume == "Marius"
    assert cardClient[0].CNP == "2010487264921"
    assert cardClient[0].dataNasterii == "01.01.2001"
    assert cardClient[0].dataInregistrarii == "22.09.2021"

def testAdaugaTranzactie():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    clearFile("test-tranzactii.json")
    tranzactieRepository = RepositoryJson("test-tranzactii.json")
    tranzactieService = TranzactieService(tranzactieRepository,
                                          masinaRepository,
                                          cardClientRepository)
    tranzactieService.adauga("1", "1", "2", 315.0, 690.99,
                             "01.12.2021", "15:17")

    tranzactii = tranzactieService.getAll()
    assert len(tranzactii) == 1
    assert tranzactii[0].idEntitate == "1"
    assert tranzactii[0].idMasina == "1"
    assert tranzactii[0].idCardClient == "2"
    assert tranzactii[0].sumaPiese == 0
    #suma piese devine 0 pt ca masina e in garantie
    assert tranzactii[0].sumaManopera == 690.99
    assert tranzactii[0].data == "01.12.2021"
    assert tranzactii[0].ora == "15:17"
    assert tranzactii[0].reducere == 10

def testStergeTranzactie():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    clearFile("test-tranzactii.json")
    tranzactieRepository = RepositoryJson("test-tranzactii.json")
    tranzactieService = TranzactieService(tranzactieRepository,
                                          masinaRepository,
                                          cardClientRepository)
    tranzactieService.adauga("1", "1", "2", 315.0, 690.99,
                             "01.12.2021", "15:17")
    nrTranzactii = len(cardClientService.getAll())
    cardClientService.sterge("1")
    tranzactie = tranzactieService.getAll()
    assert len(tranzactie) == nrTranzactii - 1

def testModificaTranzactie():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    clearFile("test-tranzactii.json")
    tranzactieRepository = RepositoryJson("test-tranzactii.json")
    tranzactieService = TranzactieService(tranzactieRepository,
                                          masinaRepository,
                                          cardClientRepository)
    tranzactieService.adauga("1", "1", "2", 315.0, 690.99,
                             "01.12.2021", "15:17")
    tranzactieService.modifica("1", "2", "1", 110.0, 250.0,
                               "10.10.2020", "11:37")
    tranzactii = tranzactieService.getAll()
    assert tranzactii[0].idEntitate == "1"
    assert tranzactii[0].idMasina == "2"
    assert tranzactii[0].idCardClient == "1"
    assert tranzactii[0].sumaPiese == 110.0
    assert tranzactii[0].sumaManopera == 250.0
    assert tranzactii[0].data == "10.10.2020"
    assert tranzactii[0].ora == "11:37"
    assert tranzactii[0].reducere == 10

def testSearchFullTextMasini():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    masina = masinaService.searchFullTextMasini()
    assert len(masina) == 2
    assert masina[0].idMasina == "1"
    assert masina[1].idMasina == "2"

def testMasiniOrdonateDescrescatorDupaSumaManoperei():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    clearFile("test-tranzactii.json")
    tranzactieRepository = RepositoryJson("test-tranzactii.json")
    tranzactieService = TranzactieService(tranzactieRepository,
                                          masinaRepository,
                                          cardClientRepository)
    tranzactieService.adauga("1", "1", "2", 315.0, 690.99,
                             "01.12.2021", "15:17")
    tranzactieService.adauga("2", "2", "2", 123, 1430,
                             "10.10.2018", "13:11")
    masina = tranzactieService.masiniOrdonateDescrescatorDupaSumaManoperei()
    assert masina[0].idEntitate == "2"
    assert masina[1].idEntitate == "1"

def testCarduriClientOrdonateDescrescatorReduceri():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    clearFile("test-tranzactii.json")
    tranzactieRepository = RepositoryJson("test-tranzactii.json")
    tranzactieService = TranzactieService(tranzactieRepository,
                                          masinaRepository,
                                          cardClientRepository)
    tranzactieService.adauga("1", "1", "2", 315.0, 690.99,
                             "01.12.2021", "15:17")
    tranzactieService.adauga("2", "2", "2", 123, 1430,
                             "10.10.2018", "13:11")
    cardClient = tranzactieService.carduriClientOrdonateDescrescatorReduceri()
    assert cardClient[0].idEntitate == "2"

def testAfisareTranzactiiInInterval():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    clearFile("test-tranzactii.json")
    tranzactieRepository = RepositoryJson("test-tranzactii.json")
    tranzactieService = TranzactieService(tranzactieRepository,
                                          masinaRepository,
                                          cardClientRepository)
    tranzactieService.adauga("1", "1", "2", 315, 690.99,
                             "01.12.2021", "15:17")
    tranzactieService.adauga("2", "2", "2", 123, 1430,
                             "10.10.2018", "13:11")
    tranzactie = tranzactieService.afisareTranzactiiInInterval(100, 300)
    assert len(tranzactie) == 1
    assert tranzactie[0].idEntitate == "2"

def testStergereTranzactiiInIntervalZile():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Ana", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    clearFile("test-tranzactii.json")
    tranzactieRepository = RepositoryJson("test-tranzactii.json")
    tranzactieService = TranzactieService(tranzactieRepository,
                                          masinaRepository,
                                          cardClientRepository)
    tranzactieService.adauga("1", "1", "2", 315.0, 690.99,
                             "01.12.2021", "15:17")
    tranzactieService.adauga("2", "2", "2", 123, 1430,
                             "10.10.2018", "13:11")
    nrTranzactii = len(tranzactieService.getAll())
    tranzactieService.stergereTranzactiiInIntervalZile(
        "13.01.2010", "16.12.2020")
    tranzactie = tranzactieService.getAll()
    assert len(tranzactie) == nrTranzactii - 1

def testSearchFullText():
    clearFile("test-masini.json")
    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("test-masini.json")
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository, masinaValidator,
                                  undoRedoService)

    masinaService.adauga("1", "Bw", "2021", "10000", "Da")
    masinaService.adauga("2", "Mercedes", "2017", "670000", "Nu")

    clearFile("test-cardClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientRepository = RepositoryJson("test-cardClienti.json")
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          cardClientValidator, undoRedoService)

    cardClientService.adauga("1", "Pop", "Alice", "2098357102878",
                             "02.02.2002", "12.12.2020")
    cardClientService.adauga("2", "Rus", "Andrei", "6020874109145",
                             "03.12.1998", "12.12.2021")

    clearFile("test-tranzactii.json")
    tranzactieRepository = RepositoryJson("test-tranzactii.json")
    tranzactieService = TranzactieService(tranzactieRepository,
                                          masinaRepository,
                                          cardClientRepository)
    tranzactieService.adauga("1", "1", "2", 315.0, 690.99,
                             "01.12.2021", "15:17")
    tranzactieService.adauga("2", "2", "2", 123, 1430,
                             "10.10.2018", "13:11")

    masina = masinaService.searchFullTextMasina("10")
    assert len(masina) == 1
    assert masina[0].idEntitate == "1"

    cardClient = cardClientService.searchFullTextCardClient("Ali")
    assert len(cardClient) == 1
    assert cardClient[0].idEntitate == "1"

    tranzactie = tranzactieService.searchFullTextTranzactii("2018")
    assert len(tranzactie) == 1
    assert tranzactie[0].idEntitate == "2"

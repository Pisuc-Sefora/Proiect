from Domain import cardClientValidator
from Domain.cardClientValidator import CardClientValidator
from Domain.masinaValidator import MasinaValidator
from Repository.repositoryJson import RepositoryJson
from Service.cardClientService import CardClientService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService
from Teste.tests import runAllTests
from UI.consola import Consola


def main():
    undoRedoService = UndoRedoService()

    masinaRepositoryJson = RepositoryJson("masini.json")
    masinaValidator = MasinaValidator()
    masinaService = MasinaService(masinaRepositoryJson, masinaValidator,
                                  undoRedoService)

    cardClientRepositoryJson = RepositoryJson("cardClient.json")
    cardClientValidator = CardClientValidator()
    cardClientService = CardClientService(cardClientRepositoryJson, cardClientValidator,
                                          undoRedoService)

    tranzactieRepositoryJson = RepositoryJson("tranzactie.json")
    tranzactieService = TranzactieService(
        tranzactieRepositoryJson,
        masinaRepositoryJson,
        cardClientRepositoryJson)

    consola = Consola(masinaService, cardClientService, tranzactieService,
                      undoRedoService
                      )

    consola.runMenu()


if __name__ == '__main__':
    runAllTests()
    main()

from Domain.cardClientValidator import CardClientValidator
from Domain.addOperation import AddOperation
from Domain.cardClient import CardClient
from Domain.modifyOperation import ModifyOperation
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class CardClientService:
    def __init__(self, cardClientRepository: Repository,
                 cardClientValidator: CardClientValidator,
                 undoRedoService: UndoRedoService):
        self.__cardClientRepository = cardClientRepository
        self.__cardClientValidator = cardClientValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__cardClientRepository.read()

    def adauga(self,
               idCardClient,
               nume,
               preunume,
               CNP,
               dataNasterii,
               dataInregistrarii):
        cardClient = CardClient(
            idCardClient,
            nume,
            preunume,
            CNP,
            dataNasterii,
            dataInregistrarii)
        self.__cardClientValidator.valideaza(cardClient, self.__cardClientRepository)

        self.__cardClientRepository.adauga(cardClient)
        self.__undoRedoService.addUndoOperation(
            AddOperation(self.__cardClientRepository, cardClient))

    def sterge(self, idCardClient):
        self.__cardClientRepository.sterge(idCardClient)

    def modifica(self,
                 idCardClient,
                 nume,
                 preunume,
                 CNP,
                 dataNasterii,
                 dataInregistrarii):
        cardClientVechi = self.__cardClientRepository.read(idCardClient)
        cardClient = CardClient(
            idCardClient,
            nume,
            preunume,
            CNP,
            dataNasterii,
            dataInregistrarii)
        self.__cardClientRepository.modifica(cardClient)
        self.__undoRedoService.addUndoOperation(
            ModifyOperation(self.__cardClientRepository, cardClientVechi,
                            cardClient))

    def searchFullTextCardClient(self, text):
        lst = []
        for i in self.__cardClientRepository.read():
            if text in i.idEntitate:
                lst.append(i)
            elif text in i.nume:
                lst.append(i)
            elif text in i.prenume:
                lst.append(i)
            elif text in i.CNP:
                lst.append(i)
            elif text in i.dataNasterii:
                lst.append(i)
            elif text in i.dataInregistrarii:
                lst.append(i)
        return lst

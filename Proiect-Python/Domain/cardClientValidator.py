from Domain.cardClient import CardClient
from Repository.repository import Repository


class CardClientValidator:
    def valideaza(self,
                  cardClient: CardClient,
                  cardClientRepository: Repository):
        erori = []
        if self.valideazaData(cardClient.dataNasterii) == False:
            erori.append("Data nasterii nu e valida")
        if self.valideazaData(cardClient.dataInregistrarii) == False:
            erori.append("Data inregistrarii nu e valida")
        lst_cnp = [cc.CNP for cc in cardClientRepository.read()]
        if cardClient.CNP in lst_cnp:
            erori.append("CNP-ul nu este unic")
        if len(erori) > 0:
            raise ValueError(erori)

    def valideazaData(self, data):
        lst = data.split(".")
        if int(lst[1]) <= 0:
            return False
        else:
            if lst[1] == "02":
                if int(lst[0]) <= 0 or int(lst[0]) > 28:
                    return False
            elif lst[1] in ["01", "03", "05", "07", "08","10", "12"]:
                if int(lst[0]) <= 0 or int(lst[0]) > 31:
                    return False
            elif lst[1] in ["04", "06", "09", "11"]:
                if int(lst[0]) <= 0 or int(lst[0]) > 30:
                    return False
            elif int(lst[1]) <= 0 or int(lst[1]) > 12:
                return False
        return True

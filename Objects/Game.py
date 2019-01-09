from datetime import datetime
from Constants import Constants
from Makers import Check

class Game:
    def __init__(self, tournament, players, score, meet):
        self.players = players
        self.tournament = tournament
        self.score = score
        self.meet = meet
        # self.firstRating = '0/0/0/0'
        # self.secondRating = '0/0/0/0'
        # #self.initScoreZero()
        # self.initSendStrat(countStrat = countStrat)
        self.score = score
        dateNow = datetime.now()
        self.yearNow = dateNow.year
        self.monthNow = dateNow.month
        # self.id_tournament = id_tournament
        # self.dirtyScore = dirtyScore.replace("-", ":")
        # self.coeffFirst = coeffFirst
        # self.coeffSecond = coeffSecond
        # self.listOfSendEvent = []
        # self.lastCoefFirst = "0.0"
        # self.lastCoefSecond = "0.0"
        pass
    #
    # def isValidRating(self):
    #     if (self.firstRating != '0' and self.secondRating != '0'):
    #         return True
    #     else:
    #         return False
    #
    # def initSendStrat(self, countStrat):
    #     self.listSendStrat = []
    #     for i in range(0, countStrat):
    #         self.listSendStrat.append(False)
    #
    #
    #
    # def isPrintStrat(self, idStrat):
    #     return self.listSendStrat[idStrat - 1]
    #
    # def goodAge(self, nameID):
    #     if (nameID == Constants.ID_1 or nameID == Constants.ID_2):
    #         if (int(self.yearNow) - int(self.firstRating.split('/')[2]) >= Constants.MIN_YEAR
    #                 and int(self.yearNow) - int(self.secondRating.split('/')[2]) >= Constants.MIN_YEAR):
    #             return True
    #         else:
    #             return False
    #     elif (nameID == Constants.ID_3 or nameID == Constants.ID_4):
    #         return True
    #     else:
    #         return False
    #
    # def __eq__(self, other):
    #     if isinstance(other, Game):
    #         return (self.firstPlayer == other.firstPlayer and self.secondPlayer == other.secondPlayer)
    #     return NotImplemented
    #
    #
    # # SET METHODS
    # def setPrintStrat(self, idStrat):
    #     self.listSendStrat.remove(self.listSendStrat[idStrat - 1])
    #     self.listSendStrat.insert(idStrat - 1, True)
    #
    # def setListSendStrat(self, listOfSendStrat):
    #     self.listSendStrat = listOfSendStrat.copy()
    #
    # def setScore(self, newScore):
    #     self.score = newScore
    #
    # def setIsUpdate(self, isUpdate):
    #     self.isUpdate = isUpdate
    #
    # def setRating(self, ratingFirst, ratingSecond):
    #     self.firstRating = ratingFirst
    #     self.secondRating = ratingSecond
    #
    #
    # # GET METHODS
    # def getRatingPlayersPrint(self):
    #     strToPrint = ""
    #     if (self.id_tournament == Constants.ID_1 or
    #         self.id_tournament == Constants.ID_2):
    #         splitFirstRating = self.firstRating.split('/')
    #         splitSecondRating = self.secondRating.split('/')
    #         strToPrint += "Начальные кефы: " + self.coeffFirst + " - " + \
    #             self.coeffSecond + "\n"
    #         strToPrint += "текущие кефы: " + self.lastCoefFirst + " - " + \
    #                       self.lastCoefSecond + "\n"
    #         strToPrint += "Рейтинг(Москва/Украина): " + splitFirstRating[0] + " - " + \
    #                       splitSecondRating[0] + "\n"
    #         strToPrint += "Рейтинг (этот ТТ): " + splitFirstRating[1] + " - " + \
    #                       splitSecondRating[1] + "\n"
    #         strToPrint += "Год рождения: " + splitFirstRating[2] + " - " + \
    #                       splitSecondRating[2] + "\n"
    #         strToPrint += "Турниры(кол-во): " + splitFirstRating[3] + " - " + \
    #                       splitSecondRating[3] + "\n"
    #     elif (self.id_tournament == Constants.ID_3 or
    #         self.id_tournament == Constants.ID_4):
    #         strToPrint += "Начальные кефы: " + self.coeffFirst + " - " + \
    #             self.coeffSecond + "\n"
    #         strToPrint += "текущие кефы: " + self.lastCoefFirst + " - " + \
    #                       self.lastCoefSecond + "\n"
    #         strToPrint += "Рейтинг в лиге про: " + self.firstRating.split('/')[0] + " - " + \
    #                       self.secondRating.split('/')[0] + "\n"
    #     return strToPrint
    #
    # def getWinPlayer(self):
    #     if (self.score[0].getFirstScore() > self.score[0].getSecondScore()):
    #         return "1"#, self.firstPlayer
    #     elif (self.score[0].getFirstScore() < self.score[0].getSecondScore()):
    #         return "2"#, self.secondPlayer
    #     else:
    #         return "Нету победителя"
    #
    # def getFavPlayer(self):
    #     if (Check.checkFavRating(1, self.coeffFirst, self.coeffSecond) == Constants.FAVARIT):
    #         return "1"#self.firstPlayer
    #     elif (Check.checkFavRating(2, self.coeffFirst, self.coeffSecond) == Constants.FAVARIT):
    #         return "2"#self.secondPlayer
    #     else:
    #         return "Нету фаворита"
    #
    # def getLoserPlayer(self):
    #     if (self.score[0].getFirstScore() < self.score[0].getSecondScore()):
    #         return "1"#self.firstPlayer
    #     elif (self.score[0].getFirstScore() > self.score[0].getSecondScore()):
    #         return "2"#self.secondPlayer
    #     else:
    #         return "Нету победителя"
    #
    # def getLosRatPlayer(self):
    #     if (Check.checkFavRating(1, self.coeffFirst, self.coeffSecond) == Constants.LOSER_RATING):
    #         return "1"#self.firstPlayer
    #     elif (Check.checkFavRating(2, self.coeffFirst, self.coeffSecond) == Constants.LOSER_RATING):
    #         return "2"#self.secondPlayer
    #     else:
    #         return "Нету фаворита"
    #
    # def getAllPlayer(self):
    #     return self.firstPlayer + " - " + self.secondPlayer
    #
    # def getListSendStrat(self):
    #     return self.listSendStrat
    #
    # def getFirstPlayer(self):
    #     return self.firstPlayer
    #
    # def getSecondPlayer(self):
    #     return self.secondPlayer
    #
    # def getScore(self):
    #     return self.score
    #
    # def getIsUpdate(self):
    #     return self.isUpdate
    #
    # def getFirstRating(self):
    #     return self.firstRating
    #
    # def getSecondRating(self):
    #     return self.secondRating
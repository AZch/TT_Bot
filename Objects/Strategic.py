from Makers import Check
from Constants import Constants
from Objects.EndGame import EndGame


class StrategicTableTennis:
    def __init__(self, description, countStrat, sets, isEverySet, isMore, scoreCheck, isCheckSet, isOneWin,
                 whatGame, isFavorite, whyPlayer, howWin, endScoreCheck, endSet):
        self.description = description
        self.countStrat = countStrat
        self.sets = sets
        self.isEverySet = isEverySet
        self.isMore = isMore
        self.scoreCheck = scoreCheck
        self.isCheckSet = isCheckSet
        self.isOneWin = isOneWin
        self.whatGame = whatGame
        self.isFavorite = isFavorite
        self.howWin = howWin
        self.whyPlayer = whyPlayer
        self.endScoreCheck = endScoreCheck
        self.endSet = endSet
        pass

    def analysisStrat(self, setsScore):
        if (self.whatGame == Constants.GAME_TT and (setsScore[0].getFirstScore() == 3 or setsScore[0].getSecondScore() == 3)):
            return False
        if (setsScore[0].getFirstScore() + setsScore[0].getSecondScore() != len(self.sets)):
            return False
        if (self.isOneWin):
            if (abs(setsScore[0].getFirstScore() - setsScore[0].getSecondScore()) != len(self.sets)):
                return False
        saveFirstScore = setsScore[0]
        trueSet = ""
        countDiff = 0
        whatSets = self.sets
        if (self.isCheckSet):
            whatSets = self.scoreCheck
        for set in whatSets: # номер сета
            doneSet = False
            isFirstSet = False
            for oneSet in setsScore: # физичиский сет
                if (oneSet.getCountSet() == int(set)):
                    doneSet = True
                    if (self.isCheckSet):
                        if (oneSet.getFirstScore() > oneSet.getSecondScore()):
                            if (len(trueSet) == len("")):
                                isFirstSet = True
                                trueSet += set
                            elif (isFirstSet):
                                trueSet += set
                            else:
                                return False
                        else:
                            if (len(trueSet) == len("")):
                                isFirstSet = False
                                trueSet += set
                            elif (not isFirstSet):
                                trueSet += set
                            else:
                                return False
                    elif (self.isEverySet):
                        if (self.isMore):
                            if (abs(oneSet.getFirstScore() - oneSet.getSecondScore()) >= int(self.scoreCheck)):
                                trueSet += set
                            else:
                                return False
                        else:
                            if (abs(oneSet.getFirstScore() - oneSet.getSecondScore()) <= int(self.scoreCheck)):
                                trueSet += set
                            else:
                                return False
                    else:
                        countDiff += abs(oneSet.getFirstScore() - oneSet.getSecondScore())
                        trueSet += set
        if (whatSets == trueSet):
            if (self.isEverySet):
                return True
            else:
                if (self.isMore and countDiff >= int(self.scoreCheck)):
                    return True
                elif (not self.isMore and countDiff <= int(self.scoreCheck)):
                    return True
                else:
                    return False
        else:
            return False

    # анализирует только фаваритов
    def analysisFavarite(self, game, current_id_name_game):
        if (game.getScore()[0].getFirstScore() == game.getScore()[0].getSecondScore()):
            if (Check.checkFavRating(1, game.lastCoefFirst, game.lastCoefSecond) == self.isFavorite):
                if (game.getScore()[int(self.sets[0])].getFirstScore() > game.getScore()[int(self.sets[0])].getSecondScore()):
                    return self.isFavorite
                else:
                    return Constants.LOSER_FAVARIT
            elif (Check.checkFavRating(2, game.lastCoefFirst, game.lastCoefSecond) == self.isFavorite):
                if (game.getScore()[int(self.sets[0])].getFirstScore() < game.getScore()[int(self.sets[0])].getSecondScore()):
                    return self.isFavorite
                else:
                    return Constants.LOSER_FAVARIT
            else:
                return Check.checkFavRating(2, game.lastCoefFirst, game.lastCoefSecond)
        if (game.getScore()[0].getFirstScore() >= game.getScore()[0].getSecondScore()):
            if (Check.checkFavRating(1, game.lastCoefFirst, game.lastCoefSecond) == self.isFavorite):
                return self.isFavorite
            else:
                return Check.checkFavRating(1, game.lastCoefFirst, game.lastCoefSecond)
        elif (game.getScore()[0].getFirstScore() <= game.getScore()[0].getSecondScore()):
            if (Check.checkFavRating(2, game.lastCoefFirst, game.lastCoefSecond) == self.isFavorite):
                return self.isFavorite
            else:
                return Check.checkFavRating(2, game.lastCoefFirst, game.lastCoefSecond)

    def getCountStrat(self):
        return self.countStrat

    def getDescription(self):
        return self.description

    def getWhyPlayer(self):
        return self.whyPlayer

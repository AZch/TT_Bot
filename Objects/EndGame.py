from Constants import Constants
from Objects.Game import Game
from Makers import Check

class EndGame:
    def __init__(self, isEverySet, sets, whoWin, count, what_hand):
        self.isEverySet = isEverySet
        self.sets = sets
        self.whoWin = whoWin
        self.count = count
        self.what_hand = what_hand
        pass

    def CheckEndGame(self, game, strat):
        if (strat.whatGame == Constants.GAME_TT and (game.score[0].getFirstScore() + game.score[0].getSecondScore() != 5)):
            return False
        trueSet = ""
        countDiff = 0
        firstScoreEnd = 0
        secondScoreEnd = 0
        for set in self.sets: # номер сета
            for oneSet in game.score:
                if (oneSet.getCountSet() == int(set)):
                    if (not self.isEverySet):
                        firstScoreEnd += oneSet.getFirstScore()
                        secondScoreEnd += oneSet.getSecondScore()
                    else:
                       if (not Check.checkWin(whoWinFlag=self.whoWin, scoreFirst=oneSet.getFirstScore(),
                                          scoreSecond=oneSet.getSecondScore(), count=self.count, WHAT_HAND=self.what_hand)):
                           return False
        if (not self.isEverySet):
            if (not Check.checkWin(whoWinFlag=self.whoWin, scoreFirst=firstScoreEnd,
                               scoreSecond=secondScoreEnd, count=self.count, WHAT_HAND=self.what_hand)):
                return False
        return True
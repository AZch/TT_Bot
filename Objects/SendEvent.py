from Objects.Game import Game
from Objects.Strategic import StrategicTableTennis
from Constants import Constants

class SendEvent:
    def __init__(self, nameF, nameS, dirty, isScore, whyPlayer, countPrint):
        self.nameF = nameF
        self.nameS = nameS
        self.dirty = dirty
        self.isScore = isScore
        self.whyPlayer = whyPlayer
        self.countPrint = countPrint
        pass
        # self.link = link
        # self.total = total
        # self.whyTeam = whyTeam
    # def __init__(self, countPrint, game, whatPlayer, scoreCheck, howWin, gameSet):
    #     self.game = game
    #     self.countPrint = countPrint
    #     self.whatPlayer = whatPlayer
    #     self.scoreChek = scoreCheck
    #     self.howWin = howWin
    #     self.gameSet = gameSet
    #     pass
    #
    # def checkEvent(self, scoreGame):
    #     try:
    #         if (int(scoreGame[0].first) + int(scoreGame[0].second) != self.gameSet):
    #             return Constants.GAME_NOT_END
    #     except:
    #         send_message(chat_id=281265894, text="problem send event") # i'm
    #         return Constants.GAME_NOT_END
    #
    #     if (self.howWin == Constants.HOW_GAME_WIN):
    #         if (self.whatPlayer == "1" and int(scoreGame[self.gameSet].first) > int(scoreGame[self.gameSet].second)):
    #             return Constants.GAME_WIN
    #         elif (self.whatPlayer == "2" and int(scoreGame[self.gameSet].first) < int(scoreGame[self.gameSet].second)):
    #             return Constants.GAME_WIN
    #         else:
    #             return Constants.GAME_LOSE
    #     elif (self.howWin == Constants.HOW_GAME_TOTAL_U):
    #         if (int(scoreGame[self.gameSet].first) + int(scoreGame[self.gameSet].second) >= self.scoreChek):
    #             return Constants.GAME_WIN
    #         else:
    #             return Constants.GAME_LOSE
    #     elif (self.howWin == Constants.HOW_GAME_TOTAL_D):
    #         if (int(scoreGame[self.gameSet].first) + int(scoreGame[self.gameSet].second) <= self.scoreChek):
    #             return Constants.GAME_WIN
    #         else:
    #             return Constants.GAME_LOSE
    #     elif (self.howWin == Constants.HOW_GAME_HAND):
    #         if (self.whatPlayer == "1" and int(scoreGame[self.gameSet].first) + self.scoreChek > int(scoreGame[self.gameSet].second)):
    #             return Constants.GAME_WIN
    #         elif (self.whatPlayer == "2" and int(scoreGame[self.gameSet].first) < int(scoreGame[self.gameSet].second) + self.scoreChek):
    #             return Constants.GAME_WIN
    #         else:
    #             return Constants.GAME_LOSE
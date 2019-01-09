from Constants import Constants
from Objects.OneScore import OneScore


# вывод результатов из лиги про
def printLigaPro(game, countPrint, curr_name_tournament, strat, text_split, count, prevStr):
    strToPrint = "#TT" + str(countPrint) + " " + prevStr + "\n"
    strToPrint += Constants.getTournamentByID(curr_name_tournament) + "\n"
    strToPrint += game.getFirstPlayer() + " - " + game.getSecondPlayer() + "\n"
    strToPrint += game.getRatingPlayersPrint()
    if (game.score[0].first == 2 and game.score[0].second == game.score[0].first):
        countFirstScore = 0
        countSecondScore = 0
        for oneScore in game.score[1:]:
            countFirstScore += oneScore.first
            countSecondScore += oneScore.second
        strToPrint += "Сумма очков: " + str(countFirstScore) + " : " + str(countSecondScore) + "\n"
    strToPrint += "Счёт: " + text_split[count + 1].replace("-", ":") + "\n"
    strToPrint +=  strat.getDescription() +  printStratGame(game=game, strat=strat)
    return strToPrint

# вывод результатов из тт кап
def printTT_CUP(game, countPrint, curr_name_tournament, strat, text_split, count, prevStr):
    strToPrint = "#TT" + str(countPrint) + " " + prevStr + "\n"
    strToPrint += Constants.getTournamentByID(curr_name_tournament) + "\n"
    strToPrint += game.getFirstPlayer() + " - " + game.getSecondPlayer() + "\n"
    strToPrint += game.getRatingPlayersPrint()
    if (game.score[0].first == 2 and game.score[0].second == game.score[0].first):
        countFirstScore = 0
        countSecondScore = 0
        for oneScore in game.score[1:]:
            countFirstScore += oneScore.first
            countSecondScore += oneScore.second
        strToPrint += "Сумма очков: " + str(countFirstScore) + " : " + str(countSecondScore) + "\n"
    strToPrint += "Счёт: " + text_split[count + 1].replace("-", ":") + "\n"
    strToPrint +=  strat.getDescription() +  printStratGame(game=game, strat=strat)

    return strToPrint

def printStratGame(game, strat):
    if (strat.getWhyPlayer() == Constants.WIN_PLAYER):
        return game.getWinPlayer()
    elif (strat.getWhyPlayer() == Constants.FAV_PLAYER):
        return game.getFavPlayer()
    elif (strat.getWhyPlayer() == Constants.NOT_PLAYER):
        return ""
    elif (strat.getWhyPlayer() == Constants.LOSER_PLAYER):
        return game.getLoserPlayer()
    elif (strat.getWhyPlayer() == Constants.LOS_RAT_PLAYER):
        return game.getLosRatPlayer()
    elif (strat.getWhyPlayer() == Constants.ALL_PLAYER):
        return game.getAllPlayer()

# печать результатов
def printStrat(game, countPrint, curr_name_tournament, strat, text_split, count, prevStr):
    if (curr_name_tournament == Constants.ID_1 or curr_name_tournament == Constants.ID_2):
        return printTT_CUP(game, countPrint, curr_name_tournament, strat, text_split, count, prevStr = prevStr)
    elif (curr_name_tournament == Constants.ID_3 or curr_name_tournament == Constants.ID_4):
        return printLigaPro(game, countPrint, curr_name_tournament, strat, text_split, count, prevStr = prevStr)
    else:
        return "я не знаю что это"

def printCMD(game, strat):
    print(game.getFirstPlayer() + " Р/Г.Р./Т: " + game.getFirstRating() + " - " +
          game.getSecondPlayer() + " Р/Г.Р./Т: " + game.getSecondRating())
    print("Стратегия № " + str(strat.getCountStrat()) + " " + strat.getDescription())

def getStrAboutGame(listOfGame):
    if (len(listOfGame) == 0):
        return "Нет текущих игр, иди отдыхай"
    retStr = "Текущие игры:\n"
    gameCount = 0
    for game in listOfGame:
        retStr += str(gameCount + 1) + ") "
        retStr += Constants.getTournamentByID(game.id_tournament) + "\n"
        retStr += game.firstPlayer + " - " + game.secondPlayer + "\n"
        retStr += game.getRatingPlayersPrint()
        retStr += "Счёт: " + game.dirtyScore + "\n"
        gameCount += 1
    retStr += "Бомбить буков вздумал? :)"
    return retStr

def getStrAboutOneGame(game):
    retStr = "Началась игра \n"
    retStr += Constants.getTournamentByID(game.id_tournament) + "\n"
    retStr += game.firstPlayer + " - " + game.secondPlayer + "\n"
    retStr += game.getRatingPlayersPrint()
    retStr += "Счёт: " + game.dirtyScore + "\n"
    retStr += "Станут другими дела :)"
    return retStr
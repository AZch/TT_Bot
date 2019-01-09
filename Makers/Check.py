from Constants import Constants
from Makers import ParseGame


# Если игра завершилась
def checkTotalGameParse(printName, text_split, count, var):
    if (printName == True and var == "5" and len(var) == len("5") and
                    text_split[count - 1] != Constants.value_2 and
                    text_split[count - 1] == Constants.value_3):
        return True
    else:
        return False

# Если игра находится в режиме таймаута
def checkTimeoutGameParse(printName, text_split, count, var):
    if (printName == True and var == "5" and len(var) == len("5") and
                    text_split[count - 1] == Constants.value_2 and
                    text_split[count - 1] != Constants.value_3):
        return True
    else:
        return False

# Проверка текущего состояния парсинга строк для возможности проверить игру на наличие стратегий
def checkCurrectGameParse(printName, text_split, count, var):
    if (printName == True and var == "5" and len(var) == len("5") and
                    text_split[count - 1] != Constants.value_2 and
                    text_split[count - 1] != Constants.value_3):
        return True
    else:
        return False

# проверка игры на возможность её вывода
def checkGameToCheck(var, printName, curr_name_tournament):
    if (var == Constants.name_1 and len(var) >= len(Constants.name_1)):
        curr_name_tournament = Constants.ID_1
        printName = True
    elif (var == Constants.name_2 and len(var) >= len(Constants.name_1)):
        curr_name_tournament = Constants.ID_2
        printName = True
    elif (var == Constants.name_3 and len(var) >= len(Constants.name_1)):
        curr_name_tournament = Constants.ID_3
        printName = True
    elif (var == Constants.name_4 and len(var) >= len(Constants.name_1)):
        curr_name_tournament = Constants.ID_4
        printName = True
    else:
        if (var[0: len(Constants.name_event)] == Constants.name_event):
            printName = False
            curr_name_tournament = Constants.ID_NULL
    return printName, curr_name_tournament

# Проверка и опрделение рейтинга (diff 75)
def checkFavRating(whoFav, firstRating, secondRating):
    #if (firstRating.split('/')[0] == "Странный трабл(не в стату)" or secondRating.split('/')[0] == "Странный трабл(не в стату)"):
    #   return Constants.NOT_FAVARIT
    if (not ParseGame.isFloatStr(firstRating)):
        return Constants.NOT_FAVARIT
    sub = float(secondRating) - float(firstRating)
    if (sub > Constants.COUNT_FAVORITE_POINT and whoFav == 1):
        return Constants.FAVARIT
    elif (sub < -1 * Constants.COUNT_FAVORITE_POINT and whoFav == 2):
        return Constants.FAVARIT
    elif (sub < Constants.COUNT_FAVORITE_POINT and sub > -1 * Constants.COUNT_FAVORITE_POINT and abs(sub) <= Constants.EQUAL_GAME_FAV):
        return Constants.NOT_FAVARIT
    else:
        return Constants.LOSER_FAVARIT

def checkWin(whoWinFlag, scoreFirst, scoreSecond, count, WHAT_HAND):
    if (whoWinFlag == Constants.WHO_WIN_FIRST):
        if (scoreFirst > scoreSecond):
            return True
        else:
            return False
    if (whoWinFlag == Constants.WHO_WIN_SECOND):
        if (scoreFirst < scoreSecond):
            return True
        else:
            return False
    if (whoWinFlag == Constants.WHO_WIN_HAND_FIRST):
        if (WHAT_HAND == Constants.HAND_MORE):
            if (scoreFirst + count > scoreSecond):
                return True
            else:
                return False
        elif (WHAT_HAND == Constants.HAND_LESS):
            if (scoreFirst + count > scoreSecond):
                return True
            else:
                return False
    if (whoWinFlag == Constants.WHO_WIN_HAND_SECOND):
        if (WHAT_HAND == Constants.HAND_MORE):
            if (scoreSecond + count > scoreFirst):
                return True
            else:
                return False
        elif (WHAT_HAND == Constants.HAND_LESS):
            if (scoreSecond + count > scoreFirst):
                return True
            else:
                return False
    if (whoWinFlag == Constants.WHO_WIN_EQUAL):
        if (scoreFirst - scoreSecond == 0):
            return True
        else:
            return False
    if (whoWinFlag == Constants.WHO_WIN_TOTAL_U):
        if (scoreFirst + scoreSecond >= count):
            return True
        else:
            return False
    if (whoWinFlag == Constants.WHO_WIN_TOTAL_D):
        if (scoreFirst + scoreSecond <= count):
            return True
        else:
            return False
    return False
from Objects.Game import Game
from Objects.OneScore import OneScore
from Constants import Constants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from MainFile import mainWork
from Makers import Print
import  app


def ParseGame(players, dirtyScore, countStrat, id_tournament, coeffFirst, coeffSecond):
    tranlation_table_score = dict.fromkeys(map(ord, ':\(*—-)'), ' ')
    cleanScore = dirtyScore.translate(tranlation_table_score)

    tranlation_table_players = dict.fromkeys(map(ord, '-— '), ' ')
    twoPlayers = players.translate(tranlation_table_players)
    #print(twoPlayers)
    return Game(firstPlayer = twoPlayers.split()[0] + " " + twoPlayers.split()[1],
                secondPlayer = twoPlayers.split()[2] + " " + twoPlayers.split()[3],
                score = ParseScore(cleanScore.split()), countStrat=countStrat, id_tournament=id_tournament,
                dirtyScore=dirtyScore, coeffFirst = coeffFirst, coeffSecond = coeffSecond)

def ParseScore(cleanScore):
    listOfScore = []
    indexGame = 0
    i = 0
    while True:
        if (i + 1 >= len(cleanScore) or not isNumStr(cleanScore[i]) or not isNumStr(cleanScore[i + 1])):
            break
        listOfScore.append(OneScore(first = int(cleanScore[i]), second = int(cleanScore[i + 1]), whatSet = indexGame))
        indexGame += 1
        i += 2
    return listOfScore

def isNumStr(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def isFloatStr(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def findGame(listOfGame, game, driverScoreTT, driverScoreLigaPro, curr_name_tournament, isEnd):
    for oneExistGame in listOfGame:
        if (oneExistGame.getFirstPlayer() == game.getFirstPlayer() and oneExistGame.getSecondPlayer() == game.getSecondPlayer()):
            oneExistGame.setScore(game.getScore())
            oneExistGame.dirtyScore = game.dirtyScore
            if (isFloatStr(game.coeffFirst) and isFloatStr(game.coeffSecond)):
                if ((not isFloatStr(oneExistGame.coeffFirst) or not isFloatStr(oneExistGame.coeffSecond)) 
                    or (oneExistGame.coeffFirst == 0 and oneExistGame.coeffSecond == 0 and game.coeffFirst != 0 and game.coeffSecond != 0)):
                    oneExistGame.coeffFirst = game.coeffFirst
                    oneExistGame.coeffSecond = game.coeffSecond
                    #print(Print.getStrAboutOneGame(game=oneExistGame))
                    #send_message(chat_id=281265894, text=Print.getStrAboutOneGame(game=oneExistGame))
            #game.setIsUpdate(isUpdate = True)
            #listOfGame.insert(listOfGame.index(oneExistGame), game)
            #listOfGame.remove(oneExistGame)
            return listOfGame, oneExistGame
        #print(oneExistGame.getScore())
    #listOfGame.append(game)

    game.setRating(getRating(game.getFirstPlayer().split()[0], game.getFirstPlayer(),
                                       driverTT_CUP=driverScoreTT, driverLigaPro=driverScoreLigaPro,
                                       idTournament=curr_name_tournament),
                   getRating(game.getSecondPlayer().split()[0],
                                       game.getSecondPlayer(),
                                       driverTT_CUP=driverScoreTT,
                                       driverLigaPro=driverScoreLigaPro,
                                       idTournament=curr_name_tournament))
    
    if (not isEnd):
        #print(Print.getStrAboutOneGame(game=game))
        listOfGame.append(game)
        #send_message(chat_id=281265894, text=Print.getStrAboutOneGame(game=game))
    return listOfGame, game

def getRatingTT_Cup(name, fullName, driver):
    driver.get(Constants.TT_CUP_LINK)
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "id_player_search_input"))
    )
    element.send_keys(Keys.TAB)
    element.send_keys(str(name))
    element.send_keys(Keys.ENTER)

    elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "content"))
    )
    text = elements.text
    text_split = text.split(Constants.SPLIT_TT_CUP_GET_PLAYERS)

    text_split = text_split[1].split("\n")
    this_people = False
    retStr = '0/0/0/0'

    for var in text_split:
        if (this_people and var[0:len(Constants.TT_CUP_RATING_WORD)] == Constants.TT_CUP_RATING_WORD):
            retStr = var.split(Constants.SPLIT_TT_DATA_ABOUT_PLAYER)[1][1:]
        if (this_people and var[0:len(Constants.TT_CUP_DATE_OF_BIRTH_WORD)] == Constants.TT_CUP_DATE_OF_BIRTH_WORD):
            retStr += "/" + var.split(Constants.SPLIT_TT_DATA_ABOUT_PLAYER)[1][1:]
        if (this_people and var[0:len(Constants.TT_CUP_TOURNAMENTS_WORD)] == Constants.TT_CUP_TOURNAMENTS_WORD):
            retStr += "/" + var.split(Constants.SPLIT_TT_DATA_ABOUT_PLAYER)[1][1:]
            return getRatingUKR_TT_CUP(fullName, driver) + '/' + retStr

        if (var[0:len(fullName)] == fullName.upper()):
            this_people = True

    return retStr

def getRatingUKR_TT_CUP(fullName, driver):
    elements = WebDriverWait(driver, 15).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "player-name"))
    )
    for oneElem in elements:
        if (oneElem.text[0:len(fullName)] == fullName.upper()):
            oneElem.click()
            break
    elements = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "content"))
    )
    text = elements.text
    try:
        text_split = text.split(Constants.SPLIT_TT_CUP_GET_PLAYERS_RAT_UKR)
        text_split = text_split[1].split("\n")
    except Exception:
        print ("опять")
        return 'всё ещё странно'
    this_people = False

    for var in text_split:
        if (this_people and var[0:len(Constants.TT_CUP_RATING_WORD_UKR)] == Constants.TT_CUP_RATING_WORD_UKR):
            return var.split(Constants.SPLIT_TT_DATA_ABOUT_PLAYER)[1][1:]

        if (var[0:len(fullName)] == fullName.upper()):
            this_people = True
    return '0'

def getRationLigaPro(firstName, secondName, driver):
    UrlLigaProRes = Constants.MAIN_URL_LIGA_PRO + firstName
    if (secondName != ""):
        UrlLigaProRes += Constants.SPACE_URL_LIGA_PRO + secondName
    driver.get(UrlLigaProRes + Constants.END_URL_LIGA_PRO)
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bordered-table"))
    )
    text = element.text
    textSplit = text.split("\n")
    thisPeopleFName = False
    thisPeopleSName = False
    for var in textSplit[1:]:
        words = var.split()
        countWord = 0
        for word in words[1:]:
            countWord += 1
            if (thisPeopleFName and thisPeopleSName and len(word.split('.')) == 3):
                return words[countWord - 1]
            if (thisPeopleFName and thisPeopleSName):
                continue
            if (thisPeopleFName and word.upper()[0:len(secondName)] == secondName):
                thisPeopleSName = True
                continue
            if (word.upper() == firstName.upper()):
                thisPeopleFName = True
                continue
            elif (not thisPeopleFName):
                break

    return '0/0/0/0'

def getRating(name, sOrfName, driverTT_CUP, driverLigaPro, idTournament):
    if (idTournament == Constants.ID_1 or idTournament == Constants.ID_2):
        return getRatingTT_Cup(name, sOrfName, driver = driverTT_CUP)
    elif (idTournament == Constants.ID_3 or idTournament == Constants.ID_4):
        return getRationLigaPro(name, sOrfName.split()[1], driver = driverLigaPro) + "/0/0/0"
    else:
        return '0/0/0/0'

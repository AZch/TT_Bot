from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Constants import Constants
from Makers import Loads, Check, ParseGame, Print
from datetime import datetime
import time
from pyvirtualdisplay import Display
#from app import send_message
import app
from Objects.Game import Game
from Objects.SendEvent import SendEvent
from Objects.DelGame import DelGame
import requests

proxies = {'http': 'https://telegram:telegram@lzpaq.tgproxy.me:443', 'https': 'https://telegram:telegram@lzpaq.tgproxy.me:443'}
token = '684761241:AAHanKSvHWV81b00IgAV3HKws9PTQbL7JnA'
URL = 'https://api.telegram.org/bot' + token + '/'
hand = 3.5

def send_message(chat_id, text):
    # https://api.telegram.org/bot503945314:AAqMC9y0tRho/sendMessage
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    req = requests.post(url, json = answer)
    return req.json()

def makeFind(driver, stop, listOfGame, driverScoreTT, driverScoreLigaPro, que, display, listOfMemberShort, listOfMemberStrat, listOfMemberAll):
    countPrint = 19
    isSend = False
    #send_message(chat_id=281265894, text="im start work") # i'm
    isSendPr = False
    listOfSendEvent = []
    listOfDelGame = []
    countWin = 15
    countLose = 3
    while True:
        #time.sleep(1)
        #f = requests.get("https://1xstavka.ru/live/Football/118737-Japan-J-League/167448762-Vissel-Kobe-Yokohama-F-Marinos/")
        #print (f.content)live-list__championship-event

        try:
            isSendPr = False
            try:
                elements = WebDriverWait(driver, 30).until(
                    EC.visibility_of_all_elements_located((By.XPATH, "//div[(@class='live-list__championship-event ' or @class='live-list__championship-event') and not(ancestor::div[contains(@style,'display: none;')])]"))# or "//div[@class='live-list__championship-header' and not(ancestor::div[contains(@style,'display: none;')])]"))
                )
                #driver.find_elements_by_xpath("//span[@class='stat_wrapper']//a[@class='stat sprite-blue']")
                links = []
                links = WebDriverWait(driver, 30).until(  # live-list__championship
                                    EC.visibility_of_all_elements_located((By.XPATH,
                                                                             "//a[@class='stat sprite-blue' and not(ancestor::div[contains(@style,'display: none;')])]"))
                                )
            except:
                driver.get("https://betcity.ru/ru/live/table-tennis")
                continue
            countLink = 0
            for element in elements:

                #if (len(links) != len(elements)):
                #    a = 5

                isDrop = False
                text = element.text
                textSplit = text.split('\n')
                if (len(textSplit) > 0): #and (textSplit[0] == 'Настольный теннис. Мужчины. Лига Про.' or textSplit[0] == 'Настольный теннис. Мужчины. TT-Cup.')):
                    #gameStr = getGameStr(textSplit)
                    currGame = parseSimpleGame(textSplit=textSplit)
                    isAdd = False
                    if (not checkEndGame(text) or (currGame.score[0] != 3 and currGame.score[1] != 3)):
                        countLink += 1
                        isAdd = True
                    if (not isAdd and (not checkEndGame(text) or (currGame.score[0] != 4 and currGame.score[1] != 4 and not checkFiveSets(text)))):
                        countLink += 1
                        continue

                    if (checkEndScore(currGame.score)):
                        for event in listOfSendEvent:
                            if (event.nameF == currGame.players[0] and event.nameS == currGame.players[1]):
                                if (event.isScore):
                                    aboutStr = ""
                                    if (event.dirty):
                                        print()
                                        if (getLastSetCheck(text, event.whyPlayer, hand=hand)):
                                            countWin += 1
                                            aboutStr = " + "
                                        else:
                                            countLose += 1
                                            aboutStr = " - "
                                    elif (not event.dirty):
                                        if (currGame.score[0] == 3 or currGame.score[1] == 3):
                                            countWin += 1
                                            aboutStr = " + "
                                        else:
                                            countLose += 1
                                            aboutStr = " - "
                                    strSend = "#TT" + str(event.countPrint) + aboutStr  + str(countWin) + "+ " + str(countLose) + "-"
                                    #send_message(chat_id=281265894, text=str(countWin) + "+ " + str(countLose) + "-")
                                    #send_message(chat_id=319201172, text=str(countWin) + "+ " + str(countLose) + "-")
                                    #send_message(chat_id=270749872, text=str(countWin) + "+ " + str(countLose) + "-")
                                    #send_message(chat_id=607415198, text=str(countWin) + "+ " + str(countLose) + "-")
                                    sendGame(strToPrint=strSend, listOfMember=listOfMemberStrat)
                                    sendGame(strToPrint=strSend, listOfMember=listOfMemberAll)
                                    sendGame(strToPrint=strSend, listOfMember=listOfMemberShort)


                                listOfSendEvent.remove(event)
                                break
                        for game in listOfGame:
                            if (game.players[0] == currGame.players[0] and game.players[1] == currGame.players[1]):
                                # if (currGame.score[0] + currGame.score[1] == 3):
                                #     countWin += 1
                                # else:
                                #     countLose += 1
                                listOfGame.remove(game)
                                break
                    else:
                        findGame = False
                        if (currGame.score[0] + currGame.score[1] == 2 and (currGame.score[0] == 2 or currGame.score[1] == 2)):
                            stopFind = False
                            for event in listOfSendEvent:
                                if (event.nameF == currGame.players[0] and event.nameS == currGame.players[1]):
                                    stopFind = True
                                    break
                            if (stopFind):
                                continue
                            for game in listOfGame:
                                if (game.players[0] == currGame.players[0] and game.players[1] == currGame.players[1]):
                                    findGame = True
                                    checkStrat = True
                                    # for meet in game.meet:
                                    #     meetSplit = meet.split(' ')
                                    #     meetMonth = meetSplit[0].split('.')[1]
                                    #     meetYear = meetSplit[0].split('.')[2]
                                        #if (not checkMeetData(int(meetMonth), int(meetYear), int(game.monthNow), int(game.yearNow) - 2000)):
                                        #    checkStrat = False
                                        #    break
                                    if (checkStrat and len(game.meet) >= 3):
                                        strPrint, dirty, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond, game, whyPlayer = checkMeet(
                                            game.players, game.meet, getPlayerWin(currGame.score), game.yearNow,
                                            game.monthNow, game=game)
                                        strSend = "(чистые победы/грязные победы/процент выигрышных партий)\n"
                                        statFirst = "(" + str(firstEmptyWin) + "/" + str(firstDirtyWin) + "/" + str(percentWinFirst * 100) + "%)"
                                        statSecond = "(" + str(secondEmptyWin) + "/" + str(secondDirtyWin) + "/" + str(percentWinSecond * 100) + "%)"
                                        corrStrOne = ""
                                        corrStrTwo = ""
                                        countOneSpace = 0
                                        countTwoSpace = 0
                                        # if (len(game.players[0]) > len(statFirst)):
                                        #     countTwoSpace = len(game.players[0]) - len(statFirst)
                                        # else:
                                        #     countOneSpace = len(statFirst) - len(game.players[0])
                                        # while (countOneSpace > 0):
                                        #     corrStrOne += " "
                                        #     countOneSpace -= 1
                                        # while (countTwoSpace > 0):
                                        #     corrStrTwo += " "
                                        #     countTwoSpace -= 1
                                        strSend += game.players[0] + corrStrOne + " - " + game.players[1] + "\n"
                                        strSend += statFirst + corrStrTwo + " - " + statSecond + "\n"
                                        strSend += str(currGame.score[0]) + " : " + str(currGame.score[1]) + "\n"

                                        #strAboutWin = "чистые/грязные победы:\n" + "1. " + str(firstEmptyWin) + "/" + str(firstDirtyWin) + "\n2. " + str(secondEmptyWin) + "/" + str(secondDirtyWin) + "\n"

                                        strMeet = ""
                                        for meet in game.meet:
                                            strMeet += meet + "\n"
                                        if (strPrint != 'net'):
                                            strCountSend = "#TT" + str(countPrint) + " "
                                            strSimpleSend =strCountSend +  game.players[0] + corrStrOne + " - " + game.players[1] + "\n" + strPrint
                                            strSend += strPrint + "\n"
                                            strSend = strCountSend + strSend
                                            #send_message(chat_id=270749872, text=strSimpleSend)
                                            #send_message(chat_id=607415198, text=strSimpleSend)
                                            sendGame(strToPrint=strSimpleSend, listOfMember=listOfMemberShort)

                                            strSend += strMeet
                                            listOfSendEvent.append(
                                                SendEvent(game.players[0], game.players[1], dirty=dirty, isScore=True, whyPlayer = whyPlayer, countPrint = countPrint))
                                            sendGame(strToPrint=strSend, listOfMember=listOfMemberStrat)
                                            sendGame(strToPrint=strSend, listOfMember=listOfMemberAll)
                                            countPrint += 1
                                            #send_message(chat_id=281265894, text= strSend)
                                            #send_message(chat_id=319201172, text= strSend)
                                        else:
                                            strSend += strMeet
                                            listOfSendEvent.append(
                                                SendEvent(game.players[0], game.players[1], dirty=dirty, isScore=False, whyPlayer = whyPlayer, countPrint = 0))
                                            game, currGame, listOfSendEvent = sendInfoNotStrat(game, currGame, listOfSendEvent, strSend, listOfMemberAll)
                                        break
                                    #else:
                                     #   game, currGame, listOfSendEvent = sendInfoNotStrat(game, currGame,
                                     #                                                      listOfSendEvent, "soon\n")


                        if (not findGame):
                            for game in listOfGame:
                                if (game.players[0] == currGame.players[0] and game.players[1] == currGame.players[1]):
                                    findGame = True
                                    break

                        if (not findGame):
                            newGame, isAdd = parseGame(textSplit=textSplit, count=countLink - 1, links=links,
                                driverAboutPlayers=driverScoreTT, game=currGame)
                            if (isAdd):
                                listOfGame.append(newGame)


        except Exception as err:
            if (not isSendPr):
                #print("problem main")
                #send_message(chat_id=281265894, text=str(err))
                driver.get("https://betcity.ru/ru/live/table-tennis")
                print(err)
                isSendPr = True
        #else:
        #    makeFind(driver, stop, listOfStrat, newListOfGame, driverScoreTT

#def getGameStr()
def checkFiveSets(text):
    if (text.rfind("5 sets") == -1):
        return False
    else:
        return True


def checkEndGame(text):
    if (text.rfind("Прием пари окончен") == -1):
        return False
    else:
        print("Прием пари окончен")
        return True

def sendInfoNotStrat(game, currGame, listOfSendEvent, strSend, listOfMemberAll):
    sendGame(strToPrint=strSend, listOfMember=listOfMemberAll)
    return game, currGame, listOfSendEvent

def getPlayerWin(score):
    if (score[0] > score[1]):
        return 0
    else:
        return 1

def checkMeetData(monthMeet, yearMeet, monthNow, yearNow):
    if (yearMeet < yearNow):
        yearMeet += 1
        monthMeet = -12 + monthMeet - 1 - monthNow
    while (yearMeet < yearNow):
        yearMeet += 1
        monthMeet -= 12
    if (monthNow - monthMeet <= 6):
        return True
    else:
        return False

def checkMeet(players, meeting, winPlayersIndex, yearNow, monthNow, game):
    firstEmptyWin = 0
    firstDirtyWin = 0
    secondEmptyWin = 0
    secondDirtyWin = 0
    countMeetFive = 0
    percentWinFirst = 0.0
    percentWinSecond = 0.0
    newMeet = []
    for meet in meeting:
        meetSplit = meet.split(' ')
        count = 2
        meetFirst = meetSplit[1]
        meetSecond = ""
        while meetSplit[count] != '-':
            meetFirst += " " + meetSplit[count]
            count += 1
        count += 1
        meetSecond += meetSplit[count]
        count += 1
        while (len(meetSplit) > count and not ParseGame.isNumStr(meetSplit[count].split(':')[0])):
            meetSecond += ' ' + meetSplit[count]
            count += 1
        try :
            meetScoreFirst = int(meetSplit[count].split(':')[0])
            meetScoreSecond = int(meetSplit[count].split(':')[1])
        except:
            return "net", False, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond
        if (meetScoreFirst == 3):
            if (meetScoreSecond == 0):
                if (players[0] == meetFirst):
                    firstEmptyWin += 1
                    newMeet.append(meetSplit[0] + " | " + str(meetScoreFirst) + ":" + str(meetScoreSecond))
                else:
                    secondEmptyWin += 1
                    newMeet.append(meetSplit[0] + " | " + str(meetScoreSecond) + ":" + str(meetScoreFirst))
            else:
                if (players[0] == meetFirst):
                    firstDirtyWin += 1
                    newMeet.append(meetSplit[0] + " | " + str(meetScoreFirst) + ":" + str(meetScoreSecond))
                else:
                    secondDirtyWin += 1
                    newMeet.append(meetSplit[0] + " | " + str(meetScoreSecond) + ":" + str(meetScoreFirst))
        elif (meetScoreSecond == 3):
            if (meetScoreFirst == 0):
                if (players[0] == meetFirst):
                    secondEmptyWin += 1
                    newMeet.append(meetSplit[0] + " | " + str(meetScoreFirst) + ":" + str(meetScoreSecond))
                else:
                    firstEmptyWin += 1
                    newMeet.append(meetSplit[0] + " | " + str(meetScoreSecond) + ":" + str(meetScoreFirst))
            else:
                if (players[0] == meetFirst):
                    secondDirtyWin += 1
                    newMeet.append(meetSplit[0] + " | " + str(meetScoreFirst) + ":" + str(meetScoreSecond))
                else:
                    firstDirtyWin += 1
                    newMeet.append(meetSplit[0] + " | " + str(meetScoreSecond) + ":" + str(meetScoreFirst))
        countMeetFive += 1
        if (countMeetFive == 5):
            #percentWinFirst = float(firstEmptyWin + firstDirtyWin) / (firstDirtyWin + firstEmptyWin + secondDirtyWin + secondEmptyWin)
            #percentWinSecond = float(secondEmptyWin + secondDirtyWin) / (firstDirtyWin + firstEmptyWin + secondDirtyWin + secondEmptyWin)
            break
    percentWinFirst = float(firstEmptyWin + firstDirtyWin) / (firstDirtyWin + firstEmptyWin + secondDirtyWin + secondEmptyWin)
    percentWinSecond = float(secondEmptyWin + secondDirtyWin) / (firstDirtyWin + firstEmptyWin + secondDirtyWin + secondEmptyWin)
    game.meet = newMeet
    # try:
    #     percentFirstEmpty = float(firstEmptyWin) / (firstEmptyWin + firstDirtyWin)
    # except:
    #     percentFirstEmpty = 0.0
    # try:
    #     percentFirstDirty = float(firstDirtyWin) / (firstEmptyWin + firstDirtyWin)
    # except:
    #     percentFirstDirty = 0.0
    # try:
    #     percentSecondEmpty = float(secondEmptyWin) / (secondEmptyWin + secondDirtyWin)
    # except:
    #     percentSecondEmpty = 0.0
    # try:
    #     percentSecondDirty = float(secondDirtyWin) / (secondEmptyWin + secondDirtyWin)
    # except:
    #     percentSecondDirty = 0.0
    if (winPlayersIndex == 0):
        if (firstEmptyWin >= 3 and percentWinFirst >= 0.8):
            return "3 сет П" + str(1), False, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond, game, 0
        elif ((firstDirtyWin + secondDirtyWin >= 4 and percentWinFirst >= 0.8)):
            return "3 сет Ф" + str(hand) + " " + str(2), True, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond, game, 1
        elif (firstDirtyWin + secondDirtyWin >= 5):
            return "тест\n3 сет Ф" + str(hand) + " " + str(2), True, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond, game, 1
    elif (winPlayersIndex == 1):
        if (secondEmptyWin >= 3 and percentWinSecond >= 0.8):
            return "3 сет П" + str(2), False, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond, game, 1
        elif (secondDirtyWin + firstDirtyWin >= 4 and percentWinSecond >= 0.8):
            return "3 сет Ф" + str(hand) + " " + str(1), True, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond, game, 0
        elif  (firstDirtyWin + secondDirtyWin >= 5):
            return "тест\n3 сет Ф" + str(hand) + " " + str(1), True, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond, game, 0
    return "net", False, firstEmptyWin, firstDirtyWin, secondEmptyWin, secondDirtyWin, percentWinFirst, percentWinSecond, game, 0

def getLastSetCheck(text, whyPlayer, hand):
    try:
        textSplit = text.replace('(', ')').replace('\n', '').split(')')
        scores = textSplit[1].split(', ')
        toCheck = 0.0
        if (scores[-1].split(':')[0] == '0' and scores[-1].split(':')[1] == '0'):
            toCheck = int(scores[-2].split(':')[0]) - int(scores[-2].split(':')[1])
        else:
            toCheck = int(scores[-1].split(':')[0]) - int(scores[-1].split(':')[1])
        if (whyPlayer == 0):
            if (toCheck > 0):
                return True
            elif (toCheck + hand > 0):
                return True
            else:
                return False
        else:
            if (toCheck < 0):
                return True
            elif (toCheck - hand < 0):
                return True
            else:
                return False

    except:
        return False

def checkEndScore(score):
    return len(score) > 1 and (score[0] + score[1] == 3)

def getScore(textSplit):
    score = []
    if (textSplit[1] == '•' or textSplit[3] == '•'):
        score.append(int(textSplit[4].split(':')[0]))
        score.append(int(textSplit[4].split(':')[1]))
    else:
        score.append(int(textSplit[3].split(':')[0]))
        score.append(int(textSplit[3].split(':')[1]))
    return score

def parseGame(textSplit, links, count, driverAboutPlayers, game):
    if (textSplit[1] == '•'):
        firstPlayer = textSplit[2]
        secondPlayer = textSplit[3]
    else:
        firstPlayer = textSplit[1]
        secondPlayer = textSplit[2]
    players = []
    players.append(firstPlayer)
    players.append(secondPlayer)

    driverAboutPlayers.get(str(links[count].get_attribute('href')))
    element = WebDriverWait(driverAboutPlayers, 30).until(
                    EC.visibility_of_element_located((By.CLASS_NAME,'mstat__content' ))
            ) 
    meet, isAdd = getMeetFivePlayer(element.text.split('\n'), game=game)

    return Game(textSplit[0], players, getScore(textSplit), meet), isAdd

def parseSimpleGame(textSplit):
    if (textSplit[1] == '•'):
        firstPlayer = textSplit[2]
        secondPlayer = textSplit[3]
    else:
        firstPlayer = textSplit[1]
        secondPlayer = textSplit[2]
    players = []
    players.append(firstPlayer)
    players.append(secondPlayer)
    return Game('', players, getScore(textSplit), [])

def getMeetFivePlayer(textSplit, game):
    read = False
    countMeet = 0
    firstCheck = True
    meet = []
    for var in textSplit:
        if (read and ParseGame.isNumStr(var.split('.')[0])):
            meetSplit = var.split(' ')
            if (firstCheck):
                firstCheck = False
                count = 2
                meetFirst = meetSplit[1]
                while meetSplit[count] != '-':
                    meetFirst += " " + meetSplit[count]
                    count += 1
                if (not (game.players[0] == meetFirst or game.players[1] == meetFirst)):
                    return meet, False

            meetMonth = meetSplit[0].split('.')[1]
            meetYear = meetSplit[0].split('.')[2]
            if (checkMeetData(int(meetMonth), int(meetYear), int(game.monthNow), int(game.yearNow) - 2000)):
                meet.append(var)
                countMeet += 1
                if (countMeet == 5):
                    break
            else:
                return meet, True
        if (var == 'ОЧНЫЕ ВСТРЕЧИ:'):
            read = True
    return meet, True

# param - list
# 0, 1 - угловые (0)
# 2, 3 - пенальти (1)
# 4, 5 - жёлтые карточки (2)
# 6, 7 - красные карточки (3)
# 8, 9 - Атаки (4)
# 10, 11 - опасные атаки (5)
# 12, 13 - % владение мячом (6)
# 14, 15 - удары в створ (7)
# 16, 17 - удары в сторону ворот (8)
def checkGame(param, whatMore, minute):
    whyTeam = -1
    if (len(param) >= 18):
        if (ParseGame.isNumStr(param[10]) and ParseGame.isNumStr(param[11]) and
                ParseGame.isNumStr(param[8]) and ParseGame.isNumStr(param[9])):
            winParam = []
            loseParam = []
            if (int(param[10]) >= int(param[11]) * whatMore):
                winParam = setLeftParam(param=param)
                loseParam = setRightParam(param=param)
                whyTeam = 2
            elif (whatMore * int(param[10]) <= int(param[11])):
                winParam = setRightParam(param=param)
                loseParam = setLeftParam(param=param)
                whyTeam = 1
            else:
                return False, whyTeam
            if (ParseGame.isNumStr(loseParam[5]) and ParseGame.isNumStr(minute)):
                if (float(loseParam[5]) <= float(minute) / 5 and float(loseParam[4]) <= float(minute) / 2):
                    if (ParseGame.isNumStr(loseParam[4]) and ParseGame.isNumStr(winParam[4])):
                        if (int(loseParam[4]) < int(winParam[4])):
                            if (ParseGame.isNumStr(loseParam[6]) and ParseGame.isNumStr(winParam[6])):
                                if (int(winParam[6]) - int(loseParam[6]) < 10):
                                    return False, whyTeam
                            if (ParseGame.isNumStr(loseParam[0]) and ParseGame.isNumStr(winParam[0])):
                                if (int(loseParam[0]) > int(winParam[0])):
                                    return False, whyTeam
                            if (ParseGame.isNumStr(loseParam[7]) and ParseGame.isNumStr(winParam[7])):
                                if (int(loseParam[7]) > 1 and int(loseParam[7]) > int(winParam[7])):
                                    return False, whyTeam
                            if (ParseGame.isNumStr(loseParam[8]) and ParseGame.isNumStr(winParam[8])):
                                if (int(loseParam[8]) > 1 and int(loseParam[8]) > int(winParam[8])):
                                    return False, whyTeam
                            return True, whyTeam

    return False, whyTeam

def getScores(textSplit):
    countNum = 0
    countStartNum = 0
    startCounting = False
    for var in textSplit:
        if (ParseGame.isNumStr(var)):
            if (not startCounting):
                countStartNum = countNum
            startCounting = True
        elif (startCounting):
            break
        countNum += 1

    scoresEnd = []
    if (ParseGame.isNumStr(textSplit[countStartNum]) and
            ParseGame.isNumStr(textSplit[countStartNum + (countNum - countStartNum) / 2])):
        scoresEnd.append(int(textSplit[countStartNum]))
        scoresEnd.append(int(textSplit[countStartNum + (countNum - countStartNum) / 2]))
    else:
        scoresEnd.append(-1)
        scoresEnd.append(-1)
    return scoresEnd






def setLeftParam(param):
    leftParam = []
    for i in range(9):
        leftParam.append(param[i * 2])
    return leftParam

def setRightParam(param):
    rightParam = []
    for i in range(9):
        rightParam.append(param[i * 2 + 1])
    return rightParam

def setLastCoeff(text_split, count, game):
    countLastCoeff = 2
    if (text_split[count + 2].split()[1] == "сет"):
        countLastCoeff = count + 4
    elif (len(text_split[count + 5].split()) < 2):
        countLastCoeff = count + 6
    else:
        countLastCoeff = count + 5
    check = text_split[countLastCoeff]
    if (len(text_split[countLastCoeff].split()) > 0):
        coeffStr = text_split[countLastCoeff]
        game.lastCoefFirst = coeffStr.split()[0]
        game.lastCoefSecond = coeffStr.split()[1]
    return game

def sendGame(strToPrint, listOfMember):
    print("send game")
    #try:
    for chat_id in listOfMember:
        send_message(chat_id=chat_id, text=strToPrint)
    #except:
        #print(problemSend + " " + listOfMember)
    #while thread.is_alive():
        #strToPrint = qe.get()
    print(strToPrint)

#if __name__ == '__main__':
def initFind(que, listOfGame, listOfMemberShort, listOfMemberStrat, listOfMemberAll):

    driver, driverScoreLigaPro, driverScoreTT_Cup, display = Loads.loadDrivers(webdriver=webdriver)

   
    makeFind(driver=driver, stop=False, listOfGame=listOfGame,
             driverScoreTT=driverScoreLigaPro, driverScoreLigaPro=driverScoreLigaPro, que=que, display=display,
             listOfMemberShort=listOfMemberShort, listOfMemberStrat=listOfMemberStrat, listOfMemberAll=listOfMemberAll)
    pass
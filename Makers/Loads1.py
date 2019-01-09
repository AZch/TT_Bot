from Objects.Strategic import StrategicTableTennis
from Constants import Constants


def loadStrat():
    listOfStrat = []
    oneStrat = StrategicTableTennis(description=" победа в 3м сете", countStrat=1, sets="12",
                                    scoreCheck="6", isMore=True, isEverySet=False, isCheckSet=False,
                                    isOneWin=True, whatGame=Constants.GAME_TT,
                                    isFavorite=Constants.FAVARIT, whyPlayer=Constants.WIN_PLAYER)
    listOfStrat.append(oneStrat)

    threeStrat = StrategicTableTennis(description=" победа во 2м сете", countStrat=3, sets="1",
                                      scoreCheck="6", isMore=True, isEverySet=True, isCheckSet=False,
                                      isOneWin=True, whatGame=Constants.GAME_TT,
                                      isFavorite=Constants.FAVARIT, whyPlayer=Constants.WIN_PLAYER)
    listOfStrat.append(threeStrat)

    fiveStart = StrategicTableTennis(description=" фора +3.5 в 4ом сете", countStrat=5, sets="123",
                                     scoreCheck="3", isMore=False, isEverySet=True, isCheckSet=False,
                                     isOneWin=False, whatGame=Constants.GAME_TT,
                                     isFavorite=Constants.NOT_FAVARIT, whyPlayer=Constants.NOT_PLAYER)
    listOfStrat.append(fiveStart)
    sixStart = StrategicTableTennis(description="5 сет тб 17.5 (крайний случай 18.5)", countStrat=6, sets="1234",
                                    scoreCheck="3", isMore=False, isEverySet=True, isCheckSet=False,
                                    isOneWin=False, whatGame=Constants.GAME_TT,
                                    isFavorite=Constants.NOT_FAVARIT, whyPlayer=Constants.NOT_PLAYER)
    listOfStrat.append(sixStart)
    return listOfStrat

def loadCombinationStratOr():
    listOfCombinationStrat = []
    # 1
    listOfStrat = []
    twoOneStrat = StrategicTableTennis(description=" фора +4.5 в 3м сете", countStrat=21, sets="12",
                                       scoreCheck="5", isMore=False, isEverySet=False, isCheckSet=False,
                                       isOneWin=True, whatGame=Constants.GAME_TT,
                                       isFavorite=Constants.LOSER_FAVARIT, whyPlayer=Constants.LOSER_PLAYER)
    listOfStrat.append(twoOneStrat)
    twoStrat = StrategicTableTennis(description=" фора +4.5 в 3м сете", countStrat=2, sets="12",
                                    scoreCheck="5", isMore=False, isEverySet=False, isCheckSet=False,
                                    isOneWin=True, whatGame=Constants.GAME_TT,
                                    isFavorite=Constants.NOT_FAVARIT, whyPlayer=Constants.LOSER_PLAYER)
    listOfStrat.append(twoStrat)
    listOfCombinationStrat.append(listOfStrat)

    # 2
    listOfStrat = []
    fourDopStart = StrategicTableTennis(description=" победа в 5", countStrat=41, sets="1234",
                                        scoreCheck="34", isMore=True, isEverySet=True, isCheckSet=True,
                                        isOneWin=False, whatGame=Constants.GAME_TT,
                                        isFavorite=Constants.FAVARIT, whyPlayer=Constants.FAV_PLAYER)
    listOfStrat.append(fourDopStart)
    fourStart = StrategicTableTennis(description=" победа в 5", countStrat=4, sets="1234",
                                     scoreCheck="1", isMore=True, isEverySet=True, isCheckSet=True,
                                     isOneWin=False, whatGame=Constants.GAME_TT,
                                     isFavorite=Constants.FAVARIT, whyPlayer=Constants.FAV_PLAYER)
    listOfStrat.append(fourStart)

    listOfCombinationStrat.append(listOfStrat)

    return listOfCombinationStrat


def loadDrivers(webdriver):
    driver = webdriver.Chrome(Constants.CHROME_BROWSER_DRIVER)
    driver.get(Constants.FONBET_TABLE_TENNIS_LINK)

    driverScoreTT_Cup = webdriver.Chrome(Constants.CHROME_BROWSER_DRIVER)

    driverScoreLigaPro = webdriver.Chrome("C:\\Users\\anton\\Desktop\\chromedriver.exe")

    return driver, driverScoreLigaPro, driverScoreTT_Cup
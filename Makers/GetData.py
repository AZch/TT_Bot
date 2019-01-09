import pymysql
from Objects.Strategic import StrategicTableTennis

def getSimpleStrat(conn):
    #cursor = conn.cursor()
    #cursor.execute(
    #    "SELECT id, description, countStrat, setsGame, scoreCheck, isMore, isEverySet, isCheckSet,"
    #    "   isOneWin, whatGame, isFavorite, whyPlayer, howWin, endScoreCheck, endSet, winGame, loseGame, "
    #    "   from Strat where idNextStrat = 0"
    #)
    #listOfStrat = []
    #if cursor.rowcount > 0:
    #    for row in cursor.fetchall():
    #        listOfStrat.append(StrategicTableTennis(description=row[1], countStrat=row[2], sets=row[3]))
    #return 0
    pass

def getOrStrat():
    pass

def getAndStrat():
    pass

def getUsers():
    pass

def getUser():
    pass

def getPercentStratPlayer(conn, plId, stratId):
    #cursor = conn.cursor()
    #cursor.execute(
    #    "SELECT plStrat.winStrat, plStrat.loseStrat from Player pl, PlayerStrat plStrat, Strat strat where pl.id = plStrat.idPlayer"
    #    "   and plStrat.idStrat = strat.id and pl.id = '%d' and strat.id = '%d';" % (plId, stratId)
    #)
    #if cursor.rowcount > 0:
    #    for row in cursor.fetchall():
    #        return row[0] * 100 / (row[0] + row[1])
    #return 0
    pass
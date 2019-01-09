name_1 = "НАСТ. ТЕННИС. TT-CUP. УКРАИНА"
name_2 = "НАСТ. ТЕННИС. ЖЕ. TT-CUP. УКРАИНА"
name_3 = "НАСТ. ТЕННИС. ЛИГА ПРО. МОСКВА"
name_4 = "НАСТ. ТЕННИС. ЖЕ. ЛИГА ПРО. МОСКВА"
name_event = "НАСТ. ТЕННИС."
name_not_god_tournament = "Не наш выбор"
ID_NULL = 0
ID_1 = 1
ID_2 = 2
ID_3 = 3
ID_4 = 4

WHO_WIN_FIRST = 1
WHO_WIN_SECOND = 2
WHO_WIN_HAND_FIRST = 3
WHO_WIN_HAND_SECOND = 4
WHO_WIN_TOTAL_U = 5
WHO_WIN_TOTAL_D = 6
WHO_WIN_EQUAL = 7
WHO_WIN_DONTSTRAT = -1

HOW_GAME_TOTAL_U = 0
HOW_GAME_TOTAL_D = 1
HOW_GAME_WIN = 2
HOW_GAME_HAND = 3

GAME_NOT_END = 0
GAME_WIN = 1
GAME_LOSE = 2

HAND_MORE = 1
HAND_LESS = 2

COUNT_FAVORITE_POINT = 0.4
EQUAL_GAME_FAV = 0.11

MIN_YEAR = 20

value_1 = "Тотал"
value_2 = 'ТАЙМАУТ'
value_3 = 'ИТОГ'

WIN_PLAYER = 0
LOSER_PLAYER = 1
ALL_PLAYER = 2
NOT_PLAYER = 3
FAV_PLAYER = 4
LOS_RAT_PLAYER = 5

FAVARIT = 0
NOT_FAVARIT = 1
LOSER_FAVARIT = 2
LOSER_RATING = 3

GAME_TT = "наст. теннис."

TT_CUP_TOURNAMENTS_WORD = "турниры:"
TT_CUP_DATE_OF_BIRTH_WORD = "год рождения:"
TT_CUP_RATING_WORD = "рейтинг:"
TT_CUP_RATING_WORD_UKR = "Рейтинг Украины:"

SPLIT_TT_DATA_ABOUT_PLAYER = ':'
SPLIT_TT_CUP_GET_PLAYERS = "\nИГРОКИ\n"
SPLIT_TT_CUP_GET_PLAYERS_RAT_UKR = "\nПЕРСОНАЛЬНАЯ СТРАНИЦА ИГРОКА\n"


CHROME_BROWSER_DRIVER = "C:\\Users\\anton\\Desktop\\chromedriver.exe"

FONBET_TABLE_TENNIS_LINK = "https://www.fonbet.ru/#!/live/table-tennis"
TT_CUP_LINK = "http://tt-cup.com/players/"

MAIN_URL_LIGA_PRO = "http://tt.sport-liga.pro/players/?name="
SPACE_URL_LIGA_PRO = "%20"
END_URL_LIGA_PRO = "&rat=Искать"

COUNT_WORD_RATING_LIGA_PRO = 6

def getTournamentByID(ID):
    if (ID == ID_1):
        return name_1
    elif (ID == ID_2):
        return name_2
    elif (ID == ID_3):
        return name_3
    elif (ID == ID_4):
        return name_4
    else:
        return name_not_god_tournament
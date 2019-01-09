#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import re
from threading import Thread
from MainFile import mainWork
import queue
from Makers import Print
#from flask_sslify import SSLify


print("uping file")

#listOfGame = []
#listOfMember = []
#def loopSendStrat():


#threadSendStrat = Thread(target=loopSendStrat, args=[])
#threadSendStrat.start()

app = Flask(__name__)
#sslify = SSLify(app)


http = "http"
serverIP_Port = ""


http = "http"
serverIP_Port = ""


token = '684761241:AAHanKSvHWV81b00IgAV3HKws9PTQbL7JnA'
URL = 'https://api.telegram.org/bot' + token + '/'
def parseText(text):
    pattern = r'/\w+'
    ret = re.search(pattern, text).group()
    return ret[1:]

@app.route('/', methods = ['POST', 'GET'])
def index():
    print("u posta")
    if request.method == 'POST':
        req = request.get_json()
        print(req)
        try:
            chat_id = req['message']['chat']['id']
            #print("get chat id")
            message = req['message']['text']
            #print("get message")
            name = req['message']['from']['first_name']
            #print("get user id")
            user_id = req['message']['from']['id']
        except:
            #if (message == '/me'):
            #    send_message(chat_id=281265894, text=str(chat_id)) # i'm
            #    send_message(chat_id=281265894, text="from: " + getNamePrint(chat_id, user_id)) # i'm
            return 'hello g'
        #print(listOfGame)
        command = message
        print("у комманд")
        if (command == '/me'):
            send_message(chat_id=281265894, text=str(chat_id)) # i'm
            send_message(chat_id=281265894, text="from: " + getNamePrint(chat_id, user_id)) # i'm
        elif (command == '/game'):
            #global listOfGame
            send_message(chat_id=chat_id, text=Print.getStrAboutGame(listOfGame=listOfGame))
        elif (chat_id==281265894 and len(command.split('?')) > 0 and command.split('?')[0] == '/addshort'):
            send_message(chat_id=281265894, text="add: " +command.split('?')[1]) # i'm
            listOfMemberShort.append(int(command.split('?')[1]))
            send_message(chat_id=int(command.split('?')[1]), text="вы добавлены в рассылку!")
        elif (chat_id==281265894 and len(command.split('?')) > 0 and command.split('?')[0] == '/addall'):
            send_message(chat_id=281265894, text="add: " +command.split('?')[1]) # i'm
            listOfMemberAll.append(int(command.split('?')[1]))
            send_message(chat_id=int(command.split('?')[1]), text="вы добавлены в рассылку с полной отдачей!")
        elif (chat_id==281265894 and len(command.split('?')) > 0 and command.split('?')[0] == '/addstrat'):
            send_message(chat_id=281265894, text="add: " +command.split('?')[1]) # i'm
            listOfMemberStrat.append(int(command.split('?')[1]))
            send_message(chat_id=int(command.split('?')[1]), text="вы добавлены в рассылку по стратам!")
        elif (command=='/all' and checkInStrat(chat_id)):
            try:
                listOfMemberStrat.remove(chat_id)
                listOfMemberAll.append(chat_id)
                send_message(chat_id=chat_id, text="вы добавлены в рассылку с полнйо отдачей!")
            except:
                send_message(chat_id=281265894, text="alladd truble: " + str(chat_id)) # i'm
                send_message(chat_id=chat_id, text="alladd truble please write @AZchDev") # i'm
        elif (command=='/strat' and checkInAll(chat_id)):
            try:
                listOfMemberAll.remove(chat_id)
                listOfMemberStrat.append(chat_id)
                send_message(chat_id=chat_id, text="вы добавлены в рассылку по стратам!")
            except:
                send_message(chat_id=281265894, text="stratadd truble: " + str(chat_id)) # i'm
                send_message(chat_id=chat_id, text="stratadd truble please write @AZchDev") # i'm
        elif (chat_id==281265894 and len(command.split('?')) > 0 and command.split('?')[0] == '/delshort'):
            try:
                send_message(chat_id=281265894, text="del: " +command.split('?')[1]) # i'm
                delFromShort(command.split('?')[1])
                send_message(chat_id=int(command.split('?')[1]), text="вы удалены из ограниченной рассылки!")
            except:
                send_message(chat_id=281265894, text="delshort truble: " + str(chat_id)) # i'm
        elif (chat_id==281265894 and len(command.split('?')) > 0 and command.split('?')[0] == '/dellist'):
            try:
                send_message(chat_id=281265894, text="del: " +command.split('?')[1]) # i'm
                delFromLists(command.split('?')[1])
                send_message(chat_id=int(command.split('?')[1]), text="вы удалены из рассылки!")
            except:
                send_message(chat_id=281265894, text="dellist truble: " + str(chat_id)) # i'm
        




        return 'hello g'
    return 'hello g'
    #if (request.method == 'POST'):
        #try:
            #req = request.get_json()


def delFromLists(chat_id):
    for oneId in listOfMemberAll:
        if (oneId == chat_id):
            listOfMemberAll.remove(oneId)
    for oneId in listOfMemberStrat:
        if (oneId == chat_id):
            listOfMemberStrat.remove(oneId)

def delFromShort(chat_id):
    for oneId in listOfMemberShort:
        if (oneId == chat_id):
            listOfMemberShort.remove(oneId)

def checkInStrat(chat_id):
    for oneId in listOfMemberStrat:
        if (oneId == chat_id):
            return True
    return False

def checkInAll(chat_id):
    for oneId in listOfMemberAll:
        if (oneId == chat_id):
            return True
    return False


def getNamePrint(chat_id, user_id):
    namePrint = ''
    answer = {'chat_id': chat_id, 'user_id': user_id}
    user = requests.get(URL + 'getChatMember', answer).json()
    try:
        return " @%s (%s %s)" % (user['result']['user']['username'], user['result']['user']['first_name'], user['result']['user']['last_name'])
    except Exception as e:
        try:
            return "@%s (%s)" % (user['result']['user']['username'], user['result']['user']['first_name'])
        except Exception as e:
            try:
                return "%s %s" % (user['result']['user']['first_name'],
                                                         user['result']['user']['last_name'])
            except Exception as e:
                return "%s" % (user['result']['user']['first_name'])

def send_message(chat_id, text):
    # https://api.telegram.org/bot503945314:AAqMC9y0tRho/sendMessage
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    req = requests.post(url, json = answer)
    return req.json()

def makelistOfMemberShort(listOfMemberShort):

    listOfMemberShort.append(270749872) # радик м
    listOfMemberShort.append(-1001258306501) # чат object'a

    return listOfMemberShort

def makelistOfMemberStratMore(listOfMemberStrat):
    listOfMemberStrat.append(319201172) # obj3ct 
    listOfMemberStrat.append(607415198) # валерий
    return listOfMemberStrat

def makelistOfMemberAllMore(listOfMemberAll):
    listOfMemberAll.append(281265894) # i'm
    return listOfMemberAll



if __name__ == '__main__':
    print("start main")
    global listOfMemberShort
    global listOfGame
    global listOfMemberStrat
    global listOfMemberAll

    listOfMemberShort= []
    listOfMemberShort = makelistOfMemberShort(listOfMemberShort)   
 
    listOfMemberStrat = []
    listOfMemeber = makelistOfMemberStratMore(listOfMemberStrat)

    listOfMemberAll = []
    listOfMemberAll = makelistOfMemberAllMore(listOfMemberAll)

    listOfGame = []
    qe = queue.Queue()
    thread = Thread(target=mainWork.initFind, args=[qe, listOfGame, listOfMemberShort, listOfMemberStrat, listOfMemberAll])
    thread.start()
    print("start app")
    app.run()

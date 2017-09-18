# coding=utf-8
from __future__ import print_function
import json
from os import listdir
import sys
import pysolr
from random import randint
import re

training_path = "/home/ubuntu/progettoSII/intents"
#training_path = "/Users/blackmamba/Desktop/SII-chatbot/intents"
solr = pysolr.Solr('http://localhost:8983/solr/prova', timeout=10)
regex = re.compile(r'\w*(\\xe9|\\xe0|\\xe8|\\xf2|\\xf9|\\xec|\\u0027)')
regex2 = '\w*(\\xe9|\\xe0|\\xe8|\\xf2|\\xf9|\\xec|\\u0027)'

def add_intents_into_db():
    for filename in listdir(training_path):
        if filename.endswith(".json"):
            f = open(training_path + "/" + filename, "r")
            value = json.loads(f.read())
            domande = []
            risposte = []
            data = {}

            for itemData in value["userSays"]:
                for itemText in itemData["data"]:
                    userSays = itemText['text']
                    while re.match(regex, userSays):
                        userSays = changeCodes(userSays)
                    domande.append(userSays)

            for itemResponses in value["responses"]:
                for itemMessages in itemResponses["messages"]:
                    messages = itemMessages['speech']
                    print(filename)
                    if isinstance(messages, list):
                        for sentences in messages:
                            risposte.append(sentences)
                    else:
                        while re.match(regex, messages):
                            messages = changeCodes(messages)
                        risposte.append(messages)

            data['id'] = filename
            data['topic'] = filename.split(".")[2]+".json"
            data['domande'] = domande
            data['risposte'] = risposte

            solr.add([data])

def changeCodes(messagge):
    if '\\xe9' in messagge:
        finalMessage = re.sub(r"(\\xe9)", 'é', messagge)
    elif '\\xe0' in messagge:
        finalMessage = re.sub(r"(\\xe0)", 'à', messagge)
    elif '\\xe8' in messagge:
        finalMessage = re.sub(r"(\\xe8)", 'è', messagge)
    elif '\\xf2' in messagge:
        finalMessage = re.sub(r"(\\xf2)", 'ò', messagge)
    elif '\\xf9' in messagge:
        finalMessage = re.sub(r"(\\xf9)", 'ù', messagge)
    elif '\\xec' in messagge:
        finalMessage = re.sub(r"(\\xec)", 'ì', messagge)
    elif '\\u0027' in messagge:
        finalMessage = re.sub(r"(\\u0027)", '\'', messagge)
    return finalMessage

def getResponses(phrase):

    results = solr.search(phrase)
    if results.__len__()>0:
        for result in results:

            messagges = []

            for sentences in result['risposte']:
                messagges.append(sentences)

            if messagges.__len__()>1:
                position = randint(1, messagges.__len__() - 1)
            else:
                position = 0
            messagge = messagges[position]

            finalMessage = ''
            if '\\xe9' in messagge:
                finalMessage = re.sub(r"(\\xe9)",'é',messagge)
            elif '\\xe0' in messagge:
                finalMessage = re.sub(r"(\\xe0)",'à',messagge)
            elif '\\xe8' in messagge:
                finalMessage = re.sub(r"(\\xe8)",'è',messagge)
            elif '\\xf2' in messagge:
                finalMessage = re.sub(r"(\\xf2)",'ò',messagge)
            elif '\\xf9' in messagge:
                finalMessage = re.sub(r"(\\xf9)",'ù',messagge)
            elif '\\xec' in messagge:
                finalMessage = re.sub(r"(\\xec)",'ì',messagge)
            elif '\\u0027' in messagge:
                finalMessage = re.sub(r"(\\u0027)",'\'',messagge)
            else:
                finalMessage = messagge
            return finalMessage
    else:
        return 'non so ancora come risponderti'



if __name__ == '__main__':
    if sys.argv.__len__()>2:
        globals()[sys.argv[1]](sys.argv[2])
    else:
        globals()[sys.argv[1]]()







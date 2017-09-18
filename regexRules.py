# coding=utf-8
from solr import getResponses
import re
from random import randint

listHello = ['ciao', 'ao', 'ei', 'ehi', 'salve', 'buongiorno', 'buonasera', 'buondi']
listHelloResponse = ['Ciao!', 'ao zii', 'ei bello', 'Salve', 'Ciao come stai?', 'Ciao come va?']

byeRegex = '(a|ci|sto|addio) (dopo|presto|vediamo|sentiamo|si|pi[ù,u])? ' \
           '?(dopo|bell[o,a]|car[o,a]|vede|pi[u,ù]|presto)? ?(tardi)?'
listBye = ['arrivederci', 'a dopo', 'ci vediamo dopo', 'ci vediamo presto', 'a dopo caro',
           'a dopo cara', 'a dopo bello', 'a dopo bella', 'bella!']

regexAnnoying = '(sei|mi|sono) (noios[o,a]|irritante|dai|annoio|annoiat[o,a]|annoi|stai) ?(fastidio|annoiando)?'
listAnnoying = ['Mi dispiace. Vorrei farti divertire di più', 'Possiamo parlare di qualsiasi cosa.', 'Magari non hai ancora provato tutte le mie capacità.']

howAreYouRegex = '(come|che|tutto|stai) (stai|va|butta|si|bene|ti) ?(\?|dice|senti|va)?'
listHowYouAreResponses = ['Tutto bene, tu?','Alla grande e tu?','Tutto apposto, grazie, tu invece?', 'Ti ringrazio, io bene e tu?','sono una macchina, non posso stare male, tu stai bene invece?']

thankRegex = '(\bgrazie\b)[^\?]*$|(\bti ringrazio\b)[^\?]*$'
listThankResponses = ['Non c\'è di che!', 'Ma figurati!', 'Prego!', 'Figurati, per così poco...']

whoAreYouRegex = '(come|quale|cosa|hai|come|che|a|chi) (ti|è|sei|saresti|un|nome|fai|cosa) ?(chiami|il|nome|definiresti|hai|chiamano|servi)? ?(tuo)? ?(nome)?'
listWhoAreYouResponses = ['Sono un bot programmato per rispondere alle tue domande', 'Mi chiamo Jhonattan e sono qui per parlare con te', 'Sono Jhonattan, pronto a risponderti!']

howOldAreYouRegex = '(quanti|mi dici|dimmi|quanto) (anni|la tua età|la tua eta|sei grande| sei vecchi[a,o]) ?(hai)?'
listHowOldAreYouResponses = ['Non ho un\'età, sono un bot', 'Sono un bot molto giovane, spero di soddisfare ogni tua richiesta', 'Io sono nuovo, tu invece quanti anni hai?']

badAnswerRegex = '(rispondi|non hai risposto|puoi rispondere|rispondimi|non mi hai dato|dammi) (alla|una risposta)? ?(mia)? ?(domanda)?'
listBadAnswerRegex = ['Potresti ripetere la domanda in un altro modo, per favore?','Potresti essere più specifico? Non ho capito bene', 'Scusami, prova a formulare la domanda diversamente']

helpRegex = '(aiutarmi|aiuto|aiutami|assistenza|ho bisogno di te|mi aiuti)'
listHelpResponses = ['Sono qui per aiutarti', 'Dimmi tutto', 'Dimmi qual è il tuo problema', 'Provo ad aiutarti, dimmi!']


def getResponse(phrase):

    if len(phrase) < 2:
        return 'non ho capito puoi ripetere'

    elif any(word in phrase.split(' ') for word in listHello):
        position = randint(0, listHelloResponse.__len__()-1)
        return listHelloResponse[position]

    elif re.match(byeRegex, phrase):
        position = randint(0, listBye.__len__()-1)
        return listBye[position]

    elif re.match(regexAnnoying, phrase):
        position = randint(0, listAnnoying.__len__() - 1)
        return listAnnoying[position]

    elif re.match(howAreYouRegex, phrase):
        position = randint(0, listHowYouAreResponses.__len__() - 1)
        return listHowYouAreResponses[position]

    elif re.match(thankRegex, phrase):
        position = randint(0, listThankResponses.__len__() - 1)
        return listThankResponses[position]

    elif re.match(whoAreYouRegex, phrase):
        position = randint(0, listWhoAreYouResponses.__len__() - 1)
        return listWhoAreYouResponses[position]

    elif re.match(howOldAreYouRegex, phrase):
        position = randint(0, listHowOldAreYouResponses.__len__() - 1)
        return listHowOldAreYouResponses[position]

    elif re.match(badAnswerRegex, phrase):
        position = randint(0, listBadAnswerRegex.__len__() - 1)
        return listBadAnswerRegex[position]

    elif re.match(helpRegex, phrase):
        position = randint(0, listHelpResponses.__len__() - 1)
        return listHelpResponses[position]

    else:
        return getResponses(phrase)


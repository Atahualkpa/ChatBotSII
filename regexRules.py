# coding=utf-8
from solr import selectCore
import re
from random import randint

listHello = ['ciao', 'ao', 'ei', 'ehi', 'salve', 'buongiorno', 'buonasera', 'buondi']
listHelloResponse = ['Ciao!', 'ao zii', 'ei bello', 'Salve', 'Ciao come stai?', 'Ciao come va?']

byeRegex = '(a|ci|sto) (dopo|presto|vediamo|sentiamo|si|pi[ù,u]|andando) ?(dopo|bell[o,a]|car[o,a]|vede|pi[u,ù]|presto)? ?(tardi)?'
listBye = ['arrivederci', 'a dopo', 'ci vediamo dopo', 'ci vediamo presto', 'a dopo caro',
           'a dopo cara', 'a dopo bello', 'a dopo bella', 'bella!']

regexAnnoying = '(.*?)(sei|mi|sono) (noios[o,a]|irritante|dai|annoio|annoiat[o,a]|annoi|stai) ?(fastidio|annoiando)?'
listAnnoying = ['Mi dispiace. Vorrei farti divertire di più', 'Possiamo parlare di qualsiasi cosa.',
                'Magari non hai ancora provato tutte le mie capacità.']

howAreYouRegex = '(.*?)(come|che|stai) (stai|va|butta|si|ti) ?(\?|dice|senti|va)?\??'
listHowYouAreResponses = ['Tutto bene, tu?', 'Alla grande e tu?', 'Tutto apposto, grazie, tu invece?',
                          'Ti ringrazio, io bene e tu?',
                          'sono una macchina, non posso stare male, tu stai bene invece?']

thankRegex = '((.*?)(ti ringrazio|grazie))[^\?]*$'
listThankResponses = ['Non c\'è di che!', 'Ma figurati!', 'Prego!', 'Figurati, per così poco...']

whoAreYouRegex = '(.*?)(come|qual[e,\']?|hai|chi è|mi dici) (ti chiami|ti chiamano|ti definiresti|è il tuo nome|un nome|il tuo nome)'
listWhoAreYouResponses = ['Sono un bot programmato per rispondere alle tue domande',
                          'Mi chiamo Jhonattan e sono qui per parlare con te', 'Sono Jhonattan, pronto a risponderti!']

howOldAreYouRegex = '(.*?)(quanti|mi dici|dimmi|quanto) (anni|la tua età|la tua eta|sei grande|sei vecchi[a,o]) ?(hai)?'
listHowOldAreYouResponses = ['Non ho un\'età, sono un bot',
                             'Sono un bot molto giovane, spero di soddisfare ogni tua richiesta',
                             'Io sono nuovo, tu invece quanti anni hai?']

badAnswerRegex = '(.*?)(rispondi|non hai risposto|puoi rispondere|rispondimi|non mi hai dato una risposta|dammi una risposta)'
listBadAnswerRegex = ['Potresti ripetere la domanda in un altro modo, per favore?',
                      'Potresti essere più specifico? Non ho capito bene',
                      'Scusami, prova a formulare la domanda diversamente']

helpRegex = '(.*?)(aiutarmi|aiuto|aiutami|assistenza|ho bisogno di te|mi aiuti)'
listHelpResponses = ['Sono qui per aiutarti', 'Dimmi tutto', 'Dimmi qual è il tuo problema',
                     'Provo ad aiutarti, dimmi!']


def getResponse(phrase):
    if len(phrase) < 2:
        return 'non ho capito puoi ripetere'

    elif any(word in phrase.split(' ') for word in listHello):
        position = randint(0, listHelloResponse.__len__() - 1)
        return listHelloResponse[position]

    elif re.match(byeRegex, phrase) or re.match('addio', phrase):
        position = randint(0, listBye.__len__() - 1)
        print 'byeRegex'
        return listBye[position]

    elif re.match(regexAnnoying, phrase):
        position = randint(0, listAnnoying.__len__() - 1)
        print 'regexAnnoying'
        return listAnnoying[position]

    elif re.match(howAreYouRegex, phrase) or re.match('tutto bene\?', phrase):
        position = randint(0, listHowYouAreResponses.__len__() - 1)
        print 'howAreYouRegex'
        return listHowYouAreResponses[position]

    elif re.match(thankRegex, phrase):
        position = randint(0, listThankResponses.__len__() - 1)
        print 'thankRegex'
        return listThankResponses[position]

    elif re.match(whoAreYouRegex, phrase) or re.match('(chi sei|cosa fai|a che servi|a cosa servi|chi saresti|chi è)',phrase):
        position = randint(0, listWhoAreYouResponses.__len__() - 1)
        print 'whoAreYouRegex'
        return listWhoAreYouResponses[position]

    elif re.match(howOldAreYouRegex, phrase):
        position = randint(0, listHowOldAreYouResponses.__len__() - 1)
        print 'howOldAreYouRegex'
        return listHowOldAreYouResponses[position]

    elif re.match(badAnswerRegex, phrase):
        position = randint(0, listBadAnswerRegex.__len__() - 1)
        print 'badAnswerRegex'
        return listBadAnswerRegex[position]

    elif re.match(helpRegex, phrase):
        position = randint(0, listHelpResponses.__len__() - 1)
        print 'helpRegex'
        return listHelpResponses[position]

    else:
        return selectCore(re.sub('\W',' ',phrase))


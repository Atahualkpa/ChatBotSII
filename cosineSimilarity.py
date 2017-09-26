# coding=utf-8
import re, math
import nltk
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
from nltk.corpus import stopwords
from pattern.text.it import conjugate, INFINITIVE,PRESENT, SG, parse

from rippletagger.tagger import Tagger
tagger = Tagger(language="it")

#nltk.download('stopwords')

#WORD = re.compile(r'\w+')

stemmer = SnowballStemmer("italian")
stoplist = stopwords.words('italian')

def analyzeSentence(text):
    taggedSentence = tagger.tag(re.sub('\W',' ',text))
    vectSentence = []

    print taggedSentence

    for word in taggedSentence:
        if word[0] not in stoplist:
            if 'AUX' in word or 'VERB' in word:
                vectSentence.append(conjugate(word[0], INFINITIVE))
            else:
                vectSentence.append(stemmer.stem(word[0]))
    return Counter(vectSentence)

def get_cosine(text1, text2):
     vec1 = analyzeSentence(text1)
     print vec1
     vec2 = analyzeSentence(text2)
     print vec2
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

#text1 = 'come faccio a demolire la mia macchina'
#text2 = 'Demolizione di un veicolo'

#vector1 = analyzeSentence(text1)
#vector2 = analyzeSentence(text2)

#cosine = get_cosine(text1, text2)

#print 'Cosine:', cosine

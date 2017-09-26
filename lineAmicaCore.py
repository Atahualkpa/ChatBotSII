# coding=utf-8
import xml.etree.ElementTree as ET
import re
import pysolr
solr = pysolr.Solr('http://localhost:8983/solr/lineamica', timeout=10)

tree = ET.parse('/Users/blackmamba/Downloads/domande-risposte.xml')
root = tree.getroot()
data = {}

for nodes in root.findall('node'):
    data['id'] = re.sub(' ','_',nodes.findall('Titolo')[0].text)
    data['topic'] = nodes.findall('Titolo')[0].text
    data['domande'] = nodes.findall('Domanda')[0].text
    data['risposte'] = nodes.findall('Risposta')[0].text
    solr.add([data])

print 'end *.* '
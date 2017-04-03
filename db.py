import math
import nltk.collocations
import nltk.corpus
import collections
from nltk.corpus import wordnet as wn
from slugify import slugify
from arango import ArangoClient
from bk import semantic_similarity

client = ArangoClient(
    protocol='http',
    host='localhost',
    port=8529,
    username='root',
    password='root',
    enable_logging=True
)
'''
db = client.create_database('yahoo_query')
keywords = db.create_collection('keywords')
keywords.add_hash_index(fields=['name'], unique=True)
'''
db = client.db('yahoo_query')

f = open('ydata.txt')
rawText = f.read()
splitText = rawText.split('\n')


def convertToKey(s):
    ord3 = lambda x : '%.3d' % ord(x)
    return int(''.join(map(ord3, s)))

def convertFromKey(n):
    s = str(n)
    return ''.join([chr(int(s[i:i+3])) for i in range(0, len(s), 3)])

def create_nodes(stxt):
    keywords = db.create_collection('keywords')
    for txt in stxt:        
        if txt:
            txt = txt.strip().strip('"')
            key = convertToKey(txt)
            
            data = {'_key': str(key), 'name': txt, 'title': txt}
            keywords.insert(data)    
            print data
        
    return True
        

def create_relation_graph(stxt):
    
    count = 0   
    countCompare = 0   
    
    
    relation_graph = db.create_graph('relation')
    relations = relation_graph.create_edge_definition(
        name='relations',
        from_collections=['keywords'],
        to_collections=['keywords']
    )
    
    
    for txt in stxt:        
        
        txt = txt.strip().strip('"')
                
        
        for compareTxt in stxt:            
            '''
            if countCompare > 5000:
                break
            '''
            compareTxt = compareTxt.strip().strip('"')
            s = semantic_similarity(txt,compareTxt)
            
            if s >= 1:
                keyTxt = convertToKey(txt)
                keycompareTxt = convertToKey(compareTxt)
                data = {'_from': 'keywords/' + str(keyTxt), '_to': 'keywords/'+ str(keycompareTxt) }               
                relations.insert(data)
                print data
     
            countCompare += 1
    
        count += 1
    
    
createNodes = create_nodes(splitText)

if createNodes:
    create_relation_graph(splitText)
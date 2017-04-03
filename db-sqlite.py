import math
import nltk.collocations
import nltk.corpus
import collections
from nltk.corpus import wordnet as wn
from slugify import slugify

from bk import *
from datetime import datetime
import time, sqlite3, re, os
import socket


DEFAULT_DB_PATH = 'filtered-data.db'


conn = sqlite3.connect(DEFAULT_DB_PATH)
c = conn.cursor()

f = open('ydata.txt')
rawText = f.read()
splitText = rawText.split('\n')


def create_nodes(stxt):

    for txt in stxt:        
        if txt:
            txt = txt.strip().strip('"')
            
            isUrl = is_valid_url(txt)       
            if isUrl:
                continue
                       
            tk1 = nltk.word_tokenize(txt)
            pt1 = nltk.pos_tag(tk1)
            cd = [word for word,pos in pt1 if pos == 'CD']            
            if cd:
                continue
            
            stmnt = 'INSERT INTO nodes (Id) VALUES(?)'
            pvalue = (txt,)
            c.execute(stmnt, pvalue)
            conn.commit()
            
            print txt
        
    return True
        

def create_relation_graph(stxt):
    
    count = 0   
    countCompare = 0   
       
    for txt in stxt:        
        
        txt = txt.strip().strip('"')
                
        
        for compareTxt in stxt:
            compareTxt = compareTxt.strip().strip('"')
            s = semantic_similarity(txt,compareTxt)
            
            if s >= 0.6:
                stmnt = 'INSERT INTO edges (Source, Target, TotalWeight) VALUES(?,?,?)'
                pvalue = (txt,compareTxt, s)
                c.execute(stmnt, pvalue)
                conn.commit()
                
                data = {'current txt': str(count), 'comparing txt': str(countCompare) }              
                print data
     
            countCompare += 1
    
        count += 1
    
    
#createNodes = create_nodes(splitText)
createNodes = True
if createNodes:
    create_relation_graph(splitText)
    


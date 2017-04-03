import nltk.collocations
import nltk.corpus
import collections
from nltk.corpus import wordnet as wn
from datetime import datetime
import time, sqlite3, re, os

DEFAULT_DB_PATH = 'bgram.db'
conn = sqlite3.connect(DEFAULT_DB_PATH)
c = conn.cursor()

f = open('ydata.txt')
rawText = f.read()
splitText = rawText.split('\n')
bgm    = nltk.collocations.BigramAssocMeasures()
#tgm    = nltk.collocations.TrigramAssocMeasures()
tFinder = nltk.collocations.BigramCollocationFinder.from_words( splitText )
#tFinder = nltk.collocations.TrigramCollocationFinder.from_words( splitText )
scored = tFinder.score_ngrams( bgm.raw_freq )

count = 0
output = sorted(tFinder.nbest(bgm.raw_freq, 5000))
for dt in output:
    count += 1
    dt1 = dt[0].strip().strip('"')
    dt2 = dt[1].strip().strip('"')
    
    stmnt = 'INSERT INTO edges (Source, Target, TotalWeight) VALUES(?,?,?)'
    pvalue = (dt1,dt2, 1)
    c.execute(stmnt, pvalue)
    conn.commit()
    
    data = {'current txt': str(count)}              
    print data
    
#print( wn.synsets('www.google.com')[0].definition() )

    
def bigram_similarity(str1, str2):
    
    
    
    return True

if __name__ == "__main__":
    print True


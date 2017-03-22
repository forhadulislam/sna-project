import nltk.collocations
import nltk.corpus
import collections
from nltk.corpus import wordnet as wn

f = open('ydata.txt')
rawText = f.read()
splitText = rawText.split('\n')
#bgm    = nltk.collocations.BigramAssocMeasures()
tgm    = nltk.collocations.TrigramAssocMeasures()
#finder = nltk.collocations.BigramCollocationFinder.from_words( splitText )
tFinder = nltk.collocations.TrigramCollocationFinder.from_words( splitText )
scored = tFinder.score_ngrams( tgm.raw_freq )

# Group bigrams by first word in bigram.                                        
prefix_keys = collections.defaultdict(list)
for key, scores in scored:
   prefix_keys[key[0]].append((key[1], scores))

# Sort keyed bigrams by strongest association.                                  
for key in prefix_keys:
   prefix_keys[key].sort(key = lambda x: -x[1])

'''
print 'www', prefix_keys['www.yahoo,ro'][0:10]
print 'xmla', prefix_keys['xmla'][:5]
print 'yooujizz', prefix_keys['yooujizz'][:5]
'''

print( sorted(tFinder.nbest(tgm.raw_freq, 10)) )
print( wn.synsets('www.google.com')[0].definition() )
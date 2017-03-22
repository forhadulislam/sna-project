import nltk, numpy
from nltk.tokenize import sent_tokenize

import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
# Ngrams with 'creature' as a member
creature_filter = lambda *w: 'creature' not in w
f = open('ydata.txt')
rawText = f.read()
## Bigrams
finder = TrigramCollocationFinder.from_documents(rawText)
# only bigrams that appear 3+ times
finder.apply_freq_filter(3)
# only bigrams that contain 'creature'
finder.apply_ngram_filter(creature_filter)
# return the 10 n-grams with the highest PMI
print finder.nbest(trigram_measures.likelihood_ratio, 10)
print(dir(TrigramCollocationFinder))

'''
if __name__ == '__main__':

    # Reading file ydata.txt which contains the data
    f = open('ydata.txt')
    rawText = f.read()
    # Splitting texts into arrays by newline
    splitText = rawText.split('\n')
    
    for i in range(0,100):
        text = sent_tokenize(splitText[i])
        textPosTag = nltk.pos_tag(text)
        print(textPosTag)
        
        '''
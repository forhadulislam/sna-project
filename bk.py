import nltk.collocations
import nltk.corpus
import collections
from nltk.corpus import wordnet as wn
from slugify import slugify


f = open('ydata.txt')
rawText = f.read()
splitText = rawText.split('\n')
bgm    = nltk.collocations.BigramAssocMeasures()
#tgm    = nltk.collocations.TrigramAssocMeasures()
tFinder = nltk.collocations.BigramCollocationFinder.from_words( splitText )
#tFinder = nltk.collocations.TrigramCollocationFinder.from_words( splitText )
scored = tFinder.score_ngrams( bgm.raw_freq )


    
    

'''
# Group bigrams by first word in bigram.                                        
prefix_keys = collections.defaultdict(list)
for key, scores in scored:
   prefix_keys[key[0]].append((key[1], scores))

# Sort keyed bigrams by strongest association.                                  
for key in prefix_keys:
   prefix_keys[key].sort(key = lambda x: -x[1])


print 'www', prefix_keys['www.yahoo,ro'][0:10]
print 'xmla', prefix_keys['xmla'][:5]
print 'yooujizz', prefix_keys['yooujizz'][:5]


#print( sorted(tFinder.nbest(bgm.raw_freq, 10)) )
#print( wn.synsets('www.google.com')[0].definition() )

# Frequency of words
splitByWord = rawText.split()
Freq_dist_nltk=nltk.FreqDist(splitByWord)
#print Freq_dist_nltk

#print splitByWord.collocations()

# Showing freq distribution numbers
for k,v in Freq_dist_nltk.items():
    if v > 1:
        #print str(k)+':'+str(v)
        print str(v)+'    '+str(k)        
'''     
def semantic_similarity(str1, str2):
    
    tk1 = nltk.word_tokenize(str1)
    pt1 = nltk.pos_tag(tk1)
    tk2 = nltk.word_tokenize(str2)
    pt2 = nltk.pos_tag(tk2)
    
    nounWeight = 0
    verbWeight = 0
    outputWeight = 0
    s = 0
    
    # Calculating noun weights
    propernouns1 = [word for word,pos in pt1 if pos == 'NN' or pos == 'NNP' or pos == 'PRP']
    propernouns2 = [word for word,pos in pt2 if pos == 'NN' or pos == 'NNP' or pos == 'PRP']    
    
    if propernouns1 and propernouns2:
        for pn1 in propernouns1:
            syns1 = wn.synsets(pn1)
            for pn2 in propernouns2:
                d = nltk.edit_distance(pn1, pn2)
                syns2 = wn.synsets(pn2)
                if syns1 and syns2:
                    s = syns1[0].wup_similarity(syns2[0])                    
                    #s = syns1[0].path_similarity(syns2[0])
                    if s > 0.2 and s < 0.4:
                        nounWeight += 0.4
                    elif s >= 0.4 and s < 0.75:
                        nounWeight += s
                    elif s >= 0.75 and s <= 1:
                        nounWeight += 1
                    else:
                        if s:
                            nounWeight += s
                
                    # If distance is lesst than or equal 2 then add 0.2
                    if d <= 2:  
                        nounWeight += 0.2
                
    # Calculating verb weights
    verbs1 = [word for word,pos in pt1 if pos == 'VBN' or pos == 'VB']
    verbs2 = [word for word,pos in pt2 if pos == 'VBN' or pos == 'VB']    
    s = 0
    if verbs1 and verbs2:
        for vb1 in verbs1:
            syns1 = wn.synsets(vb1)
            for vb2 in verbs2:
                d = nltk.edit_distance(vb1, vb2)
                syns2 = wn.synsets(vb2)
                s = syns1[0].wup_similarity(syns2[0])
                #s = syns1[0].path_similarity(syns2[0])
                if s > 0.2 and s < 0.4:
                    verbWeight += 0.4
                elif s >= 0.4 and s < 0.75:
                    verbWeight += s
                elif s >= 0.75 and s <= 1:
                    verbWeight += 1
                else:
                    if s:
                        verbWeight += s
                
                # If distance is lesst than or equal 2 then add 0.2
                if d <= 2:  
                    verbWeight += 0.2
                
    '''         
    print syns1
    print syns2
    '''
    
    outputWeight = nounWeight + verbWeight
    print "Output"
    '''
    if outputWeight > 1:
        return 1
    '''
    return outputWeight

if __name__ == "__main__":
    print semantic_similarity('amateur crossdresser','amateur gang bang')
    print semantic_similarity('world war','the great war')


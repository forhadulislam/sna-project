import nltk, numpy
from nltk.tokenize import sent_tokenize

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
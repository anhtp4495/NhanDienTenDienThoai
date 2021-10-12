from underthesea import word_tokenize
from  underthesea import sent_tokenize as st
from  underthesea import ner
import numpy as np
import codecs
import pickle
from pyvi import ViTokenizer
import thu

def token_text (text):
    s = st(text)
    Sent_list = []
    for i in range(len(s)):
        print(s[i])
        print(ViTokenizer.tokenize(s[i]))
        # sner = (ner(s[i]))
        Sent_list.append(ner(s[i]))
        # Sent_list.append(ner(word_tokenize(s[i],format="text")))
        create_wpct(Sent_list)
    return 1
'''
Sent_list = []
for i in range(len(s)):
    print(s[i])
    print(ViTokenizer.tokenize(s[i]))
    #sner = (ner(s[i]))
    Sent_list.append(ner(s[i]))
    #Sent_list.append(ner(word_tokenize(s[i],format="text")))
'''

def create_wpct (sent_list): #format list [[(),()],[(),()]]
    with codecs.open('token_test.txt', 'w', 'utf-8') as f:
        for i in range(len(sent_list)):
            for j in range (len(sent_list[i])):
                for k in range(len(sent_list[i][j])):
                    if k==len(sent_list[i][j])-1:
                        f.write(sent_list[i][j][k])
                    elif k==0:
                        f.write(thu.compound_word(sent_list[i][j][k])+'\t')
                    else:
                        f.write(sent_list[i][j][k]+'\t')
                f.write('\n')
            f.write('\n')
    return f

#create_wpct(Sent_list)

from underthesea import word_tokenize as w
from  underthesea import sent_tokenize as st
from  underthesea import ner
import numpy as np
import codecs
import pickle

def compound_word (w_string):
    #w_string=''
    w=w_string.split()
    s2=''
    for i in range(len(w)):
        if i == len(w) - 1:
            s2 = s2 + w[i]
        else:
            s2 = s2 + w[i] + '_'
    return s2


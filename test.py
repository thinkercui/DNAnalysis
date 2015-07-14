#test file
from __future__ import division
import copy
import re
import math
from Entirety import *
from WFreq import *
from NGram import *

#get all the i-gram, i <= n
def get_within_ngram(string,n):
    table = {}
    for i in range(1,n+1):
        ngram = NGram(string,i)
        table.update(ngram.table)

    return table

#------------------------------------------------------------------------------    


#dic = cal_words_entirety("test.txt")
#save_dic(dic,"dic.txt")

ngram = cal_ngram_entirety("test.txt",3)
save_dic(ngram,"ngram.txt")

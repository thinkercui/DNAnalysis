from __future__ import division
import copy
from Entirety import *
from WFreq import *
from NGram import *
from RStr import *



def getfilestr(filename):
    f = open(filename,"r")
    string = f.read()
    f.close()

    rule = re.compile(r'[^a-zA-Z\']')
    string = rule.sub("",string)

    return string.lower()
    
def get_letter_dic(text):
    lentotal = len(text)
    letterdic = NGram(text,1).table

    for key in letterdic:
        letterdic[key] = letterdic[key] / lentotal

    return letterdic

#calculate the Entirety of n-gram in a file
def cal_ngram_entirety(filename,n):
    string = getfilestr(filename)
    lentotal = len(string)
    letterdic = NGram(string,1).table
    worddic = NGram(string,n).table

    entirety = Entirety(letterdic,worddic,lentotal)
    table = copy.deepcopy(worddic)
    for key in table:
        table[key] = entirety.cal_entirety(key) + math.log(worddic[key]/lentotal)
    
    return table

#calculate the Entirety of words in a file
def cal_words_entirety(filename):
    string = getfilestr(filename)
    lentotal = len(string)
    letterdic = NGram(string,1).table
    worddic = WFreq(filename).get_word_frequency()

    entirety = Entirety(letterdic,worddic,lentotal)
    table = copy.deepcopy(worddic)
    for key in table:
        table[key] = entirety.cal_entirety(key) + math.log(worddic[key]/lentotal)
    
    return table

#save the dictionary ordered with the value
def save_dic(dic,filename):
    f = open(filename,"w")
    table = sorted(dic.items(),key=lambda d:d[1],reverse=True)
    for item in table:
        f.write(str(item[0])+"\t"+str(item[1])+"\n")

    f.close()

"""
#get the letterdic
text = getfilestr("test.txt")
letterdic = get_letter_dic(text)
save_dic(letterdic,"letter.dic")

#get random string of english letters
rstr = RStr("letter.dic")
string = rstr.get_random_str(1000000)
f = open("rand_1billion.str","w")
f.write(string)
f.close()

#get the entirety of n-gram(n==2) of normal english file
two_gram = cal_ngram_entirety("test.txt",2)
save_dic(two_gram,"two_gram.enti")

#get the entirety of n-gram(n==2) of random english file
two_gram = cal_ngram_entirety("rand_1billion.str",2)
save_dic(two_gram,"two_gram_rand.enti")
"""

"""
#get random string of english words
rstr = RStr("words_p.dic")
string = rstr.get_random_str(800000)
f = open("rand_words_800000.str","w")
f.write(string)
f.close()
print "random done!"
"""
#get the entirety of n-gram(n==2) of normal english file
two_gram = cal_ngram_entirety("test.txt",2)
save_dic(two_gram,"data/2/ngram_2.enti")

#get the entirety of n-gram(n==2) of random english file
two_gram = cal_ngram_entirety("rand_1billion.str",2)
save_dic(two_gram,"data/2/ngram_2_rand.enti")

#get the entirety of n-gram(n==2) of random english file
two_gram = cal_ngram_entirety("rand_words_800000.str",2)
save_dic(two_gram,"data/2/ngram_2_words_rand.enti")


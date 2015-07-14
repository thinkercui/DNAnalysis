#--------------------------------------------------------------------
#purpose:
#get the word frequency in a text
#
#author:cuixiaofei          time:2015.7.9
#--------------------------------------------------------------------
from __future__ import division
import re

class WFreq(object):
    def __init__(self,filename):
        self.word_total=0
        f = open(filename,"r")
        self.text = f.read()
        f.close()
        
    def get_word_frequency(self):
        #replace other words rather than english to ' '
        #all words are lower case already
        rule = re.compile(r'[^a-zA-Z\']')
        self.text = rule.sub(' ',self.text)
        self.text = self.text.lower()

        #create a list of words separated at white spaces
        wordlist = self.text.split(None)
        self.word_total = len(wordlist)	

        #create a wordfrequency dictionary
        #start with an empty dictionary
        freqDic = {}
        for word in wordlist:
            freqDic[word] = freqDic.get(word,0) + 1
	
        return freqDic

#save the dictionary ordered with the value
def save_dic(dic,filename):
    f = open(filename,"w")
    table = sorted(dic.items(),key=lambda d:d[1],reverse=True)
    for item in table:
        f.write(str(item[0])+"\t"+str(item[1])+"\n")

    f.close()


wfreq = WFreq("test.txt")
freqDic = wfreq.get_word_frequency()
save_dic(freqDic,"words.dic")
print wfreq.word_total  #wordtotal	876581

for key in freqDic:
    freqDic[key] = freqDic[key] / 876581

save_dic(freqDic,"words_p.dic")



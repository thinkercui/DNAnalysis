#----------------------------------------------------------------------
#purpose:
#get random sequece by the letterdic (letter,p)
#
#author:cuixiaofei              time:2015.7.9
#----------------------------------------------------------------------
from random import *
class RStr(object):
    def __init__(self,dic):
        self.dic = {}
        f = open(dic,"r")
        for line in f:
            data = line.split()
            self.dic[data[0]] = float(data[1])

        f.close()

    #get a random letter from the dic using roulette wheel algorithm
    def get_random_ch(self):
        rand = random()
        total = 0.0
        for key in self.dic:
            total = total + self.dic[key]
            if total >= rand:
                return key

    #get a n length random string using the dic setted
    def get_random_str(self,n):
        random_str = ""
        ncount = 0
        for i in range(n):
            #import pdb; pdb.set_trace();
            ch = self.get_random_ch()
            random_str = random_str + ch
            ncount = ncount + 1
            if ncount % 1000 == 0:
                print ncount
        return random_str

"""
rstr = RStr("letter.dic")
random_str = rstr.get_random_str(10)
print random_str,len(random_str)
"""


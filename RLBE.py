#!/usr/bin/env python
#--------------------------------------------------------------------
#purpose:
#get the left and right boundary entropy of an ngram in the sequence
#
#author:cuixiaofei          time:2015.7.13
#--------------------------------------------------------------------
from __future__ import division
import re
from math import log

class RLBE:
    def __init__(self,string):
        self.string = string

    #get all the n-gram suffix of the ngram
    def get_nsuffix(self,n,ngram):
        regstr = "("
        regstr = regstr + ngram
        for i in range(n):
            regstr = regstr + '.'

        regstr = regstr + ")"
        regex = re.compile(regstr)

        suffix = re.findall(regex,self.string)

        return suffix

    #get all the n-gram prefix of the ngram
    def get_nprefix(self,n,ngram):
        regstr = "("
        for i in range(n):
            regstr = regstr + '.'

        regstr = regstr + ngram
        regstr = regstr + ")"
        regex = re.compile(regstr)

        prefix = re.findall(regex,self.string)

        return prefix

    #get right boundary entropy
    def getRBE(self,n,ngram):
        suffix = self.get_nsuffix(n,ngram)
        nright = len(suffix)
        RBE = 0

        #create a frequency dictionary of the suffix of ngram
        freqDic = {}
        for item in suffix:
            freqDic[item] = freqDic.get(item,0) + 1

        for key in freqDic:
            p = freqDic[key] / nright
            RBE = RBE + p * log(p,2)

        RBE = -RBE

        print "right_freqDic",freqDic
        return RBE

    #get left boundary entropy
    def getLBE(self,n,ngram):
        prefix = self.get_nprefix(n,ngram)

        nleft = len(prefix)
        LBE = 0

        freqDic = {}
        for item in prefix:
            freqDic[item] = freqDic.get(item,0) + 1

        for key in freqDic:
            p = freqDic[key] / nleft
            LBE = LBE + p * log(p,2)

        LBE = -LBE

        print "left_freqDic",freqDic
        return LBE

    #get left and right boundary entropy
    def getRLBE(self,n,ngram):
        LBE = self.getLBE(n,ngram)
        RBE = self.getRBE(n,ngram)

        return LBE,RBE


if __name__ == "__main__":
    string = """HelloIamcuixiaofeiIamverygladtointroduceyouaboutthe
toolnameRLBEitisveryusefulandhelpfulIwishyouwilllikeitthisisthetest
dataofityouwillcalculatetheLBEandtheRBEofthewordsIhavejustsaidtoyou"""
    be = RLBE(string)
    LBE,RBE = be.getRLBE(2,"il")
    print "il",LBE,RBE
        
        

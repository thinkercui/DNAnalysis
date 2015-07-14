#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------
#purpose:
#calculate the word entirety using the worddic, letterdic and the length of the string(lentotal)
#
#author:    cuixiaofei      time:2015.7.9
#------------------------------------------------------------------------------------

from __future__ import division
import math

class Entirety(object):
    def __init__(self,letterdic,worddic,lentotal):
        self.letterdic = letterdic
        self.worddic = worddic
        self.lentotal = lentotal
        self.meansd = 0
        
    def cal_theory_lp(self,word):
        #get the probability of the letters combination in the word 
        p_combination = math.log(1)
        for letter in word:
            p_letter = self.letterdic[letter]/self.lentotal
            lp_letter = math.log(p_letter)
            p_combination = p_combination + lp_letter

        #get the probability of the permuation of the word's letter set
        letters = {}
        for letter in word:
            letters[letter] = letters.get(letter,0) + 1

        multi_subhead = 1
        for key in letters:
            multi_subhead = multi_subhead * math.factorial(letters[key])

        multi_numerator = math.factorial(len(word)) #分子

        p_permutation = math.log(multi_subhead / multi_numerator)
    
        #get lp_theory
        lp_theory = p_combination + p_permutation
        return lp_theory

    def cal_real_lp(self,word):
        p_word = self.worddic[word]/self.lentotal
        lp_real = math.log(p_word)

        return lp_real

    def cal_meansq_deviation(self):
        variance = 0
        for word in self.worddic:
            p_real = math.pow(math.e,self.cal_real_lp(word))
            p_theory = math.pow(math.e,self.cal_theory_lp(word))

            variance = variance + math.pow(p_real - p_theory,2)

        self.meansd = math.sqrt(variance)
            

    #calculate the Entirety of a word
    def cal_entirety(self,word):
        #return self.cal_real_lp(word) - self.cal_theory_lp(word)   #this is the entirety of last version
        p_real = math.pow(math.e,self.cal_real_lp(word))
        p_theory = math.pow(math.e,self.cal_theory_lp(word))
        
        entirety = (p_real - p_theory) / self.meansd

        return entirety
         

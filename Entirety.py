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
        
    def cal_theory_p(self,word):
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

    def cal_real_p(self,word):
        p_word = self.worddic[word]/self.lentotal
        lp_real = math.log(p_word)

        return lp_real

    #calculate the Entirety of a word
    def cal_entirety(self,word):
        return self.cal_real_p(word) - self.cal_theory_p(word)
         

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 15:01:34 2025

@author: gcrow
"""

#Generating elements of V
from thompson import *
sig = (2,1)

def elements_V(domain, range):
    d = Generators(sig, domain)
    r = Generators(sig, range)
    phi = Automorphism(d, r)
    return phi

#Example: from meeting 14th October
domain = ["x1 a1 a1", "x1 a1 a2", "x1 a2 a1 a1", "x1 a2 a1 a2", "x1 a2 a2"]
range = ["x1 a1 a2", "x1 a1 a1", "x1 a2 a1", "x1 a2 a2 a1", "x1 a2 a2 a2"]
alpha = elements_V(domain, range)
#Now save to file
alpha.save_to_file('alpha.aut', "Example to test conjugacy")

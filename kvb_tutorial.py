#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:49:13 2020

@author: mturan
"""

import pandas as pd
import os
os.chdir('/Users/mturan/Desktop/kvb/scripts')
import kvb

os.chdir('/Users/mturan/Desktop/kvb')
os.getcwd()



##################################################
#################### TUTORIAL ####################
##################################################


pdf = kvb.read_raw_pdf("kvb7.pdf")
pdf = kvb.turkish_ch(pdf)

print(kvb.get_tax_id(pdf))
print(kvb.type_check(pdf)) 
print(kvb.get_name(pdf))
print(kvb.get_term(pdf)) 
print(kvb.produce_fs_tables(pdf))

# DATABASE
test_cases = ["kvb1.pdf","kvb2.pdf","kvb3.pdf","kvb4.pdf",
              "kvb5.pdf","kvb6.pdf","kvb7.pdf","kvb8.pdf",
              "kvb9.pdf"]




tax_id = []
names = []
terms = []
types = []
pdfs = []

for i in test_cases:
    pdf = read_raw_pdf(i)
    pdf = turkish_ch(pdf)
    pdfs.append(pdf)
    
    tax = get_tax_id(pdf)
    tax_id.append(tax)
    
    type_form = type_check(pdf)
    types.append(type_form)
    
    name = get_name(pdf)
    names.append(name)
    
    term = get_term(pdf)
    terms.append(term)
    
df = pd.DataFrame(list(zip(tax_id, types, names, terms, pdfs)), 
               columns =['tax_id', 'types', 'names', 'terms', 'pdfs'])


df.to_pickle("df")

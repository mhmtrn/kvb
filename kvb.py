#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:49:04 2020

@author: mturan
"""

import pandas as pd
import PyPDF2
import os
import re

os.chdir('/Users/mturan/Desktop/kvb')
os.getcwd()


def read_raw_pdf(name_of_file: str):
    """
    The purpose of this function is to read pdf in raw format
    """
    pdfFileObj = open(str(name_of_file), 'rb')
    
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    length = pdfReader.numPages
    
    pdf = []
    for i in range(length):
        pageObj = pdfReader.getPage(i) 
        pdf.append(pageObj.extractText())
    
    pdf = ' '.join(pdf)
    
    return pdf



# upadte TR character
def turkish_ch(pdf):
    """
    The purpose of this function is update characters Turkish
    """
    pdf = pdf.replace("Ý", "İ")              
    pdf = pdf.replace("Ð", "Ğ")              
    pdf = pdf.replace("ý", "ı")              
    pdf = pdf.replace("Þ", "Ş")              
    pdf = pdf.replace("þ", "ş")              
    pdf = pdf.replace("ð", "ğ")     
    return pdf         


                    
def get_tax_id(pdf):
    """
    The purpose of this function is to detect Turkish tax id
    """
    test = "Posta Adresi"
    txt = ""
    for i in range(1000):
        txt = txt + pdf[i]
        if len(txt) == 12:
            if txt == test:
                result = pdf[i+1:i+11]          
            else:
                txt = txt[1:]       
        else:
            continue
    return result



def get_name(pdf):
    """
    The purpose of this function is to get names from tax declaration document
    """
    test = get_tax_id(pdf)
    txt = ""
    for i in range(1000):
        txt = txt + pdf[i]
        if len(txt) == 10: # it is 10 because of length of taxid
            if txt == test:
                index = i
                break
            else:
                txt = txt[1:]
    
    
    output = pdf[index+1:index+50]
    
    output = re.sub(r'\d+', '', output)
    output = re.sub(r"[-()\"#/@;:<>{}`+=~|!?,]", "", output)
                       
    remove_lower = lambda text: re.sub('[a-z]', '', text)
    
    output =  remove_lower(output)
    
    return output



def type_check(pdf):
    """
    The purpose of this function is to detect type of tax declaration
    """
    test1 = "KURUMLAR VERGİSİ BEYANNAMESİ"
    test2 = "GEÇİCİ VERGİ BEYANNAMESİ"
    
    if pdf[:6] == "KURUML":      
        txt = ""
        for i in range(1000):
            txt = txt + pdf[i]
            if len(txt) == len(test1):
                if txt == test1:
                    result = pdf[i+1:i+5]    
                else:
                    txt = txt[1:]       
            else:
                continue
            
    elif pdf[:6] == "GEÇİCİ": 
        txt = ""
        for i in range(1000):
            txt = txt + pdf[i]
            if len(txt) == len(test2):
                if txt == test2:
                    result = pdf[i+39:i+43]    
                else:
                    txt = txt[1:]       
            else:
                continue

    return result




def get_term(pdf):
    """
    The purpose of this function is to get year of tax decalaration
    """
    if pdf[:6] == "KURUML":      
        test = "l2"
        txt = ""
        for i in range(200):
            txt = txt + pdf[i]
            if len(txt) == len(test):
                if txt == test:
                    year = pdf[i:i+4]
                else:
                    txt = txt[1:] 
                
    elif pdf[:6] == "GEÇİCİ": 
        test = "m2"
        txt = ""
        for i in range(200):
            txt = txt + pdf[i]
            if len(txt) == len(test):
                if txt == test:
                    year = pdf[i:i+4]
                    term = pdf[i+4:i+5]
                    year = year + "-" + term
                else:
                    txt = txt[1:] 
                   
    return year



    
    
    

pdf = read_raw_pdf("kvb8.pdf")
pdf = turkish_ch(pdf)

print(get_tax_id(pdf))
print(type_check(pdf)) 
print(get_name(pdf))
print(get_term(pdf)) 


# DATABASE
test_cases = ["kvb1.pdf","kvb2.pdf","kvb3.pdf","kvb4.pdf",
              "kvb5.pdf","kvb6.pdf","kvb7.pdf","kvb8.pdf"]


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
    
    
    
    
    

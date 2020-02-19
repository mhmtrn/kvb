#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:49:04 2020

@author: mturan
"""

import pandas as pd
import PyPDF2
import os

os.chdir('/Users/mturan/Desktop/kvb')
os.getcwd()


def read_raw_pdf(name_of_file: str):
    """
    The purpose of this function is to read pdf in raw format
    """
    pdfFileObj = open('kvb6.pdf', 'rb')
    
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

def type_check(pdf):
    """
    The purpose of this function is to detect type of tax declaration
    """

    test = "KURUMLAR VERGİSİ BEYANNAMESİ"
    txt = ""
    for i in range(1000):
        txt = txt + pdf[i]
        if len(txt) == 28:
            if txt == test:
                result = pdf[i+1:i+5]    
                print(result)
            else:
                txt = txt[1:]       
        else:
            continue
    return result




pdf = read_raw_pdf("kvb6.pdf")
pdf = turkish_ch(pdf)
get_tax_id(pdf)
type_check(pdf)


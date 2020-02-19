#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:49:04 2020

@author: mturan
"""

import pandas as pd
import PyPDF2



pdfFileObj = open('KVB_.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

length = pdfReader.numPages

pdf = []
for i in range(length):
    pageObj = pdfReader.getPage(i) 
    print(pageObj.extractText()) 
    pdf.append(pageObj.extractText())

pdf = ' '.join(pdf)




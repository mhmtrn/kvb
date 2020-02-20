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
os.chdir('/Users/mturan/Desktop/kvb/scripts')
import dictionary

os.chdir('/Users/mturan/Desktop/kvb')
os.getcwd()


current_assets = dictionary.current_assets
tangible_assets = dictionary.tangible_assets
short_term_liabilities = dictionary.short_term_liabilities
long_term_liabilities = dictionary.long_term_liabilities
equity = dictionary.equity
income_sheet = dictionary.income_sheet



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



def get_value_of_account(account: str, part: str):
    """
    The purpose of this function is to get values of specified account
    """

    if type_check(pdf) == "1010":  
        account_index = part.find(account)     
        if account_index == -1:
            values = [] # fake move
        else:
            account_length = len(account)     
            values_account = part[account_index + account_length:]        
            first_comma = values_account.find(",")        
            second_comma = values_account.find(",", first_comma+1)        
            past_value = values_account[:first_comma+3]
            current_value = values_account[first_comma+3: second_comma+3]      
            values = [past_value, current_value]

    else:
        account_index = part.find(account)
        if account_index == -1:
            values = [] # fake move
        else:
            account_length = len(account)     
            values_account = part[account_index + account_length:]        
            first_comma = values_account.find(",")                
            value = values_account[:first_comma+3]
            values = [value]

    
    return values

    # MÜKERRER TEKRARLANAN HESAPLAR İÇİN ÇÖZ



def produce_fs_tables(pdf):
    """
    The purpose of this function is to extract financial values from the document
    """
    
    if type_check(pdf) == "1010":   # 1010 is unique code for year end reports
        
        # these section is to extract related part from the report
        current_assets_index = pdf.find(current_assets[0])
        tangible_assets_index = pdf.find(tangible_assets[0])
        short_term_liabilities_index = pdf.find(short_term_liabilities[0])
        long_term_liabilities_index = pdf.find(long_term_liabilities[0])
        equity_index = pdf.find(equity[0])
        income_sheet_index = pdf.find(income_sheet[0])
        income_sheet_index_end = pdf.find(income_sheet[-1])+100 # (heuristic)
        
        current_assets_part = pdf[current_assets_index:tangible_assets_index]
        tangible_assets_part = pdf[tangible_assets_index:short_term_liabilities_index]
        short_term_liabilities_part = pdf[short_term_liabilities_index:long_term_liabilities_index]
        long_term_liabilities_part = pdf[long_term_liabilities_index:equity_index]
        equity_part = pdf[equity_index:income_sheet_index]
        income_sheet_part = pdf[income_sheet_index:income_sheet_index_end]
    
        main_tables = [current_assets,  # main tables are from dictionary prepared in "dictionary.py"
                       tangible_assets, 
                       short_term_liabilities,
                       long_term_liabilities, 
                       equity,
                       income_sheet]
        
        parts = [current_assets_part, # extracted main tables
                 tangible_assets_part,
                 short_term_liabilities_part,
                 long_term_liabilities_part,
                 equity_part,
                 income_sheet_part]
        
    
        current_year = int(get_term(pdf))
        past_year = current_year-1
    
        tables = []
        for i, ii in zip(main_tables, parts): # look tables (in the dictionary) and look for in parts (please see maintables and parts)
            values_account = []
            names_account = []
            for accounts in i: 
                names_account.append(accounts)
                account = get_value_of_account(accounts, ii)
                values_account.append(account)
            
            fs = pd.DataFrame(list(zip(names_account, values_account)), 
                           columns =["accounts", "values"])
        
            tags = fs['values'].apply(pd.Series)
            
            if tags.shape[1] == 0: # if that part is empty, it needs another cleaning process
                tags[past_year] = 0
                tags[current_year] = 0
                fs = pd.concat([fs["accounts"], tags[:]], axis=1)
            else:            # cleaning process for converting number
                tags.columns = [past_year, current_year]
        
                tags[past_year] = tags[past_year].str.replace(".", "")
                tags[past_year] = tags[past_year].fillna(0)
                tags[past_year] = tags[past_year].replace(',','.', regex=True).astype(float)
                
                tags[current_year] = tags[current_year].str.replace(".", "")
                tags[current_year] = tags[current_year].fillna(0)
                tags[current_year] = tags[current_year].replace(',','.', regex=True).astype(float)
                
                fs = pd.concat([fs["accounts"], tags[:]], axis=1)
        
            tables.append(fs)
        
        tables = pd.concat(tables)
        
        
    elif type_check(pdf) == "1032": # 1032 is unique code for interim repots
        income_sheet_index = pdf.find(income_sheet[0])
        income_sheet_index_end = pdf.find(income_sheet[-1])+100 # (heuristic)
        
        income_sheet_part = pdf[income_sheet_index:income_sheet_index_end]
        
        values_account = []
        names_account = []
        for accounts in income_sheet: 
            names_account.append(accounts)
            account = get_value_of_account(accounts, income_sheet_part)
            values_account.append(account)
            
        fs = pd.DataFrame(list(zip(names_account, values_account)),  # in interim reports, there is only one table (income sheet)
                       columns =["accounts", "values"])
        
        tags = fs['values'].apply(pd.Series)
        
        term = get_term(pdf)
        
        tags.columns = [str(term)]
        
        tags[str(term)] = tags[str(term)].str.replace(".", "")
        tags[str(term)] = tags[str(term)].fillna(0)
        tags[str(term)] = tags[str(term)].replace(',','.', regex=True).astype(float)
        
        fs = pd.concat([fs["accounts"], tags[:]], axis=1)
        
        tables = fs
        
    tables = tables.reset_index(drop=True)

    return tables
  


pdf = read_raw_pdf("kvb9.pdf")
pdf = turkish_ch(pdf)

print(get_tax_id(pdf))
print(type_check(pdf)) 
print(get_name(pdf))
print(get_term(pdf)) 

test = produce_fs_tables(pdf)


    
    
    
    
    

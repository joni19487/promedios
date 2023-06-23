import pandas as pd
from openpyxl import Workbook
#from pyparsing import col
#import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.keys import *
import time
import os
import claves_fiscales

cuit= "23220614409"

total=0
       
df = pd.read_csv('Mis Comprobantes Emitidos - CUIT 23220614409.csv', encoding='utf-8')
print(df)
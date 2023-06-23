import pandas as pd
from openpyxl import Workbook
#from pyparsing import col
#import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.keys import *
import time
import os
import claves_fiscales

driver= r'webdriver//chromedriver.exe'
#RUTA DE DESCARGA DEL EXCEL MIS COMPROBANTES

ruta_descarga=r'C:\Users\SOLO OUTLOOK\Desktop\promedios' #ACA SE PUEDE CAMBIAR CON UN INPUT
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" :  ruta_descarga}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=driver, options=chromeOptions)
desde_hasta = "01/05/2023 - 31/05/2023"

f=open("cuits.csv","r")
#f=open("cuit_factu.csv","r")
for dato in f.readlines():
    h=open("resultados.csv","a")         
    cuit=dato[0:11]    
#    print("-"+cuit+"-","-"+clave+"-")
    #time.sleep(1)
    driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
    driver.maximize_window()
    # INGRESAR CUIT
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').clear()
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').send_keys(cuit)
    # SIGUIENTE
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/input[2]').click()
    # CLAVE FISCAL
    claves_fiscales.clave_fiscal(cuit)    
    try:
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[2]').send_keys(claves_fiscales.clave_fiscal(cuit))
        #INGRESAR
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[3]').click()
        time.sleep(2) 
        try:
            driver.find_element("xpath", '/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]').click()
        except:
            pass
        time.sleep(1)     
        #MIS COMPROBANTES
        driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[1]/input').click()
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[1]/input').send_keys('Mis Comprobantes')
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/ul/li/a/div/div/div[1]/div/p').click()
        time.sleep(1)
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.close()
        driver.switch_to.window(window_after)
        time.sleep(1)
        try:
            driver.find_element_by_xpath("/html/body/form/main/div/div/div[2]/div/a/div/div[2]/h2").click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/main/div/section/div/div[2]/div[2]/a/div[1]").click()

        except:
            driver.find_element_by_xpath("/html/body/main/div/section/div/div[2]/div[2]/a/div[1]").click()

        #FECHA
        driver.find_element("xpath", '/html/body/main/div/section/div[1]/div/div[1]/div/div[1]/div/div/input').clear()
        time.sleep(1)
        driver.find_element("xpath", '/html/body/main/div/section/div[1]/div/div[1]/div/div[1]/div/div/input').send_keys(desde_hasta)
        time.sleep(1)
        driver.find_element("xpath", '/html/body/main/div/section/div[1]/div/div[1]/div/div[5]/div/button').click()
        time.sleep(3)
        driver.find_element("xpath", '/html/body/main/div/section/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/button[1]/span').click()
        #time.sleep(1)
        time.sleep(3)    
        
        def resultado_mis_comprobantes():
            
            total=0   
            nota_de_credito = False
            factura_c = False         
            
            df = pd.read_csv('Mis Comprobantes Emitidos - CUIT '+cuit+'.csv', encoding='utf-8')  
            for row, datos in df.iterrows():        
                tipo=datos[1]
                importe=float(datos['Imp. Total'])
                if tipo[5]=='F':
                    total=importe+total
                    factura_c = True 
                    
                elif tipo[0:3] =='211':
                    total=importe+total
                    factura_c = True  
                elif tipo[0:3] =='213':
                    importe=importe*-1
                    total=importe+total
                    nota_de_credito = True
                elif tipo[5]=='N':
                    importe=importe*-1
                    total=importe+total
                    nota_de_credito = True
            if nota_de_credito == True:
              h.write( "NOTA DE CREDITO " + ";" + str(total) + " " + ";" + cuit + "\n")  
            elif factura_c  == True:
              h.write( "FACTURA C " + ";" + str(total) + " " + ";" + cuit + "\n")    
            elif total == 0:
              h.write( "FACTURA C " + ";" + str(total) + " " + ";" + cuit + "\n")  
            
            return total    
            
        resultado_mis_comprobantes()
        
        try:
            time.sleep(1)
            os.remove("Mis Comprobantes Emitidos.csv")
        except:
            pass
        try:
            time.sleep(1)        
            os.remove("Mis Comprobantes Emitidos - CUIT "+cuit+".csv")
        except:
            pass
        try:
            time.sleep(1)
            os.remove('Mis Comprobantes Emitidos '+cuit+'.csv')
        except:
            pass
    
    
    except Exception as e:  
        ERROR_CLAVE=open("Clave Fiscal Incorrecta.csv","a")  
        ERROR_CLAVE.write("--- CLAVE FISCAL ERRONEA --- "+ " " + ";"+ cuit + "\n")
        pass

from selenium import webdriver
import keyboard
import time
import pandas as pd
import claves_fiscales
import os

driver= r'webdriver//chromedriver.exe'
ruta_descarga=r'C:\Users\SOLO OUTLOOK\Documents\facturacion\descargas' #ACA SE PUEDE CAMBIAR CON UN INPUT
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" :  ruta_descarga}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=driver, options=chromeOptions)

CUIT = "20305266591"
CLAVE = "Cascuer123456"
FECHA = "27/12/2022"
DESDE = "01/12/2022"
HASTA = "31/12/2022"

driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
driver.maximize_window()
driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').clear()
driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').send_keys(CUIT)
driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/input[2]').click()
driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[2]').send_keys(CLAVE)
driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[3]').click()
time.sleep(1)
driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[1]/input').click()
time.sleep(1)
driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[1]/input').send_keys('Mis Comprobantes')
time.sleep(1)
driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/ul/li/a/div/div/div[1]/div/p').click()
time.sleep(3)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.close()
driver.switch_to.window(window_after)
time.sleep(1)
driver.find_element_by_xpath("/html/body/form/main/div/div/div[2]/div/a/div/div[2]/h2").click()


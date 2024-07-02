import sys
sys.path.insert(1, r'C:\Users\jorge\OneDrive\Documentos\Prueba Serquo')

import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Funciones_Globales():

    def __init__(self,driver):
        self.driver = driver
    

    def Tiempo(self,tiempo):
        t=time.sleep(tiempo)
        return t
    
    def Navegar(self,url,Tiempo):
        self.driver.get(url)
        t = time.sleep(Tiempo)
        return t
    
    def Texto_Xpath_Validar(self,xpath,username,tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val=self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val.clear()
            val.send_keys(username)
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print('No se encontro el elemento' + xpath)
            self.driver.close()

    def Texto_ID_Validar(self,id,username,tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,id)
            val.clear()
            val.send_keys(username)
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print('No se encontro el elemento' + id)
            self.driver.close()

    def Click_Xpath_Validar(self,xpath,tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH,xpath)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print('No se encontro el elemento' + xpath)
            self.driver.close()
            t = time.sleep(tiempo)
            return t
        
    def Click_ID_Validar(self,ID,tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.find_element(By.ID,ID)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print('No se encontro el elemento' + ID)
            self.driver.close()
            return t

    def scroll_to_element(self,xpath,tiempo):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH,xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();",element)
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print('No se encontro el elemento' + xpath)
            self.driver.close()
            return t

    def comprobar_texto(self,xpath,texto,tiempo):
         t = time.sleep(tiempo)
         try:
            element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH,xpath)
            text = element.text.strip()
            print(text)
            if text != texto:
                print("La compra no se ha realizado")
                self.driver.close()
            else:
                print('Texto correcto, se ha realizado la compra correctamente')
                return t
         except TimeoutException as ex:
             print(ex.msg)
             print('No se encontro el elemento, Error al completar la compra ')
             self.driver.close()
             return t
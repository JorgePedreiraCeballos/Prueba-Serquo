import sys
sys.path.insert(1, r'C:\Users\jorge\OneDrive\Documentos\Prueba Serquo')
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageFunctions.Globalfunctions import Funciones_Globales
from pageFunctions.mainPageFunctions import Home_Page
from pageData.data import *
from pageObjetcs.mainPageObjects import *

tg = .5 

class test_login_and_buy(unittest.TestCase):

    def setUp(self):
        s=Service('C:\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test_buy(self):
        driver = self.driver
        mp = Home_Page(driver)
        gf = Funciones_Globales(driver)
        # visitiamos la pagina y hacemos login
        mp.Login(url,loginButton,usernameField,username,passwordField,password,loginConfirmButton,tg)
        # hacemos click en el primer item de los productos
        mp.go_and_click(firstItem,tg)
        # hacemos click en el boton add to cart
        mp.go_and_click(addToCartButton,tg)
        # damos a aceptar en el alert que aparece
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(tg)
        # hacemos click en Cart para ver el carrito
        mp.go_and_click(cartButton,tg)
        # hacemos click on place order
        mp.go_and_click(placeOrderButton,tg)
        # rellenamos el formulario y le damos al boton purchase
        mp.rellenar_formulario_compra(nameField,name,countryField,country,cityField,city,creditCardField,creditCard,monthField,month,yearField,year,tg)
        mp.go_and_click(purchaseButton,tg)
        # comprobamos que aparece el texto Thanks you for your purchase para confirmar que la compra se ha realizado correctamente
        gf.comprobar_texto(purchaseText,textPurchase,tg)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


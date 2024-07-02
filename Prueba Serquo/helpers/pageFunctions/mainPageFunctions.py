import sys
sys.path.insert(1, r'C:\Users\jorge\OneDrive\Documentos\Prueba Serquo')

from Globalfunctions import Funciones_Globales

class Home_Page():

    def __init__(self,driver):
        self.driver = driver

    def Login(self,url,login_button, username_field, user,password_field, user_password,login_confirmation, t):
        driver = self.driver
        gf = Funciones_Globales(driver)
        gf.Navegar(url,t)
        gf.Click_ID_Validar(login_button,t)
        gf.Texto_ID_Validar(username_field,user,t)
        gf.Texto_ID_Validar(password_field, user_password,t)
        gf.Click_Xpath_Validar(login_confirmation,t)

    def go_and_click(self,xpath, t):
        driver = self.driver
        gf = Funciones_Globales(driver)
        gf.scroll_to_element(xpath, t)
        gf.Click_Xpath_Validar(xpath, t)

    def rellenar_formulario_compra(self,name_field, user_name, country_field, country, city_field, city, creditCard_field, creditCard, month_field, month, year_field, year, t):
        driver = self.driver
        gf = Funciones_Globales(driver)
        gf.Texto_Xpath_Validar(name_field, user_name, t)
        gf.Texto_Xpath_Validar(country_field, country, t)
        gf.Texto_Xpath_Validar(city_field, city, t)
        gf.Texto_Xpath_Validar(creditCard_field, creditCard, t)
        gf.Texto_Xpath_Validar(month_field, month, t)
        gf.Texto_Xpath_Validar(year_field, year, t)
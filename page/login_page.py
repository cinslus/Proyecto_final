from selenium.webdriver.common.by import By # permite importar selectores 
# funcion constructor se ejecuta automaticamente se cree el objeto
from utils.logger import logger
class loginPage:
    def __init__(self,driver):
        self.driver = driver    #define que se va a guardar el navegador dentro de la clase
        #selectores
        self.username_input = (By.ID,"user-name")
        self.password_input = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
        self.error_login = (By.CSS_SELECTOR,"[data-test='error']")
        

    def open(self): # abre el navegador
        try:
            self.driver.get("https://www.saucedemo.com/")
        except:
            logger.critical("No se pudo conectar con la pagina")
        
    def ingresar_usuario(self,usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario)
        
    def ingresar_password(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        
    def login(self,usuario, password): 
        self.open()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()   
        
    def get_error_login_message(self): 
        try:
            return self.driver.find_element(*self.error_login).text #captura el error de login invalido
        except:
            logger.warning("No se pudo capturar el error")
            

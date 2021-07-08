from bs4.element import PageElement
from selenium.webdriver import Chrome
from time import sleep
from forms import Form

from selenium.webdriver.remote.webelement import WebElement

class SeleniumManager():
    def __init__(self):
        self.driver = Chrome("extra/chromedriver.exe")
    
    #Connects the webdriver to the url.
    def connect(self, url):
        self.get_driver().get(url)
        sleep(1)
        return

    #Selects by id.
    def select_by_id(self, id):
        return self.get_driver().find_element_by_id(id)

    #Selects by class name.
    def select_by_class(self, class_name):
        return self.get_driver().find_element_by_class_name(class_name)

    #Selects all with the same class.
    def select_all_by_class(self, class_name):
        return self.get_driver().find_elements_by_class_name(class_name)

    #Performs the click.
    def click(self, element:WebElement):
        element.click()

    #Checks if element text is the same of the condition given.
    def check_text_condition(self, element:WebElement, condition):
        if(element.text.lower() == condition.lower()):
            return True
        
        return False

    #Fill the form fields using a Form() object.
    #Form values and Element field values must be in the same order.
    def fill_form(self, fields, form:Form):
        form_values = form.get_listof_values()
        i = 0
        for field in fields:
            if ('submit' in field.get_attribute('type')):
                self.click(field)
            else:
                field.send_keys(form_values[i])
                i += 1 

    #Ends the webdriver session.
    def terminate(self):
        self.driver.quit()
        return        

    ### Gets and Sets ###

    def get_driver(self):
        return self.driver

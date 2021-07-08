

class Form():

    def __init__(self, name, subject, phone, company, email, website, message):
        self.name = name
        self.subject = subject
        self.phone = phone
        self.company = company
        self.email = email
        self.website = website
        self.message = message

    #Returns a list with all the Object values.
    def get_listof_values(self):
        values = [
            self.get_name(),
            self.get_subject(),
            self.get_phone(),
            self.get_company(),
            self.get_email(),
            self.get_website(),
            self.get_message()
        ]
        return values

    ### Gets and Sets ###

    def get_name(self):
        return self.name

    def get_subject(self):
        return self.subject
    
    def get_phone(self):
        return self.phone

    def get_company(self):
        return self.company

    def get_email(self):
        return self.email
    
    def get_website(self):
        return self.website

    def get_message(self):
        return self.message

    def set_name(self, name):
        self.name = name
    
    def set_subject(self, subject):
        self.subject = subject
    
    def set_phone(self, phone):
        self.phone = phone
    
    def set_company(self, company):
        self.company = company

    def set_email(self, email):
        self.email = email

    def set_website(self, website):
        self.website = website
    
    def set_message(self, message):
        self.message = message
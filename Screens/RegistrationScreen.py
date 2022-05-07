from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
import re

import database_handler

class RegistrationScreen(MDScreen):

    def verify_password_strength(self, password):
        if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!%*#?&])[\w\d@$!%*#?&]{6,12}$", password):
            return True
        else:
            return False

    def register(self):
        username = self.ids.username.text
        password = self.ids.password.text

        password_check = self.verify_password_strength(password)
        if password_check:
            print('register')
        else:
            MDDialog(title="Password should at least have\n"
                           "at least one digit\n"
                           "at least one uppercase letter\n"
                           "at least one lowercase letter\n"
                           "at least one special character\n").open()
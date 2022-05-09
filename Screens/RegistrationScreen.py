from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
import re

import database_handler

class RegistrationScreen(MDScreen):

    # method to check if the username meets the standards (check the snackbar below for detailed rules)
    def verify_username_structure(self, username):
        if re.match(r"^[A-Za-z][A-Za-z0-9_]{4,15}$", username):
            return True
        else:
            return False

    # method to check if the password meets the standards (check the snackbar below for detailed rules)
    def verify_password_strength(self, password):
        if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!%*#?&])[\w\d@$!%*#?&]{5,12}$", password):
            return True
        else:
            return False

    def register(self):
        username = self.ids.username.text
        password = self.ids.password.text

        username_check = self.verify_username_structure(username)
        password_check = self.verify_password_strength(password)

        if username_check and password_check:
            execute_command = database_handler.register_user(username, password, "user")

            if execute_command:
                database_handler.store_to_log('user registered successfully')
                Snackbar(text="User registered Successfully").open()
            else:
                Snackbar(text="username already taken").open()
        else:
            database_handler.store_to_log('unsuccessful user registration')
            MDDialog(title="Username (5-16 characters):\n"
                           "should start with an alphabet\n"
                           "can have alphabets, numbers or an underscore\n"
                           "\n"
                           "Password (6-12 characters) should at least have:\n"
                           "one digit\n"
                           "one uppercase letter\n"
                           "one lowercase letter\n"
                           "one special character [@$!%*#?&]\n").open()
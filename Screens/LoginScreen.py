from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

import StaticPages
import database_handler

class LoginScreen(MDScreen):

    def login(self):
        # fetch login credentials from teh screen
        username = self.ids.username.text
        password = self.ids.password.text

        # check if the credentials are valid using the DB
        login_check = database_handler.check_password(username, password)

        if login_check:
            StaticPages.is_logged_in = True
            StaticPages.username = username
            database_handler.store_to_log('logged in')
            Snackbar(text="Login successful").open()
        else:
            StaticPages.is_logged_in = False
            StaticPages.username = ''
            database_handler.store_to_log('failed to login')
            Snackbar(text="invalid username/password").open()

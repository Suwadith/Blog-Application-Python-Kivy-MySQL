from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

import StaticPages
import database_handler

# store = JsonStore('storage.json')

class LoginScreen(MDScreen):

    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        login_check = database_handler.check_password(username, password)

        if login_check:
            # print("valid")
            # store.put('is_logged_in', value=True)
            # store.put('username', value=username)
            StaticPages.is_logged_in = True
            StaticPages.username = username
            Snackbar(text="Login successful").open()
        else:
            StaticPages.is_logged_in = False
            StaticPages.username = ''
            Snackbar(text="invalid username/password").open()
            # print("invalid")



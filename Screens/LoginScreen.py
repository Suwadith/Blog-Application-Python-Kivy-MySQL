from kivy.storage.jsonstore import JsonStore
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

import database_handler

store = JsonStore('hello.json')

class LoginScreen(MDScreen):
    pass

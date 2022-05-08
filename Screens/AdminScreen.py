from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField
from plyer import filechooser


import StaticPages
import database_handler
import encryption

class AdminScreen(MDScreen):
    pass
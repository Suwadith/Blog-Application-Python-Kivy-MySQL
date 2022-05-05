from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.factory import Factory
# from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

import database_handler


class BlogAndJournal(MDApp):
    def build(self):
        return Builder.load_file('Toolbar.kv')

    def public_home_page(self):

        # Snackbar(text="This is a snackbar!").open()
        results = database_handler.get_public_blog_post()
        print(results)
        print("Public")

    def members_home_page(self):
        print("Members")

    def private_home_page(self):
        print("Private")

    def create_post(self):
        print("Create Post")

    def admin_page(self):
        print("Admin")

    def login_logout(self):
        print("Login/Logout")


BlogAndJournal().run()
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window

import StaticPages
from Screens.CreatePostScreen import CreatePostScreen
from Screens.LoginScreen import LoginScreen
from Screens.MemberScreen import MemberScreen
from Screens.PrivateScreen import PrivateScreen
from Screens.PublicScreen import PublicScreen
from Screens.RegistrationScreen import RegistrationScreen


class ScreenManager(ScreenManager):
    pass

sm = ScreenManager()
sm.add_widget(PublicScreen(name='public'))
sm.add_widget(MemberScreen(name='member'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegistrationScreen(name='registration'))
sm.add_widget(CreatePostScreen(name='create_post'))
sm.add_widget(PrivateScreen(name='private'))


class BlogAndJournal(MDApp):

    def build(self):
        return Builder.load_file('Main.kv')

BlogAndJournal().run()

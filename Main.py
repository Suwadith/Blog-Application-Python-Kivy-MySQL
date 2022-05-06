from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore

from Screens.LoginScreen import LoginScreen
from Screens.MemberScreen import MemberScreen
from Screens.PublicScreen import PublicScreen

store = JsonStore('hello.json')
store.put('is_logged_in', value=False)


class RegistrationScreen(MDScreen):
    pass



class ScreenManager(ScreenManager):
    is_logged_in = False

sm = ScreenManager()
sm.add_widget(PublicScreen(name='public'))
sm.add_widget(MemberScreen(name='member'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegistrationScreen(name='registration'))


class BlogAndJournal(MDApp):

    def build(self):

        return Builder.load_file('Main.kv')


BlogAndJournal().run()

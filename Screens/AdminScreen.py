from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.gridlayout import MDGridLayout
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

    def load_logs(self):
        if StaticPages.is_logged_in and StaticPages.username=='admin':
            results = database_handler.retrieve_logs()

            for log in results:

                timestamp = MDLabel(
                    text=str(log[6])
                )
                activity = MDLabel(
                    text=log[1]
                )
                username = MDLabel(
                    text=log[2]
                )
                ip_address = MDLabel(
                    text=log[3]
                )
                location = MDLabel(
                    text=log[4]
                )
                device = MDLabel(
                    text=log[5]
                )

                self.ids.logs.add_widget(timestamp)
                self.ids.logs.add_widget(activity)
                self.ids.logs.add_widget(username)
                self.ids.logs.add_widget(ip_address)
                self.ids.logs.add_widget(location)
                self.ids.logs.add_widget(device)

        else:
            Snackbar(text="Only admin can view the logs").open()
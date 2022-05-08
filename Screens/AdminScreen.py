from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

import StaticPages
import database_handler

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
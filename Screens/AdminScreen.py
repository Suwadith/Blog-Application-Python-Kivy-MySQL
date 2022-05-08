from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

import StaticPages
import database_handler

class AdminScreen(MDScreen):

    # load all logs
    def load_logs(self):
        # check if user is logged in, and it is the admin
        if StaticPages.is_logged_in and StaticPages.username=='admin':
            # retrieve activities from logs table
            results = database_handler.retrieve_logs()
            # iterate all the log entries received
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

                # attach all the logs to the screen
                self.ids.logs.add_widget(timestamp)
                self.ids.logs.add_widget(activity)
                self.ids.logs.add_widget(username)
                self.ids.logs.add_widget(ip_address)
                self.ids.logs.add_widget(location)
                self.ids.logs.add_widget(device)

        else:
            # Error popup
            Snackbar(text="Only admin can view the logs").open()
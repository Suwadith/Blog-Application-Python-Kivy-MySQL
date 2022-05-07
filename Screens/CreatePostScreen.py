from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window


import StaticPages
import database_handler


class CreatePostScreen(MDScreen):

    is_member_only = "public"

    def checkbox_click(self, instance, value):
        if value is True:
            self.is_member_only = "member"
        else:
            self.is_member_only = "public"

    def create_post(self):
        if StaticPages.is_logged_in:

            title = self.ids.title.text
            body = self.ids.body.text
            visibility = self.is_member_only
            username = StaticPages.username

            result = database_handler.store_blog_post(title, body, visibility, username)

            if result:
                Snackbar(text="Successfully posted").open()
            else:
                Snackbar(text="Error occurred while trying to post").open()

        else:
            Snackbar(text="Please login to make posts").open()

        self.ids.title.text = ''
        self.ids.body.text = ''

from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from plyer import filechooser

import StaticPages
import database_handler


class CreatePostScreen(MDScreen):

    def file_chooser(self, **kwargs):
        filechooser.open_file(on_selection=self.selected, **kwargs)

    def selected(self, selection):
        print(selection[0])
        StaticPages.file_path = selection[0]

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
            file_path = StaticPages.file_path

            if file_path is None:
                result = database_handler.store_blog_post(title, body, visibility, username)
            else:
                result = database_handler.store_blog_post_with_file(title, body, visibility, username, file_path)

            if result:
                database_handler.store_to_log('created post')
                Snackbar(text="Successfully posted").open()
            else:
                Snackbar(text="Error occurred while trying to post").open()

        else:
            Snackbar(text="Please login to make posts").open()

        self.ids.title.text = ''
        self.ids.body.text = ''
        StaticPages.file_path = None

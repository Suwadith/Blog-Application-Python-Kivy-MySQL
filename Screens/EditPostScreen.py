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


class EditPostScreen(MDScreen):

    def update_post(self):
        title = self.post_title.text
        body = self.post_body.text
        blog_id = self.result[0]

        # print(title)
        # print(body)
        # print(blog_id)

        result = database_handler.update_post(title, body, blog_id)

        if result:
            database_handler.store_to_log('edited post')
            Snackbar(text="Successfully updated").open()
        else:
            Snackbar(text="Error occurred while trying to update").open()

    def load_post_to_edit(self):
        self.result = database_handler.get_post_by_id(StaticPages.edit_blog_id)
        # print(result)

        self.ids.post.clear_widgets()
        self.post_card = MDCard(
            orientation="vertical",
            size_hint=[None, None],
            size=["500dp", "500dp"],
            pos_hint={"center_x": .5, "center_y": .5},
            padding="20dp",
            spacing="25dp"
        )
        self.title = MDLabel(
            halign="center",
            text="Edit Post"
        )
        self.post_title = MDTextField(
            hint_text="Blog Title",
            text=encryption.decrypt_message(self.result[2]),
            mode="rectangle"
        )
        self.post_body = MDTextField(
            hint_text="Body",
            text=encryption.decrypt_message(self.result[3]),
            mode="rectangle",
            multiline=True,
            max_height="100dp"
        )
        self.update_post_button = MDRaisedButton(
            pos_hint={"center_x": .5, "center_y": .5},
            text="UPDATE",
            on_press=lambda x: self.update_post()
        )


        # post_attachment = MDLabel(text=(base64.b64decode(post[4])))
        # author_name = MDLabel(
        #     text=post[6],
        #     halign="right",
        #     theme_text_color="Secondary",
        #     size_hint_y=None,
        #     height="20dp"
        # )

        # box_layout = MDBoxLayout(
        #     orientation="horizontal",
        #     spacing="15dp"
        # )
        #
        # update_button = MDRaisedButton(
        #     pos_hint={"center_x": .5, "center_y": .5},
        #     text="Update",
        #     on_press=lambda x: self.update_post(result[0])
        # )

        self.post_card.add_widget(self.title)
        self.post_card.add_widget(self.post_title)
        # post_card.add_widget(post_timestamp)
        self.post_card.add_widget(self.post_body)
        self.post_card.add_widget(self.update_post_button)
        # post_card.add_widget(author_name)
        # post_card.add_widget(box_layout)
        # box_layout.add_widget(update_button)

        self.ids.post.add_widget(self.post_card)
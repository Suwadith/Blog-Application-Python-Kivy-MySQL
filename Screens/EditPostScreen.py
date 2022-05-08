from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField

import StaticPages
import database_handler
import encryption


class EditPostScreen(MDScreen):

    def update_post(self):
        title = self.post_title.text
        body = self.post_body.text
        blog_id = self.result[0]

        result = database_handler.update_post(title, body, blog_id)

        if result:
            database_handler.store_to_log('edited post')
            Snackbar(text="Successfully updated").open()
        else:
            Snackbar(text="Error occurred while trying to update").open()

    def load_post_to_edit(self):
        self.result = database_handler.get_post_by_id(StaticPages.edit_blog_id)

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

        self.post_card.add_widget(self.title)
        self.post_card.add_widget(self.post_title)
        self.post_card.add_widget(self.post_body)
        self.post_card.add_widget(self.update_post_button)

        self.ids.post.add_widget(self.post_card)
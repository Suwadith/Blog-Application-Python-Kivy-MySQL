from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from functools import partial
import magic

import StaticPages
import database_handler
import encryption


class PrivateScreen(MDScreen):

    player = None
    image = None
    audio_button = None

    def play_audio(self, audio_path, instance):
        sound = SoundLoader.load(audio_path)
        sound.play()

    # method to delete a specific post based on the blog_id
    def delete_post(self, blog_id, instance):
        result = database_handler.delete_blog_post(blog_id)

        if result:
            database_handler.store_to_log('deleted post')
            Snackbar(text="Successfully Deleted the post").open()
        else:
            Snackbar(text="Error occurred").open()

        self.load_posts()

    # edit the post by fetching the blog_id and move to the edit screen
    def edit_post(self, blog_id, instance):
        StaticPages.edit_blog_id = blog_id
        self.parent.current = "edit"

    def load_posts(self):
        self.ids.posts.clear_widgets()
        if StaticPages.is_logged_in:
            database_handler.store_to_log('accessed personal page section')
            results = database_handler.get_user_blog_posts(StaticPages.username)
            for post in results:

                self.player = None
                self.image = None
                self.audio_button = None

                post_card = MDCard(
                    orientation="vertical",
                    padding="20dp",
                    size_hint=[None, None],
                    size=["500dp", "600dp"],
                    pos_hint={"center_x": .5, "center_y": .5}
                )

                post_title = MDLabel(
                    halign="center",
                    text=encryption.decrypt_message(post[2]),
                    theme_text_color="Secondary",
                    size_hint_y=None,
                    height="40dp"
                )

                title_separator = MDSeparator(
                    height="1dp"
                )

                post_body = MDLabel(
                    text=encryption.decrypt_message(post[3])
                )

                if post[4] is not None:
                    file_type = (magic.from_file(str(post[4]), mime=True)).split("/")[0]

                    if file_type == "image":
                        self.image = Image(source=str(post[4]))
                    elif file_type == "video":
                        self.player = VideoPlayer(source=str(post[4]))
                    elif file_type == "audio":
                        self.audio_button = MDRaisedButton(
                            pos_hint={"center_x": .5, "center_y": .5},
                            text="Play audio"
                        )
                        audio_button_callback = partial(self.play_audio, str(post[4]))
                        self.audio_button.bind(on_press=audio_button_callback)

                attachment_separator = MDSeparator(
                    height="1dp"
                )

                box_layout = MDBoxLayout(
                    orientation="horizontal",
                    spacing="15dp"
                )

                delete_button = MDRaisedButton(
                    pos_hint={"center_x": .5, "center_y": .5},
                    text="Delete"
                )
                delete_button_callback = partial(self.delete_post, post[0])
                delete_button.bind(on_press=delete_button_callback)

                edit_button = MDRaisedButton(
                    pos_hint={"center_x": .5, "center_y": .5},
                    text="Edit"
                )
                edit_button_callback = partial(self.edit_post, post[0])
                edit_button.bind(on_press=edit_button_callback)

                post_card.add_widget(post_title)
                post_card.add_widget(title_separator)
                post_card.add_widget(post_body)

                if self.player is not None:
                    post_card.add_widget(self.player)
                if self.image is not None:
                    post_card.add_widget(self.image)
                if self.audio_button is not None:
                    post_card.add_widget(self.audio_button)

                post_card.add_widget(attachment_separator)
                post_card.add_widget(box_layout)
                box_layout.add_widget(delete_button)
                box_layout.add_widget(edit_button)

                self.ids.posts.add_widget(post_card)

        else:
            Snackbar(text="Please login to view your own posts").open()

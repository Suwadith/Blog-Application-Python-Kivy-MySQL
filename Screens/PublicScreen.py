from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from functools import partial
import magic

import database_handler
import encryption


class PublicScreen(MDScreen):

    player = None
    image = None
    audio_button = None

    # method to play the audio file
    def play_audio(self, audio_path, instance):
        sound = SoundLoader.load(audio_path)
        sound.play()

    # method to load posts
    def load_posts(self):
        self.ids.posts.clear_widgets()
        database_handler.store_to_log('accessed public posts section')
        results = database_handler.get_public_blog_post()
        for post in results:

            self.player = None
            self.image = None
            self.audio_button = None

            post_card = MDCard(
                orientation="vertical",
                padding="20dp",
                size_hint=[None, None],
                size=["500dp", "500dp"],
                pos_hint={"center_x": .5, "center_y": .5}
            )

            post_title = MDLabel(
                halign="center",
                text=str(encryption.decrypt_message(post[2])),
                theme_text_color="Secondary",
                size_hint_y=None,
                height="40dp"
            )

            title_separator = MDSeparator(
                height="1dp"
            )

            post_timestamp = MDLabel(
                text=str(post[1]),
                halign="right",
                theme_text_color="Secondary",
                size_hint_y=None,
                height="20dp"
            )

            post_body = MDLabel(
                text=str(encryption.decrypt_message(post[3])),
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

            author_name = MDLabel(
                text=post[6],
                halign="right",
                theme_text_color="Secondary",
                size_hint_y=None,
                height="20dp"
            )

            post_card.add_widget(post_title)
            post_card.add_widget(title_separator)
            post_card.add_widget(post_timestamp)
            post_card.add_widget(post_body)

            if self.player is not None:
                post_card.add_widget(self.player)
            if self.image is not None:
                post_card.add_widget(self.image)
            if self.audio_button is not None:
                post_card.add_widget(self.audio_button)

            post_card.add_widget(attachment_separator)
            post_card.add_widget(author_name)

            self.ids.posts.add_widget(post_card)

from kivy.storage.jsonstore import JsonStore
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
import StaticPages

import database_handler

# store = JsonStore('storage.json')
import encryption


class MemberScreen(MDScreen):

    def load_posts(self):
        self.ids.posts.clear_widgets()
        # if store.get('is_logged_in')['value']:
        if StaticPages.is_logged_in:
            # print('in')
            # session
            results = database_handler.get_member_blog_post()
            for post in results:
                post_card = MDCard(
                    orientation="vertical",
                    padding="20dp",
                    size_hint=[None, None],
                    size=["500dp", "500dp"],
                    pos_hint={"center_x": .5, "center_y": .5},
                    # size=self.size
                    # adaptive_height=True
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
                post_timestamp = MDLabel(
                    text=str(post[1]),
                    halign="right",
                    theme_text_color="Secondary",
                    # pos_hint={"top": 0}
                    size_hint_y=None,
                    height="20dp"
                )
                post_body = MDLabel(
                    text=encryption.decrypt_message(post[3]),
                    # size_hint_y=None
                    # height='10dp'
                )
                # post_attachment = MDLabel(text=(base64.b64decode(post[4])))
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
                post_card.add_widget(author_name)
                # post_card.add_widget(post_attachment)

                self.ids.posts.add_widget(post_card)

        else:
            Snackbar(text="Please login to view member restricted posts").open()

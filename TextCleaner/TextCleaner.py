from TextCleaner import *

class TextCleaner:
    def __init__(self, spaces: True, punctuation: True, html: True, emoji: True, lower: True):
        self.spaces = spaces
        self.punctuation = punctuation
        self.html = html
        self.emoji = emoji
        self.lower = lower

        self.to_lower = to_lower_text
        self.clean_emoji = clean_emoji
        self.clean_punctuation = clean_punctuation
        self.clean_html = clean_html
        self.clean_space = clean_spaces

    def clean_text(self, text: str) -> str:
        pass
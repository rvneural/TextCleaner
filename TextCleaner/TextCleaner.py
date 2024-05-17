from TextCleaner import *


class TextCleaner:
    def __init__(self, spaces=True, punctuation=True, html=True, emoji=True, lower=True,
                 stopwords=True, morpheme=True):
        self.spaces = spaces
        self.punctuation = punctuation
        self.html = html
        self.emoji = emoji
        self.lower = lower
        self.stopwords = stopwords
        self.morpheme = morpheme

        self.to_lower = to_lower_text
        self.clean_emoji = clean_emoji
        self.clean_punctuation = clean_punctuation
        self.clean_html = clean_html
        self.clean_space = clean_spaces
        self.clean_stopwords = clean_stopwords
        self.to_morpheme = text_to_morphems

    def clean_text(self, text: str, language: str) -> str:
        if self.lower:
            text = self.to_lower(self, text)
        if self.emoji:
            text = self.clean_emoji(self, text)
        if self.html:
            text = self.clean_html(self, text)
        if self.spaces:
            text = self.clean_space(self, text)
        if self.punctuation:
            text = self.clean_punctuation(self, text)
        if self.stopwords:
            text = self.clean_stopwords(self, text, language)
        if self.morpheme:
            text = self.to_morpheme(self, text, language)

        return text

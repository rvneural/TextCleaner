import _clean_stopwords
import _emoji_cleaner
import _html_cleaner
import _punctuation_cleaner
import _spaces_cleaner
import _to_lower
import _to_morpheme


class TextCleaner:
    def __init__(self, spaces=True, punctuation=True, html=True, emoji=True, lower=True,
                 stop_words=True, morpheme=True):

        """
        Метод __init__ инциализирует экземпляр класса TextCleaner

        self.spaces = spaces - Необходимо ли удалять пробелы
        self.punctuation = punctuation - Необходимо ли удалять пунктуацию
        self.html = html - Необходимо ли удалять теги HTML
        self.emoji = emoji - Необходимо ли удалять Emoji
        self.lower = lower - Необходимо ли переводить текст в нижний регистр
        self.stopwords = stop_words - Необходимо ли удалять стоп слова
        self.morpheme = morpheme - Необходимо ли заменять слова на морфемы

        """

        self.spaces = spaces
        self.punctuation = punctuation
        self.html = html
        self.emoji = emoji
        self.lower = lower
        self.stopwords = stop_words
        self.morpheme = morpheme

        self.to_lower = _to_lower
        self.clean_emoji = _emoji_cleaner
        self.clean_punctuation = _punctuation_cleaner
        self.clean_html = _html_cleaner
        self.clean_space = _spaces_cleaner
        self.clean_stopwords = _clean_stopwords
        self.to_morpheme = _to_morpheme

    def clean_text(self, text: str) -> str:

        """ Метод clean_text форматирует текст в зависимости от поставленных флагов"""

        if self.lower:
            text = self.to_lower(self, text)
        if self.emoji:
            text = self.clean_emoji(self, text)
        if self.html:
            text = self.clean_html(self, text)
        if self.punctuation:
            text = self.clean_punctuation(self, text)
        if self.stopwords:
            text = self.clean_stopwords(self, text)
        if self.morpheme:
            text = self.to_morpheme(self, text)
        if self.spaces:
            text = self.clean_space(self, text)

        return text

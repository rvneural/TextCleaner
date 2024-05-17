from src.ru_text_cleaner import *


def clean_emoji(self, text: str) -> str:

    """
        Функция clean_emoji удаляет все emoji из текста

        moji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"
                                   u"\U0001F300-\U0001F5FF"
                                   u"\U0001F680-\U0001F6FF"
                                   u"\U0001F1E0-\U0001F1FF"
                                   "]+", flags=re.UNICODE)
        Коомпилирует шаблон эмодзи

        return emoji_pattern.sub(r'', text) - Возвращает текст без emoji

        Параметры
        ------
            "[" u"\U0001F600-\U0001F64F" u"\U0001F300-\U0001F5FF" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" "]+" - шаблон с эмодзи
            flags=re.UNICODE - флаг кодировки
            r'' - заменяет emoji на пустоту
        """

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


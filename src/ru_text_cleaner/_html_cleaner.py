from src.ru_text_cleaner import *


def clean_html(self, text: str) -> str:
    return re.sub('<[^<]+?>', '', text)

from src.TextCleaner import *


def clean_html(self, text: str) -> str:
    return re.sub('<[^<]+?>', '', text)

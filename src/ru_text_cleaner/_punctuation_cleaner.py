from src.ru_text_cleaner import *


def clean_punctuation(self, text: str) -> str:
    return ''.join(i for i in text if i not in string.punctuation)

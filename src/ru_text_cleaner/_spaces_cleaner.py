from src.ru_text_cleaner import *


def clean_spaces(self, text: str) -> str:
    text = re.sub(r' +', ' ', text)
    return text.strip()

from src.TextCleaner import *


def clean_spaces(self, text: str) -> str:
    text = re.sub(r' +', ' ', text)
    return text.strip()

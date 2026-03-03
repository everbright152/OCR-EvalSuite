import easyocr
import time
from .base_engine import BaseOCREngine


class EasyOCREngine(BaseOCREngine):
    def __init__(self, languages=None):
        super().__init__("easyocr")

        if languages is None:
            languages = ['en']

        self.reader = easyocr.Reader(languages)

    def recognize(self, image_path: str, lang: str):
        start = time.time()

        results = self.reader.readtext(image_path)
        text = " ".join([res[1] for res in results])

        end = time.time()

        return text.strip(), None, end - start
        
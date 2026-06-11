# services/ocr_service.py

import mss
import pytesseract

from PIL import (
    Image,
    ImageOps,
    ImageEnhance
)

from config.settings import settings


pytesseract.pytesseract.tesseract_cmd = (
    settings.TESSERACT_PATH
)


class OCRService:

    def _capture_screen(self) -> Image.Image:

        with mss.mss() as sct:

            screenshot = sct.grab(
                sct.monitors[1]
            )

            image = Image.frombytes(
                "RGB",
                screenshot.size,
                screenshot.rgb
            )

            # Escala de cinza
            image = ImageOps.grayscale(
                image
            )

            # Aumenta contraste
            contrast = (
                ImageEnhance.Contrast(
                    image
                )
            )

            image = contrast.enhance(
                3.0
            )

            return image

    def read_screen(self) -> str:

        image = self._capture_screen()

        return (
            pytesseract
            .image_to_string(image)
        )

    def find_word_location(
        self,
        target_word: str
    ) -> tuple[int, int] | None:

        image = self._capture_screen()

        data = pytesseract.image_to_data(
            image,
            output_type=pytesseract.Output.DICT
        )

        total_words = len(
            data["text"]
        )

        for i in range(total_words):

            word = (
                data["text"][i]
                .strip()
                .lower()
            )

            if word != target_word.lower():
                continue

            x = data["left"][i]
            y = data["top"][i]
            w = data["width"][i]
            h = data["height"][i]

            center_x = x + w // 2
            center_y = y + h // 2

            return (
                center_x,
                center_y
            )

        return None
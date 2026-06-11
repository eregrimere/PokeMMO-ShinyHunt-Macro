# config/settings.py

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:

    TESSERACT_PATH = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    WAIT_AFTER_C = 22

    SHINY_WORD = "shiny"

    STOP_KEY = "p"

    DISCORD_WEBHOOK_URL = (
    ""
)

    ESCAPE_X = 605
    ESCAPE_Y = 748

    SHINY_X_1 = 634
    SHINY_Y_1 = 706

    SHINY_X_2 = 1578
    SHINY_Y_2 = 755


settings = Settings()
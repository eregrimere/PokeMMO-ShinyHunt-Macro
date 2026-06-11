# main.py

from services.ocr_service import OCRService
from services.keyboard_service import KeyboardService
from services.mouse_service import MouseService
from services.discord_service import DiscordService

from config.settings import settings

from usecases.shiny_hunter import (
    ShinyHunter,
    StopProgramException
)


def main():

    try:

        shiny_hunter = ShinyHunter(
            ocr_service=OCRService(),
            keyboard_service=KeyboardService(),
            mouse_service=MouseService(),
            discord_service=DiscordService(
                settings.DISCORD_WEBHOOK_URL
            )
        )

        shiny_hunter.execute()

    except StopProgramException:

        print(
            "\nPrograma encerrado pelo usuário."
        )

    except KeyboardInterrupt:

        print(
            "\nPrograma interrompido."
        )

    except Exception as exception:

        print(
            f"\nErro inesperado: {exception}"
        )


if __name__ == "__main__":
    main()
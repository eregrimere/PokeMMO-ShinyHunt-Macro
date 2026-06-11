# usecases/shiny_hunter.py

import time

from pynput.keyboard import Listener

from config.settings import settings


class StopProgramException(Exception):
    pass


class ShinyHunter:

    def __init__(
        self,
        ocr_service,
        keyboard_service,
        mouse_service,
        discord_service
    ):
        self.ocr_service = ocr_service
        self.keyboard_service = keyboard_service
        self.mouse_service = mouse_service
        self.discord_service = discord_service

        self.stop_requested = False

        self.shiny_notification_sent = False

    def _on_press(self, key):

        try:

            if (
                key.char.lower()
                == settings.STOP_KEY.lower()
            ):
                self.stop_requested = True

        except Exception:
            pass

    def execute(self):

        print("Shiny Hunter iniciado.")
        print(
            f"Pressione '{settings.STOP_KEY.upper()}' para encerrar."
        )

        listener = Listener(
            on_press=self._on_press
        )

        listener.start()

        while not self.stop_requested:

            self._start_cycle()

        raise StopProgramException()

    def _start_cycle(self):

        print("Pressionando C...")

        self.keyboard_service.press_c()

        print(
            f"Aguardando {settings.WAIT_AFTER_C} segundos..."
        )

        for _ in range(
            settings.WAIT_AFTER_C
        ):

            if self.stop_requested:
                raise StopProgramException()

            time.sleep(1)

        text = (
            self.ocr_service
            .read_screen()
            .lower()
        )

        if (
            settings.SHINY_WORD
            in text
        ):

            self._handle_shiny()

            return

        self._handle_escape()

    def _handle_shiny(self):

        print("SHINY ENCONTRADO!")

        if not self.shiny_notification_sent:

            try:

                self.discord_service.send_shiny_found()

                self.shiny_notification_sent = True

                print(
                    "Webhook enviado para o Discord."
                )

            except Exception as exception:

                print(
                    f"Erro ao enviar webhook: "
                    f"{exception}"
                )

        while not self.stop_requested:

            self.mouse_service.move_and_click(
                settings.SHINY_X_1,
                settings.SHINY_Y_1
            )

            time.sleep(0.5)

            if self.stop_requested:
                raise StopProgramException()

            self.mouse_service.move_and_click(
                settings.SHINY_X_2,
                settings.SHINY_Y_2
            )

            time.sleep(0.5)

        raise StopProgramException()

    def _handle_escape(self):

        print(
            "Shiny não encontrado."
        )

        time.sleep(0.5)

        self.mouse_service.move_and_click(
            settings.ESCAPE_X,
            settings.ESCAPE_Y
        )

        print(
            f"Clique realizado em "
            f"({settings.ESCAPE_X}, "
            f"{settings.ESCAPE_Y})"
        )

        print(
            "Aguardando 7 segundos..."
        )

        for _ in range(7):

            if self.stop_requested:
                raise StopProgramException()

            time.sleep(1)
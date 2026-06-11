# services/mouse_service.py

import pyautogui


class MouseService:

    def move_to(
        self,
        x: int,
        y: int
    ) -> None:

        pyautogui.moveTo(
            x,
            y,
            duration=0.3
        )

    def click(
        self,
        x: int,
        y: int
    ) -> None:

        pyautogui.click(x, y)

    def move_and_click(
        self,
        x: int,
        y: int
    ) -> None:

        self.move_to(x, y)

        pyautogui.click()
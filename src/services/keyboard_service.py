# services/keyboard_service.py

import pyautogui


class KeyboardService:

    def press_c(self) -> None:
        pyautogui.press("c")

    def left(self) -> None:
        pyautogui.press("a")

    def right(self) -> None:
        pyautogui.press("d")

    def press(self, key: str) -> None:
        pyautogui.press(key)
# Shiny Hunter Macro

## Overview

Shiny Hunter Macro is a Python automation project designed to detect shiny encounters using Optical Character Recognition (OCR).

The application continuously performs automated cycles, captures the screen, processes the image with OCR, and searches for a target keyword.

## Configuration Notes

- The application assumes that **Sweet Scent** is bound to the **"C"** key.
- Mouse coordinates were recorded using a **1920×1080 monitor** with the game running in **windowed mode**. Users may need to recalibrate the coordinates to match their own display and window configuration.
- The application can be stopped at any time by pressing the **"P"** key.
- All timing-related settings, delays, and configurable parameters are centralized in `settings.py`.
- You can use `mouse_finder.py` to get coordinates.

When a Shiny is detected:

- A Discord webhook notification is sent.
- The application enters a waiting loop through automated mouse interactions.
- The program remains active until manually stopped by the user.

When a Shiny is not detected:

- The application automatically performs the escape action.
- Waits for a configurable delay.
- Starts a new detection cycle.

---

## Features

- Keyboard automation
- Mouse automation
- Screen capture
- OCR-based text detection
- Discord webhook notifications
- Global hotkey to stop execution
- Centralized configuration
- Modular architecture with clear separation of responsibilities

---

## Technologies

- Python 3.10+
- Tesseract OCR
- PyAutoGUI
- MSS
- Pillow
- Pytesseract
- Requests
- Pynput

---

## Project Structure

```text
src/
│
├── main.py
│
├── config/
│   └── settings.py
│
├── services/
│   ├── discord_service.py
│   ├── keyboard_service.py
│   ├── mouse_service.py
│   └── ocr_service.py
│
└── usecases/
    └── shiny_hunter.py
```

---

## Requirements

### Python

Install Python 3.10 or later.

---

## Installation

Install the required dependencies:

```bash
pip install pyautogui mss pillow pytesseract requests pynput
```

---

## Running the Application

Execute:

```bash
python main.py
```

or

```bash
python src/main.py
```

depending on your local project structure.

---

## Execution Flow

```text
Press C
↓
Wait configured time
↓
Capture screen
↓
OCR processing
↓
Shiny found?
├─ Yes
│   ↓
│   Send Discord webhook
│   ↓
│   Execute waiting loop
│
└─ No
    ↓
    Execute escape action
    ↓
    Wait
    ↓
    Restart cycle
```

---

## Skills and Concepts Applied

### Python Backend

- Modular project organization
- Dependency injection
- Exception handling
- Configuration management
- Separation of concerns

### Software Architecture

- Service Layer Pattern
- Use Case Layer
- Single Responsibility Principle (SRP)
- Clean Code practices
- Decoupled architecture

### Libraries and Tools

- Pytesseract
- Pillow
- MSS
- PyAutoGUI
- Requests
- Pynput
- Tesseract OCR

---

## Educational Purpose

This project was built to practice and demonstrate:

- Python Backend Development
- Desktop Automation
- OCR Integration
- API Integration
- Software Architecture
- Project Organization
- Clean Code Principles
- Dependency Management
- Maintainable and Scalable Code Design

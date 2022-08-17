# Obby-Trivia-Challenge-Bot
Python Bot that uses OCR to play an online trivia game

Essentially plays games of online trivia and saves questions as it sees them.
It started by guessing every question, but after leaving it overnight, it had most questions saved in the database and was winning every game.
Since the game text was not accessible (not a web game), the bot uses OCR to copy text.

This bot was designed for one online trivia game in mind, but this could easily be modified to any other trivia game

Built using:
- AutoHotKey Python Library (takes control of PC)
- Tesseract (For the OCR)
- CV2 (For image pre-processing with the OCR)
- MongoDB (Saves questions and answers in database after seeing them once)

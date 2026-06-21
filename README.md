# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.

The purpose of this game is for the user to guess the correct answer by using as few guesses as possible to have a higher score. According to the difficulty level, the user will have to guess from either a wider range of numbers or a lower number of allowed attempts.

- [ ] Detail which bugs you found.

Bug 1: The hint messages were reversed. For example if the user's guess is too low, the game will tell the user to go even lower instead of going higher.

Bug 2: The code converted the user input into a string and so it could lead the game to give false hint. For example with the case that the code compares "100" and "93", "100" would be considered as smaller than "93" because the single character "1" is smaller than "9".

Bug 3: The difficulty level didn't seem to be actually represented by either the number of attempts allowed or the number range. For instance, the "hard" mode didn't seem much harder than the "normal" mode because the number range was smaller for the "hard" mode, which is supposed to make the game easier.

Bug 4: The game couldn't be restarted by clicking the "New Game" button. When the button is clicked, the game doesn't restart and the user must reload the page or re-run the game from the terminal 


- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 50
2. Game returns "Too Low"
3. User enters a guess of 75 -> "Too Low"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*:
![Game UI screenshot](images/game_UI.png)

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/test_game_logic.py
# ========================= 5 passed in 0.01s =========================


```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

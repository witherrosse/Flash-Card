## Flash Card App - How it works

This is a **French to English flash card app** built with Tkinter. It helps you learn French words by showing cards that flip after 3 seconds.

### Project files

- `main.py` – the complete application (single file)
- `data/french_words.csv` – original word list
- `data/words_to_learn.csv` – saves words you still need to learn
- `images/` – card front, card back, right and wrong button images

### What is used

- `tkinter` module: for GUI window, buttons, and canvas
- `pandas` module: to read and write CSV files
- `random` module: to pick random cards
- `after()` method: to flip card after 3 seconds

### How it works

1. App loads French words from a CSV file
2. Shows a card with French word on front
3. You try to remember the English meaning
4. After 3 seconds, card flips to show English translation
5. You choose:
   - **Wrong button (X)** → card goes back to the learning list
   - **Right button (✓)** → card is removed from learning list
6. Remaining words save to `words_to_learn.csv`
7. Next time you open the app, only unknown words appear

### Controls

| Button | Action |
|--------|--------|
| X (Wrong) | Show next card, keep word in learning list |
| ✓ (Right) | Remove word from list, show next card |


### How the learning list works

- First time: uses all words from `french_words.csv`
- After each session: saves unknown words to `words_to_learn.csv`
- Next session: loads only the unknown words
- Known words are removed permanently (until you restart with fresh file)

---

Learn French words easily with this flash card app!

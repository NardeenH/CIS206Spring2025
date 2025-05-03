# Race against the clock to type words accurately.

import tkinter as tk
import random

# List of words for the game
words = [
    "python", "game", "timer", "copy", "code", "fast", "logic", "string", "window", "entry",
    "button", "submit", "hello", "orange", "pink", "label", "score", "canvas", "frame", "text",
    "mouse", "event", "value", "start", "check", "color", "right", "left", "while", "break",
    "class", "input", "print", "click", "timer", "guess", "match", "loop", "reset", "center"
]
score = 0
time_left = 10
current_word = ""

# Function to start a new round
def new_word():
    global current_word, time_left
    current_word = random.choice(words)
    label_word.config(text=current_word)
    entry.delete(0, tk.END)
    time_left = 10
    update_timer()

# Function to check if the typed word is correct
def check_word():
    global score
    typed = entry.get()
    if typed.lower() == current_word.lower():
        score += 1
        label_result.config(text="Correct!")
    else:
        label_result.config(text=f" Wrong! Word was: {current_word}")
    label_score.config(text=f"Score: {score}")
    window.after(1000, new_word)  # Small pause before next word

# Function to update the countdown
def update_timer():
    global time_left
    if time_left > 0:
        label_timer.config(text=f"Time: {time_left}")
        time_left -= 1
        window.after(1000, update_timer)
    else:
        label_result.config(text=f"⏰ Time's up! Word was: {current_word}")
        window.after(1000, new_word)  # Pause before next round

# --- GUI Setup ---
window = tk.Tk()
window.title("Copy the Word Game")
window.geometry("300x280")
window.configure(bg="#ffe6f0")  

label_intro = tk.Label(window, text="Copy the word before time runs out!", font=("Arial", 10), bg="#ffe6f0", fg="deeppink")
label_intro.pack(pady=5)

label_word = tk.Label(window, text="", font=("Arial", 20, "bold"), fg="blue", bg="#ffe6f0")
label_word.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=5)

btn_submit = tk.Button(window, text="Submit", command=check_word, bg="orange", fg="white", font=("Arial", 12, "bold"))
btn_submit.pack(pady=5)

window.bind('<Return>', lambda event: check_word())

label_result = tk.Label(window, text="", font=("Arial", 12), bg="#ffe6f0")
label_result.pack(pady=5)

label_score = tk.Label(window, text="Score: 0", font=("Arial", 12), bg="#ffe6f0")
label_score.pack()

label_timer = tk.Label(window, text="Time: 5", font=("Arial", 12), fg="red", bg="#ffe6f0")
label_timer.pack(pady=10)

# Start the first round
new_word()

window.mainloop()

import tkinter as tk
import random

def move_ball(event):
    global ball_x, ball_y
    key = event.keysym

    if key == "Up":
        ball_y -= 10
    elif key == "Down":
        ball_y += 10
    elif key == "Left":
        ball_x -= 10
    elif key == "Right":
        ball_x += 10

    canvas.coords(ball, ball_x, ball_y, ball_x + ball_size, ball_y + ball_size)
    check_goal()

def check_goal():
    global score
    ball_center_x = ball_x + ball_size // 2
    ball_center_y = ball_y + ball_size // 2
    dx = ball_center_x - hole_x
    dy = ball_center_y - hole_y
    distance = (dx**2 + dy**2)**0.5

    if distance < (hole_radius - ball_size // 2):
        score += 1
        label_score.config(text=f"Score: {score}")
        reset_ball()

def reset_ball():
    global ball_x, ball_y
    ball_x = random.choice([10, 250])
    ball_y = random.choice([10, 150])
    canvas.coords(ball, ball_x, ball_y, ball_x + ball_size, ball_y + ball_size)

window = tk.Tk()
window.title("Ball into the Hole Game")
window.geometry("300x250")

canvas = tk.Canvas(window, width=300, height=200, bg="white")
canvas.pack()

# Draw hole in center
hole_x, hole_y = 150, 100
hole_radius = 20
canvas.create_oval(hole_x - hole_radius, hole_y - hole_radius,
                   hole_x + hole_radius, hole_y + hole_radius, fill="black")

ball_size = 20
ball_x, ball_y = 10, 10
ball = canvas.create_oval(ball_x, ball_y, ball_x + ball_size, ball_y + ball_size, fill="pink")

score = 0
label_score = tk.Label(window, text="Score: 0", font=("Arial", 14))
label_score.pack(pady=5)

# Bind arrow keys
window.bind("<KeyPress>", move_ball)

window.mainloop()

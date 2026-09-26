import tkinter as tk
import random

# Game data
choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
emojis = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️",
    "Lizard": "🦎",
    "Spock": "🖖"
}

# Who beats who
rules = {
    "Rock": ["Scissors", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Lizard": ["Paper", "Spock"],
    "Spock": ["Rock", "Scissors"]
}

# Reasons for win
reasons = {
    ("Rock", "Scissors"): "Rock crushes Scissors",
    ("Rock", "Lizard"): "Rock crushes Lizard",
    ("Paper", "Rock"): "Paper covers Rock",
    ("Paper", "Spock"): "Paper disproves Spock",
    ("Scissors", "Paper"): "Scissors cuts Paper",
    ("Scissors", "Lizard"): "Scissors decapitates Lizard",
    ("Lizard", "Paper"): "Lizard eats Paper",
    ("Lizard", "Spock"): "Lizard poisons Spock",
    ("Spock", "Rock"): "Spock vaporizes Rock",
    ("Spock", "Scissors"): "Spock smashes Scissors",
}

user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)

    result_text = f"You: {emojis[user_choice]} {user_choice}\nComp: {emojis[comp_choice]} {comp_choice}\n\n"

    if user_choice == comp_choice:
        result_text += "It's a TIE! 😐"
        color = "#ffcc00"
    elif comp_choice in rules[user_choice]:
        # User wins
        reason = reasons.get((user_choice, comp_choice), f"{user_choice} beats {comp_choice}")
        result_text += f"You WIN! 🎉\n{reason}"
        color = "#00ff88"
        user_score += 1
    else:
        reason = reasons.get((comp_choice, user_choice), f"{comp_choice} beats {user_choice}")
        result_text += f"You LOSE! 😂\n{reason}"
        color = "#ff4444"
        comp_score += 1

    result_label.config(text=result_text, fg=color)
    score_label.config(text=f"You: {user_score} | Comp: {comp_score}")
    # Animation effect
    comp_pick_label.config(text=f"Computer picked {emojis[comp_choice]}")

# GUI SETUP
root = tk.Tk()
root.title("CaptinBadass RPSLS Game")
root.geometry("450x600")
root.configure(bg="#111")

tk.Label(root, text="ROCK PAPER SCISSORS", font=("Impact", 18), bg="#111", fg="white").pack(pady=(15,0))
tk.Label(root, text="LIZARD SPOCK EDITION", font=("Consolas", 12, "bold"), bg="#111", fg="#00ff88").pack()

score_label = tk.Label(root, text="You: 0 | Comp: 0", font=("Arial", 14, "bold"), bg="#111", fg="white")
score_label.pack(pady=15)

# Buttons frame
btn_frame = tk.Frame(root, bg="#111")
btn_frame.pack(pady=10)

# Create buttons in 2 rows
row1 = tk.Frame(btn_frame, bg="#111")
row1.pack()
row2 = tk.Frame(btn_frame, bg="#111")
row2.pack(pady=10)

def make_btn(choice, parent):
    return tk.Button(parent, text=f"{emojis[choice]}\n{choice}",
                     font=("Arial", 11, "bold"), width=8, height=2,
                     bg="#222", fg="white", activebackground="#00ff88",
                     command=lambda: play(choice))

make_btn("Rock", row1).pack(side="left", padx=5)
make_btn("Paper", row1).pack(side="left", padx=5)
make_btn("Scissors", row1).pack(side="left", padx=5)

make_btn("Lizard", row2).pack(side="left", padx=5)
make_btn("Spock", row2).pack(side="left", padx=5)

comp_pick_label = tk.Label(root, text="Computer is waiting...", font=("Consolas", 10), bg="#111", fg="#888")
comp_pick_label.pack(pady=5)

result_label = tk.Label(root, text="Pick your weapon, Captin! 👇",
                        font=("Arial", 13, "bold"), bg="#222", fg="white",
                        wraplength=380, justify="center", padx=20, pady=20,
                        width=35, height=6)
result_label.pack(pady=20)

tk.Label(root, text="Tip: Save battery, close after play 😂", font=("Consolas", 8), bg="#111", fg="#555").pack(side="bottom", pady=10)

root.mainloop()

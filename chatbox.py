import tkinter as tk
import random

# --- UPGRADED BRAIN WITH ROAST ---
brain = {
    "hello": ["Yo Captin! 🔥", "Hey bro! Wetin dey?", "Hello boss!"],
    "how are you": ["I dey, I dey debug life", "I strong! You?"],
    "your name": ["Na CaptinBadass chatbox!", "Call me Mini-Badass"],
    "you get babe": ["I no get oh i be Jesus Baby oh, single for life 😂", "Noo!, U wan date me? "],
    "how old are you": ["I be 2 years, but my savage na 100 years!"],
    "where is your": ["I dey live for you phone","i no get house oh pls adopt me"],
    "what's you fav colour": [" I no get favourite colour oh", " my favorite colour na money"],
    "bye": ["Oya later!", "Sharp, we go talk again!,Oya dey go i know say ur data wan finish"]
}

roasts = [
    "You wey be say your brain dey on airplane mode 😂",
    "Oga shut up, even your shadow dey leave you",
    "Mumu, go charge your brain, e dey low battery",
    "You talk like person wey dey use free data reason",
    "Lol, your comeback slow pass NEPA light for Abuja",
    "Go sit down, your opinion na expired gala",
    "You get data but you no get sense, nawa!",
    "stup up joor, you wey dey use person hotstop! lol"
]

def get_reply(user_msg):
    low = user_msg.lower()

    # Savage trigger
    if any(word in low for word in ["dumb", "mumu", "stupid", "fool", "idiot", "useless", "crazy","you be moor"]):
        return random.choice(roasts)

    for key in brain:
        if key in low:
            return random.choice(brain[key])

    return "I never know that one. Teach me like this:\nteach: your question | your answer"
        # TEACHING MODE: type -> teach: question | answer
    if low.startswith("teach:"):
        try:
            _, rest = user_msg.split(":", 1)
            q, a = rest.split("|", 1)
            q = q.strip().lower()
            a = a.strip()
            if q not in brain:
                brain[q] = []
            brain[q].append(a)
            save_brain()
            return f"Sharp! I don learn '{q}' = '{a}' forever! 🧠"
        except:
            return "Use like this: teach: how old are you | I be 10 years"

    # Savage trigger
    if any(word in low for word in ["dumb", "mumu", "stupid", "fool", "idiot", "useless"]):
        return random.choice(roasts)

    for key in brain:
        if key in low:
            # if value is list, pick random
            val = brain[key]
            if isinstance(val, list):
                return random.choice(val)
            return val

    return "I never know that one. Teach me like this:\nteach: your question | your answer"

def send():
    user_text = entry.get()
    if not user_text.strip():
        return
    chat_box.config(state="normal")
    chat_box.insert(tk.END, f"You: {user_text}\n", "you")
    reply = get_reply(user_text)
    chat_box.insert(tk.END, f"Bot: {reply}\n\n", "bot")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("CaptinBadass MEMORY Bot")
root.geometry("400x550")
root.configure(bg="#111")

chat_box = tk.Text(root, bg="#222", fg="white", font=("Consolas", 10), wrap="word", state="disabled")
chat_box.tag_config("you", foreground="#00ff88")
chat_box.tag_config("bot", foreground="#88ccff")
chat_box.pack(padx=10, pady=10, fill="both", expand=True)

bottom = tk.Frame(root, bg="#111")
bottom.pack(fill="x", padx=10, pady=10)

entry = tk.Entry(bottom, font=("Consolas", 11), bg="#333", fg="white", insertbackground="white")
entry.pack(side="left", fill="x", expand=True, padx=(0,10))
entry.bind("<Return>", lambda e: send())

btn = tk.Button(bottom, text="Send", command=send, bg="#00ff88", fg="black", font=("Arial", 10, "bold"), padx=15)
btn.pack(side="right")

chat_box.config(state="normal")
chat_box.insert(tk.END, "--- MEMORY MODE ON 🧠 ---\nI no dey forget again!\nTeach me: teach: question | answer\n\n", "bot")
chat_box.config(state="disabled")

root.mainloop()

def send():
    user_text = entry.get()
    if not user_text.strip():
        return

    chat_box.config(state="normal")
    chat_box.insert(tk.END, f"You: {user_text}\n", "you")
    reply = get_reply(user_text)
    chat_box.insert(tk.END, f"Bot: {reply}\n\n", "bot")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)
    entry.delete(0, tk.END)

# Window setup
root = tk.Tk()
root.title("CaptinBadass SAVAGE Chatbox")
root.geometry("400x500")
root.configure(bg="#111")

chat_box = tk.Text(root, bg="#222", fg="white", font=("Consolas", 11), wrap="word", state="disabled")
chat_box.tag_config("you", foreground="#00ff88")
chat_box.tag_config("bot", foreground="#ff5555") # Red for savage
chat_box.pack(padx=10, pady=10, fill="both", expand=True)

bottom = tk.Frame(root, bg="#111")
bottom.pack(fill="x", padx=10, pady=10)

entry = tk.Entry(bottom, font=("Consolas", 12), bg="#333", fg="white", insertbackground="white")
entry.pack(side="left", fill="x", expand=True, padx=(0,10))
entry.bind("<Return>", lambda e: send())

btn = tk.Button(bottom, text="Send", command=send, bg="#ff5555", fg="black", font=("Arial", 10, "bold"), padx=15)
btn.pack(side="right")

chat_box.config(state="normal")
chat_box.insert(tk.END, "--- SAVAGE MODE ON 😈 ---\nType 'Let's chat i'm ready!\n\n", "bot")
chat_box.config(state="disabled")

root.mainloop()
import tkinter as tk
import random
import json
import os

# File to remember everything
BRAIN_FILE = "brain.json"

# Default brain if no file
default_brain = {
    "hello": ["Yo Captin! 🔥", "Hey bro! Wetin dey?", "Hello boss!, Hafa bad guy "],
    "how are you": ["I dey, I dey debug life", "I strong! You?, i dey alright, how ur side"],
    "what's your name": ["Na CaptinBadass chatbox!", "Call me Mini-Badass"],
    "you get babe": ["I no get oh i be Jesus Baby oh, single for life 😂"],
    "how old are you": ["I be 2 years, but my savage na 100 years!"],
    "bye": ["Oya later!", "Sharp, we go talk again!"]
}

# Load brain if e exist
if os.path.exists(BRAIN_FILE):
    with open(BRAIN_FILE, "r") as f:
        brain = json.load(f)
else:
    brain = default_brain

roasts = [
    "You wey be say your brain dey on airplane mode 😂",
    "Oga shut up, even your shadow dey leave you",
    "Mumu, go charge your brain, e don low battery",
    "You talk like person wey dey use free data reason",
    "Lol, your comeback slow pass NEPA light for Abuja",
]

def save_brain():
    with open(BRAIN_FILE, "w") as f:
        json.dump(brain, f)

def get_reply(user_msg):
    low = user_msg.lower()

    

import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
GRID = 20
SPEED = 120 # lower = faster, save battery use 150 if low

class SnakeGame:
    def __init__(self, root):
        self.root = root
        root.title("CaptinBadass Snake")
        root.geometry(f"{WIDTH}x{450}")
        root.configure(bg="#111")
        root.resizable(False, False)

        self.score = 0
        self.direction = "Right"
        self.next_dir = "Right"
        self.game_over = False

        # Score
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14, "bold"), bg="#111", fg="#00ff88")
        self.score_label.pack(pady=10)

        # Canvas
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#222", highlightthickness=0)
        self.canvas.pack()

        # Snake start
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.new_food()

        # Controls
        root.bind("<KeyPress>", self.change_dir)

        # Buttons for phone/laptop touch
        ctrl = tk.Frame(root, bg="#111")
        ctrl.pack(pady=10)

        tk.Button(ctrl, text="⬆️", width=4, bg="#333", fg="white", command=lambda: self.set_dir("Up")).grid(row=0, column=1, padx=5)
        tk.Button(ctrl, text="⬅️", width=4, bg="#333", fg="white", command=lambda: self.set_dir("Left")).grid(row=1, column=0, padx=5)
        tk.Button(ctrl, text="⬇️", width=4, bg="#333", fg="white", command=lambda: self.set_dir("Down")).grid(row=1, column=1, padx=5)
        tk.Button(ctrl, text="➡️", width=4, bg="#333", fg="white", command=lambda: self.set_dir("Right")).grid(row=1, column=2, padx=5)

        self.draw()
        self.move()

    def new_food(self):
        while True:
            x = random.randint(0, (WIDTH//GRID)-1) * GRID
            y = random.randint(0, (HEIGHT//GRID)-1) * GRID
            if (x, y) not in self.snake:
                return (x, y)

    def set_dir(self, d):
        # prevent going back on itself
        opposite = {"Up":"Down", "Down":"Up", "Left":"Right", "Right":"Left"}
        if opposite[d]!= self.direction:
            self.next_dir = d

    def change_dir(self, e):
        key = e.keysym
        mapping = {"Up":"Up", "Down":"Down", "Left":"Left", "Right":"Right", "w":"Up", "s":"Down", "a":"Left", "d":"Right"}
        if key in mapping:
            self.set_dir(mapping[key])

    def draw(self):
        self.canvas.delete("all")
        # Food
        fx, fy = self.food
        self.canvas.create_oval(fx+2, fy+2, fx+GRID-2, fy+GRID-2, fill="#ff4444", outline="")

        # Snake
        for i, (x, y) in enumerate(self.snake):
            color = "#00ff88" if i==0 else "#00cc66" # head brighter
            self.canvas.create_rectangle(x, y, x+GRID-2, y+GRID-2, fill=color, outline="")

        if self.game_over:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text=f"GAME OVER!\nScore: {self.score}\nPress R to Restart",
                                    font=("Arial", 16, "bold"), fill="white", justify="center")

    def move(self):
        if self.game_over:
            return

        self.direction = self.next_dir
        head_x, head_y = self.snake[0]

        if self.direction == "Up": head_y -= GRID
        if self.direction == "Down": head_y += GRID
        if self.direction == "Left": head_x -= GRID
        if self.direction == "Right": head_x += GRID

        new_head = (head_x, head_y)

        # Wall collision
        if not (0 <= head_x < WIDTH and 0 <= head_y < HEIGHT):
            self.end_game()
            return
        # Self collision
        if new_head in self.snake:
            self.end_game()
            return

        self.snake.insert(0, new_head)

        # Eat food?
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.new_food()
        else:
            self.snake.pop()

        self.draw()
        self.root.after(SPEED, self.move)

    def end_game(self):
        self.game_over = True
        self.draw()
        self.root.bind("<KeyPress-r>", lambda e: self.restart())
        self.root.bind("<KeyPress-R>", lambda e: self.restart())

    def restart(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.new_food()
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.direction = "Right"
        self.next_dir = "Right"
        self.game_over = False
        self.draw()
        self.move()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

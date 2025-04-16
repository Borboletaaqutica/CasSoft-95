import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snakerio Deluxe")
        self.window.resizable(False, False)
        self.window.configure(bg="#1a1a1a")

        # Configurações do jogo
        self.cell_size = 20
        self.width = 30
        self.height = 30
        self.game_speed = 100

        # Cores
        self.bg_color = "#1a1a1a"
        self.snake_color = "#32CD32"  # Verde limão vibrante
        self.food_color = "#FF4500"  # Laranja forte
        self.text_color = "#F0F0F0"

        # Canvas com borda moderna
        self.canvas = tk.Canvas(
            self.window,
            width=self.width * self.cell_size,
            height=self.height * self.cell_size,
            bg=self.bg_color,
            highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=10)

        # Inicialização do jogo
        self.snake = [(15, 15)]
        self.food = self.spawn_food()
        self.direction = "Right"
        self.running = True
        self.score = 0

        # Controles
        self.window.bind("<Up>", lambda event: self.change_direction("Up"))
        self.window.bind("<Down>", lambda event: self.change_direction("Down"))
        self.window.bind("<Left>", lambda event: self.change_direction("Left"))
        self.window.bind("<Right>", lambda event: self.change_direction("Right"))
        self.window.bind("r", lambda event: self.restart_game())

        self.update()

    def spawn_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def change_direction(self, new_direction):
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposites.get(self.direction, ""):
            self.direction = new_direction

    def restart_game(self):
        self.running = False
        self.window.after_cancel(self.update_id)
        self.snake = [(15, 15)]
        self.food = self.spawn_food()
        self.direction = "Right"
        self.running = True
        self.score = 0
        self.game_speed = 100
        self.update()

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1
        elif self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1

        new_head = (head_x, head_y)

        if (
            new_head in self.snake
            or head_x < 0 or head_x >= self.width
            or head_y < 0 or head_y >= self.height
        ):
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 1
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")

        for x, y in self.snake:
            self.canvas.create_rectangle(
                x * self.cell_size + 2,
                y * self.cell_size + 2,
                (x + 1) * self.cell_size - 2,
                (y + 1) * self.cell_size - 2,
                fill=self.snake_color,
                outline="#222"
            )

        food_x, food_y = self.food
        self.canvas.create_oval(
            food_x * self.cell_size + 4,
            food_y * self.cell_size + 4,
            (food_x + 1) * self.cell_size - 4,
            (food_y + 1) * self.cell_size - 4,
            fill=self.food_color,
            outline="#000"
        )

        self.canvas.create_text(
            10,
            10,
            anchor="nw",
            text=f"Pontos: {self.score}",
            fill=self.text_color,
            font=("Consolas", 14, "bold")
        )

        self.canvas.create_text(
            10,
            35,
            anchor="nw",
            text="Pressione R para reiniciar",
            fill=self.text_color,
            font=("Consolas", 10)
        )

    def update(self):
        if self.running:
            self.move_snake()
            self.draw()
            self.update_id = self.window.after(self.game_speed, self.update)
        else:
            self.canvas.create_text(
                self.width * self.cell_size // 2,
                self.height * self.cell_size // 2,
                text="Game Over",
                fill="red",
                font=("Consolas", 24, "bold")
            )

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()

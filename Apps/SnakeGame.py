import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)

        # Configurações do jogo
        self.cell_size = 20
        self.width = 30  # Aumentado para 30 células
        self.height = 30  # Aumentado para 30 células
        self.game_speed = 100  # Velocidade do jogo (ms)

        # Cores
        self.bg_color = "#000000"
        self.snake_color = "#00FF00"
        self.food_color = "#FF0000"
        self.text_color = "#FFFFFF"

        # Inicialização do canvas
        self.canvas = tk.Canvas(self.window, width=self.width * self.cell_size, height=self.height * self.cell_size, bg=self.bg_color)
        self.canvas.pack()

        # Inicialização do jogo
        self.snake = [(15, 15)]  # Posição inicial da cobra
        self.food = self.spawn_food()
        self.direction = "Right"
        self.running = True
        self.score = 0  # Contador de pontos

        # Controles
        self.window.bind("<Up>", lambda event: self.change_direction("Up"))
        self.window.bind("<Down>", lambda event: self.change_direction("Down"))
        self.window.bind("<Left>", lambda event: self.change_direction("Left"))
        self.window.bind("<Right>", lambda event: self.change_direction("Right"))
        self.window.bind("r", lambda event: self.restart_game())  # Reinicia o jogo ao pressionar "R"

        self.update()

    def spawn_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def change_direction(self, new_direction):
        # Evita que a cobra se mova na direção oposta imediatamente
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposites.get(self.direction, ""):
            self.direction = new_direction

    def restart_game(self):
        self.running = False  # Para a execução atual do jogo
        self.window.after_cancel(self.update_id)  # Cancela o evento pendente do método update
        self.snake = [(15, 15)]  # Reinicia a posição inicial da cobra
        self.food = self.spawn_food()
        self.direction = "Right"
        self.running = True
        self.score = 0
        self.game_speed = 100  # Reinicia a velocidade do jogo para o valor inicial
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

        # Verifica colisões
        if (
            new_head in self.snake  # Colisão com o corpo
            or head_x < 0 or head_x >= self.width  # Colisão com as paredes (horizontal)
            or head_y < 0 or head_y >= self.height  # Colisão com as paredes (vertical)
        ):
            self.running = False
            return

        # Adiciona a nova posição da cabeça
        self.snake.insert(0, new_head)

        # Verifica se comeu a comida
        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 1  # Incrementa o contador de pontos
        else:
            self.snake.pop()  # Remove a cauda se não comeu

    def draw(self):
        self.canvas.delete("all")

        # Desenha a cobra
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x * self.cell_size,
                y * self.cell_size,
                (x + 1) * self.cell_size,
                (y + 1) * self.cell_size,
                fill=self.snake_color
            )

        # Desenha a comida
        food_x, food_y = self.food
        self.canvas.create_oval(
            food_x * self.cell_size,
            food_y * self.cell_size,
            (food_x + 1) * self.cell_size,
            (food_y + 1) * self.cell_size,
            fill=self.food_color
        )

        # Exibe o contador de pontos
        self.canvas.create_text(
            10,
            10,
            anchor="nw",
            text=f"Pontos: {self.score}",
            fill=self.text_color,
            font=("Arial", 14)
        )

        # Exibe a legenda
        self.canvas.create_text(
            10,
            30,
            anchor="nw",
            text="R pra reiniciar o jogo",
            fill=self.text_color,
            font=("Arial", 10)
        )

    def update(self):
        if self.running:
            self.move_snake()
            self.draw()
            self.update_id = self.window.after(self.game_speed, self.update)  # Armazena o ID do evento
        else:
            self.canvas.create_text(
                self.width * self.cell_size // 2,
                self.height * self.cell_size // 2,
                text="Game Over",
                fill="white",
                font=("Arial", 24)
            )

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
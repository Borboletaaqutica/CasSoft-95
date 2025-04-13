import tkinter as tk
import math

# Configuração da janela principal
root = tk.Tk()
root.title("Simulador do Sistema Solar - Estilo Windows 95")
root.geometry("800x600")
root.configure(bg="lightgray")

# Canvas para desenhar os planetas
canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
canvas.pack()

# Dados dos planetas (nome, cor, raio da órbita, tamanho, velocidade angular)
planets = [
    {"name": "Mercúrio", "color": "gray", "orbit_radius": 50, "size": 5, "speed": 0.02},
    {"name": "Vênus", "color": "yellow", "orbit_radius": 100, "size": 8, "speed": 0.015},
    {"name": "Terra", "color": "blue", "orbit_radius": 150, "size": 10, "speed": 0.01},
    {"name": "Marte", "color": "red", "orbit_radius": 200, "size": 7, "speed": 0.008},
]

# Posição inicial dos planetas
for planet in planets:
    planet["angle"] = 0

# Função para atualizar a posição dos planetas
def update_positions():
    canvas.delete("all")
    # Desenhar o Sol
    canvas.create_oval(390, 290, 410, 310, fill="yellow", outline="yellow")

    for planet in planets:
        # Desenhar a órbita do planeta
        canvas.create_oval(
            400 - planet["orbit_radius"], 300 - planet["orbit_radius"],
            400 + planet["orbit_radius"], 300 + planet["orbit_radius"],
            outline="white", dash=(2, 2)
        )

        # Calcular a posição do planeta
        x = 400 + planet["orbit_radius"] * math.cos(planet["angle"])
        y = 300 + planet["orbit_radius"] * math.sin(planet["angle"])
        planet["angle"] += planet["speed"]

        # Desenhar o planeta
        canvas.create_oval(
            x - planet["size"], y - planet["size"],
            x + planet["size"], y + planet["size"],
            fill=planet["color"], outline=planet["color"]
        )

    # Atualizar a cada 50ms
    root.after(50, update_positions)

# Função para aumentar a velocidade dos planetas
def increase_speed(event=None):  # Adicionado 'event' para compatibilidade com bind
    for planet in planets:
        planet["speed"] *= 1.2  # Aumenta a velocidade em 20%

# Função para diminuir a velocidade dos planetas
def decrease_speed(event=None):  # Adicionado 'event' para compatibilidade com bind
    for planet in planets:
        planet["speed"] *= 0.8  # Diminui a velocidade em 20%

# Adicionar botões para controle de velocidade
control_frame = tk.Frame(root, bg="lightgray")
control_frame.pack(pady=10)

increase_button = tk.Button(control_frame, text="Aumentar Velocidade", command=increase_speed)
increase_button.pack(side="left", padx=5)

decrease_button = tk.Button(control_frame, text="Diminuir Velocidade", command=decrease_speed)
decrease_button.pack(side="left", padx=5)

# Vincular as teclas de seta para controle de velocidade
root.bind("<Up>", increase_speed)  # Seta para cima aumenta a velocidade
root.bind("<Down>", decrease_speed)  # Seta para baixo diminui a velocidade

# Iniciar a simulação
update_positions()

# Executar a interface gráfica
root.mainloop()
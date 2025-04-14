import tkinter as tk
import math

# janela principal
root = tk.Tk()
root.title("Simulador do Sistema Solar - Estilo Windows 95")
root.geometry("800x600")
root.configure(bg="lightgray")

# desenhar os planetas
canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
canvas.pack()

# Dados dos planetas
planets = [
    {"name": "Mercúrio", "color": "gray", "orbit_radius": 50, "size": 5, "speed": 0.02},
    {"name": "Vênus", "color": "yellow", "orbit_radius": 100, "size": 8, "speed": 0.015},
    {"name": "Terra", "color": "blue", "orbit_radius": 150, "size": 10, "speed": 0.01},
    {"name": "Marte", "color": "red", "orbit_radius": 200, "size": 7, "speed": 0.008},
]


for planet in planets:
    planet["angle"] = 0


selected_planet = None

#
def on_orbit_click(event):
    global selected_planet
    for planet in planets:
        
        distance_to_orbit = abs(
            math.sqrt((event.x - 400) ** 2 + (event.y - 300) ** 2) - planet["orbit_radius"]
        )
        if distance_to_orbit <= 5:  
            selected_planet = planet
            break

#  velocidade dos planetas na distância da órbita
def recalculate_speeds():
    for planet in planets:
        # A velocidade eh inversa a orbita
        planet["speed"] = 0.5 / planet["orbit_radius"]

#  arrastar a órbita
def on_orbit_drag(event):
    global selected_planet
    if selected_planet:
        # Calcular o novo raio da órbita com base na posição do mouse
        new_radius = math.sqrt((event.x - 400) ** 2 + (event.y - 300) ** 2)
        selected_planet["orbit_radius"] = max(20, min(new_radius, 300))  # Limitar o raio entre 20 e 300
        recalculate_speeds()  # Recalcular as velocidades

# soltar o mouse
def on_orbit_release(event):
    global selected_planet
    selected_planet = None

# eventos de mouse
canvas.bind("<Button-1>", on_orbit_click)  # Clique esquerdo
canvas.bind("<B1-Motion>", on_orbit_drag)  # Arrastar com o botão esquerdo pressionado
canvas.bind("<ButtonRelease-1>", on_orbit_release)  # Soltar o botão esquerdo

# atualizar a posição dos planetas
def update_positions():
    canvas.delete("all")
    # o Sol
    canvas.create_oval(390, 290, 410, 310, fill="yellow", outline="yellow")

    for planet in planets:
        #  órbita do planeta
        canvas.create_oval(
            400 - planet["orbit_radius"], 300 - planet["orbit_radius"],
            400 + planet["orbit_radius"], 300 + planet["orbit_radius"],
            outline="white", dash=(2, 2)
        )

        # posição do planeta
        x = 400 + planet["orbit_radius"] * math.cos(planet["angle"])
        y = 300 + planet["orbit_radius"] * math.sin(planet["angle"])
        planet["angle"] += planet["speed"]

        # Desenhar o planeta
        canvas.create_oval(
            x - planet["size"], y - planet["size"],
            x + planet["size"], y + planet["size"],
            fill=planet["color"], outline=planet["color"]
        )

    root.after(50, update_positions)

# aumentar a velocidade dos planetas
def increase_speed(event=None):  
    for planet in planets:
        planet["speed"] *= 1.2  

# diminuir a velocidade
def decrease_speed(event=None):  
    for planet in planets:
        planet["speed"] *= 0.8  

# controle de velocidade
control_frame = tk.Frame(root, bg="lightgray")
control_frame.pack(pady=10)

increase_button = tk.Button(control_frame, text="Aumentar Velocidade", command=increase_speed)
increase_button.pack(side="left", padx=5)

decrease_button = tk.Button(control_frame, text="Diminuir Velocidade", command=decrease_speed)
decrease_button.pack(side="left", padx=5)

# controlar  velocidade
root.bind("<Up>", increase_speed)  # aumenta a velocidade
root.bind("<Down>", decrease_speed)  #  diminui a velocidade

# Velocidades ao iniciar o programa
recalculate_speeds()

# Iniciar a simulação
update_positions()

# interface gráfica
root.mainloop()

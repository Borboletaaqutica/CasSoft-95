import os  # Import necessário para manipulação de caminhos
import tkinter as tk
import time
import subprocess

# Cores estilo Windows 95
BG_COLOR = "#C0C0C0"
BUTTON_COLOR = "#E0E0E0"
TEXT_COLOR = "#000000"

class CassSoft95(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CassSoft 95™")
        self.geometry("800x600")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="CassSoft 95™", font=("Fixedsys", 18), bg=BG_COLOR, fg=TEXT_COLOR)
        title.pack(pady=40)

        label = tk.Label(self, text="Bem vindo!", font=("Fixedsys", 10),
                         bg=BG_COLOR, fg=TEXT_COLOR)
        label.pack(pady=5)

        # Botão para abrir a calculadora
        calc_btn = tk.Button(self, text="Abrir Calculadora", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                             relief="raised", width=20, command=self.abrir_calculadora)
        calc_btn.pack(pady=10)

        # Botão para abrir o SnakeGame
        snake_btn = tk.Button(self, text="Abrir SnakeGame", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                              relief="raised", width=20, command=self.abrir_snakegame)
        snake_btn.pack(pady=10)

        # Botão para abrir o Simulador de Física
        simulador_btn = tk.Button(self, text="Solaris!", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                                  relief="raised", width=20, command=self.abrir_simulador)
        simulador_btn.pack(pady=10)

        # Botão para abrir o InforPC
        inforpc_btn = tk.Button(self, text="Abrir InforPC", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                                relief="raised", width=20, command=self.abrir_inforpc)
        inforpc_btn.pack(pady=10)

        sair_btn = tk.Button(self, text="Sair", bg=BUTTON_COLOR, fg=TEXT_COLOR, relief="raised", width=20, command=self.quit)
        sair_btn.pack(pady=30)

    def abrir_calculadora(self):
        # Caminho relativo para o arquivo da calculadora
        calculadora_path = os.path.join(os.path.dirname(__file__), "Apps", "Calculadora.py")
        subprocess.Popen(["python", calculadora_path])  # Abre a calculadora

    def abrir_snakegame(self):
        # Caminho relativo para o arquivo do SnakeGame
        snakegame_path = os.path.join(os.path.dirname(__file__), "Apps", "SnakeGame.py")
        subprocess.Popen(["python", snakegame_path])  # Abre o SnakeGame

    def abrir_simulador(self):
        # Caminho relativo para o arquivo do Simulador de Física
        simulador_path = os.path.join(os.path.dirname(__file__), "Apps", "Solaris.py")
        subprocess.Popen(["python", simulador_path])  # Abre o Solaris

    def abrir_inforpc(self):
        # Caminho relativo para o arquivo do InforPC
        inforpc_path = os.path.join(os.path.dirname(__file__), "Apps", "InforPC.py")
        subprocess.Popen(["python", inforpc_path])  # Abre o InforPC

def splash_screen():
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.geometry("300x150+500+300")
    splash.configure(bg=BG_COLOR)

    label = tk.Label(splash, text="Carregando CassSoft 95™...", font=("Fixedsys", 14), bg=BG_COLOR, fg=TEXT_COLOR)
    label.pack(expand=True)

    # Espera 2.5s
    def abrir_janela_principal():
        splash.destroy()
        main_window.deiconify()

    splash.after(2500, abrir_janela_principal)

if __name__ == "__main__":
    main_window = CassSoft95()
    main_window.withdraw()

    splash_screen()
    main_window.mainloop()

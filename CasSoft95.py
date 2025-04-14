import os
import tkinter as tk
import time
import subprocess
import sys 
from tkinter import PhotoImage

# Cores Windows 95
BG_COLOR = "#C0C0C0"
BUTTON_COLOR = "#808080"
TEXT_COLOR = "#000000"

def instalar_dependencias():
    """Instala as dependências listadas no arquivo requirements.txt."""
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(requirements_path):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        except subprocess.CalledProcessError:
            print("Erro ao instalar dependências. Verifique o arquivo requirements.txt.")

class CassSoft95(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CassSoft 95™")
        self.geometry("800x600")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        self.dark_mode = False
        self.create_widgets()

    def toggle_dark_mode(self):
        """Alterna entre modo claro e escuro."""
        if self.dark_mode:
            # Voltar para o modo claro
            self.configure(bg=BG_COLOR)
            self.update_colors(BG_COLOR, BUTTON_COLOR, TEXT_COLOR)
            self.dark_mode = False
        else:
            # Ativar modo escuro
            dark_bg = "#2E2E2E"
            dark_button = "#4E4E4E"
            dark_text = "#FFFFFF"
            self.configure(bg=dark_bg)
            self.update_colors(dark_bg, dark_button, dark_text)
            self.dark_mode = True

    def update_colors(self, bg_color, button_color, text_color):
        """Atualiza as cores de todos os widgets."""
        for widget in self.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=bg_color, fg=text_color)
            elif isinstance(widget, tk.Button):
                widget.configure(bg=button_color, fg=text_color)
            elif isinstance(widget, tk.Frame):
                widget.configure(bg=bg_color)

    def create_widgets(self):
        title = tk.Label(self, text="CassSoft 95™", font=("Fixedsys", 18), bg=BG_COLOR, fg=TEXT_COLOR)
        title.pack(pady=20)

        label = tk.Label(self, text="Bem vindo!", font=("Fixedsys", 10),
                         bg=BG_COLOR, fg=TEXT_COLOR)
        label.pack(pady=5)

        # Frame para organizar os botões
        button_frame = tk.Frame(self, bg=BG_COLOR)
        button_frame.pack(pady=20)

        # Botões organizados em uma grade
        calc_btn = tk.Button(button_frame, text="Calculadora", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                             relief="raised", width=20, height=3, font=("Fixedsys", 10), command=self.abrir_calculadora)
        calc_btn.grid(row=0, column=0, padx=10, pady=10)

        snake_btn = tk.Button(button_frame, text="Jogo da Cobrinha :3", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                              relief="raised", width=20, height=3, font=("Fixedsys", 10), command=self.abrir_snakegame)
        snake_btn.grid(row=0, column=1, padx=10, pady=10)

        simulador_btn = tk.Button(button_frame, text="Solaris!", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                                  relief="raised", width=20, height=3, font=("Fixedsys", 10), command=self.abrir_simulador)
        simulador_btn.grid(row=0, column=2, padx=10, pady=10)

        inforpc_btn = tk.Button(button_frame, text="InforPC", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                                relief="raised", width=20, height=3, font=("Fixedsys", 10), command=self.abrir_inforpc)
        inforpc_btn.grid(row=1, column=0, padx=10, pady=10)

        chat_btn = tk.Button(button_frame, text="Chat ao Vivo (Beta)", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                             relief="raised", width=20, height=3, font=("Fixedsys", 10), command=self.abrir_chat)
        chat_btn.grid(row=1, column=1, padx=10, pady=10)

        sair_btn = tk.Button(button_frame, text="Sair", bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                             relief="raised", width=20, height=3, font=("Fixedsys", 10), command=self.quit)
        sair_btn.grid(row=1, column=2, padx=10, pady=10)

        # Aviso abaixo do botão do Chat
        chat_warning = tk.Label(self, text="EM FASE TESTES, NAO ESPERAR MUITO", font=("Fixedsys", 8),
                                bg=BG_COLOR, fg=TEXT_COLOR)
        chat_warning.pack(pady=5)

        # Botão para alternar modo escuro
        dark_mode_btn = tk.Button(self, text="🌙", bg=BUTTON_COLOR, fg=TEXT_COLOR,
                                  relief="flat", width=3, height=1, font=("Fixedsys", 8),
                                  command=self.toggle_dark_mode)
        dark_mode_btn.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)  # Posiciona no canto inferior direito

        # Exibir imagem no canto inferior direito
        image_path = os.path.join(os.path.dirname(__file__), "Assets", "Catnerd.png")
        if os.path.exists(image_path):
            self.image = PhotoImage(file=image_path)  # Carrega a imagem
            image_label = tk.Label(self, image=self.image, bg=BG_COLOR)
            image_label.place(relx=1.0, rely=1.0, anchor="se", x=-40, y=-40)  # Ajusta posição para não sobrepor o botão

    def abrir_calculadora(self):
        # Caminho relativo da calculadora
        calculadora_path = os.path.join(os.path.dirname(__file__), "Apps", "Calculadora.py")
        subprocess.Popen(["python", calculadora_path])  # Abre a calculadora

    def abrir_snakegame(self):
        # Caminho relativo do SnakeGame
        snakegame_path = os.path.join(os.path.dirname(__file__), "Apps", "SnakeGame.py")
        subprocess.Popen(["python", snakegame_path])  # Abre o SnakeGame

    def abrir_simulador(self):
        # Caminho relativo do Solaris
        simulador_path = os.path.join(os.path.dirname(__file__), "Apps", "Solaris.py")
        subprocess.Popen(["python", simulador_path])  # Abre o Solaris

    def abrir_inforpc(self):
        # Caminho relativo do InforPC
        inforpc_path = os.path.join(os.path.dirname(__file__), "Apps", "InforPC.py")
        subprocess.Popen(["python", inforpc_path])  # Abre o InforPC

    def abrir_chat(self):
        # Caminho relativo para o arquivo do Chat
        chat_path = os.path.join(os.path.dirname(__file__), "Apps", "Chat.py")
        subprocess.Popen(["python", chat_path])  # Abre o Chat

def splash_screen():
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.geometry("300x150+500+300")
    splash.configure(bg=BG_COLOR)

    label = tk.Label(splash, text="Carregando...", font=("Fixedsys", 14), bg=BG_COLOR, fg=TEXT_COLOR)
    label.pack(expand=True)

    # Espera 2.5s
    def abrir_janela_principal():
        splash.destroy()
        main_window.deiconify()

    splash.after(2500, abrir_janela_principal)

if __name__ == "__main__":
    instalar_dependencias()  # Instala as dependebciaus kkkkk < nao sabe escrever
    main_window = CassSoft95()
    main_window.withdraw()

    splash_screen()
    main_window.mainloop()

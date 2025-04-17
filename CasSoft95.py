import os
import tkinter as tk
import tkinter.ttk as ttk 
import time
import subprocess
import sys 
import threading
import requests
import json 
from tkinter import PhotoImage, font as tkFont, messagebox
from tkinter import scrolledtext
from datetime import datetime

# Cores retrô-modernas (apenas modo escuro)
BG_COLOR = "#2E2E2E"
BUTTON_COLOR = "#4E4E4E"
TEXT_COLOR = "#FFFFFF"
BUTTON_ACTIVE_COLOR = "#5A5A5A"
FRAME_BORDER_COLOR = "#7A7A7A"
TITLE_BAR_COLOR = "#1A1A1A"
TITLE_TEXT_COLOR = "#00FFFF"


def instalar_dependencias():
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(requirements_path):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        except subprocess.CalledProcessError:
            print("Erro ao instalar dependências. Verifique o arquivo requirements.txt.")



class CassSoft95(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)  # Remove a barra de título padrão
        self.geometry("800x600")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 800
        window_height = 600
        position_x = (screen_width - window_width) // 2
        position_y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.custom_font = ("Consolas", 10)
        self.title_font = ("Fixedsys", 20)
        self.pixel_font = self.load_pixel_font()

        # Definir os botões principais e de jogos
        self.btns = [
            ("Calculadora", self.abrir_calculadora),
            ("Infor-PC", self.abrir_inforpc)
        ]

        self.jogos_btns = [
            ("Snake!", self.abrir_snakegame),
            ("Solaris!", self.abrir_simulador)
        ]

        self.create_widgets()

    def load_pixel_font(self):
        try:
            font_path = os.path.join(os.path.dirname(__file__), "Assets", "PressStart2P-Regular.ttf")
            tkFont.Font(family="Press Start 2P", size=10)
            return ("Press Start 2P", 10)
        except:
            return self.custom_font

    def update_colors(self, bg_color, button_color, text_color):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=bg_color, fg=text_color)
            elif isinstance(widget, tk.Button):
                widget.configure(bg=button_color, fg=text_color)
            elif isinstance(widget, tk.Frame):
                widget.configure(bg=bg_color)

    def apply_hover_effects(self, button):
        button.bind("<Enter>", lambda e: button.configure(bg=BUTTON_ACTIVE_COLOR))
        button.bind("<Leave>", lambda e: button.configure(bg=BUTTON_COLOR))

    def styled_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                        activebackground=BUTTON_ACTIVE_COLOR, relief="raised",
                        bd=2, font=self.custom_font, width=20, height=2,
                        highlightbackground=FRAME_BORDER_COLOR,
                        highlightthickness=1,
                        command=command,
                        takefocus=False)
        self.apply_hover_effects(btn)
        return btn

    def create_widgets(self):
        # Configurar estilo escuro para o Notebook
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
        style.configure("TNotebook.Tab", background=BUTTON_COLOR, foreground=TEXT_COLOR, padding=[10, 5],
                        font=self.custom_font)
        style.map("TNotebook.Tab", background=[("selected", TITLE_BAR_COLOR)],
                  foreground=[("selected", TITLE_TEXT_COLOR)])

        # Barra de título personalizada
        title_bar = tk.Frame(self, bg=TITLE_BAR_COLOR, relief="raised", bd=0)
        title_bar.pack(fill=tk.X)

        title = tk.Label(title_bar, text="CassSoft 95™", font=self.title_font, bg=TITLE_BAR_COLOR, fg=TITLE_TEXT_COLOR, pady=10)
        title.pack(side=tk.LEFT, padx=10)

        # Botão de saída no canto superior direito
        close_button = tk.Button(title_bar, text="X", font=self.custom_font, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                                 activebackground=BUTTON_ACTIVE_COLOR, relief="flat", command=self.quit)
        close_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Permitir mover a janela ao arrastar a barra de título
        def start_move(event):
            self.x = event.x
            self.y = event.y

        def stop_move(event):
            self.x = None
            self.y = None

        def do_move(event):
            x = self.winfo_pointerx() - self.x
            y = self.winfo_pointery() - self.y
            self.geometry(f"+{x}+{y}")

        title_bar.bind("<Button-1>", start_move)
        title_bar.bind("<ButtonRelease-1>", stop_move)
        title_bar.bind("<B1-Motion>", do_move)

        # Notebook para abas
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Aba principal
        main_tab = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(main_tab, text="Aplicativos")

        # Aba de jogos
        jogos_tab = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(jogos_tab, text="Jogos")

        # Aba de chat
        chat_tab = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(chat_tab, text="Chat")

        self.create_chat_interface(chat_tab)

        # Botões na aba principal
        for text, cmd in self.btns:
            btn = self.styled_button(main_tab, text, cmd)
            btn.pack(fill=tk.X, pady=5)

        # Botões na aba de jogos
        for text, cmd in self.jogos_btns:
            btn = self.styled_button(jogos_tab, text, cmd)
            btn.pack(fill=tk.X, pady=5)

        # Imagem no canto inferior direito
        image_path = os.path.join(os.path.dirname(__file__), "Assets", "Catnerd.png")
        if os.path.exists(image_path):
            self.image = PhotoImage(file=image_path)
            self.image_label = tk.Label(self, image=self.image, bg=BG_COLOR)
            self.image_label.place(relx=1.0, rely=1.0, anchor="se", x=-40, y=-40)

        # Função para alternar a visibilidade do gato
        def on_tab_change(event):
            selected_tab = notebook.tab(notebook.select(), "text")
            if selected_tab == "Chat":
                self.image_label.place_forget()
            else:
                self.image_label.place(relx=1.0, rely=1.0, anchor="se", x=-40, y=-40)

        # Vincular o evento de troca de abas
        notebook.bind("<<NotebookTabChanged>>", on_tab_change)

    def create_chat_interface(self, parent):
        # Interface do chat
        frame_usuario = tk.Frame(parent, bg=BG_COLOR)  # Alterado para usar tk.Frame
        frame_usuario.pack(pady=10, padx=10, fill=tk.X)

        label_usuario = tk.Label(frame_usuario, text="Usuário:", bg=BG_COLOR, fg=TEXT_COLOR)
        label_usuario.pack(side=tk.LEFT, padx=5)

        self.entrada_usuario = tk.Entry(frame_usuario, font=self.custom_font)
        self.entrada_usuario.insert(0, "Cass")
        self.entrada_usuario.configure(bg=BUTTON_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
        self.entrada_usuario.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.chat_display = scrolledtext.ScrolledText(
            parent,
            state='disabled',
            font=self.custom_font,
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            highlightbackground=FRAME_BORDER_COLOR,
            highlightthickness=1
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        frame_texto = tk.Frame(parent, bg=BG_COLOR)  # Alterado para usar tk.Frame
        frame_texto.pack(pady=10, padx=10, fill=tk.X)

        self.entrada_texto = tk.Entry(frame_texto, font=self.custom_font)
        self.entrada_texto.configure(bg=BUTTON_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
        self.entrada_texto.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.entrada_texto.bind("<Return>", self.enviar_mensagem)

        botao_enviar = tk.Button(frame_texto, text="Enviar", command=self.enviar_mensagem, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        botao_enviar.pack(side=tk.RIGHT, padx=5)

        # Thread para atualizar mensagens
        threading.Thread(target=self.atualizar_mensagens, daemon=True).start()

    def enviar_mensagem(self, event=None):
        usuario = self.entrada_usuario.get().strip()
        if not usuario:
            messagebox.showerror("Erro", "O nome de usuário não pode estar vazio.")
            return
        texto = self.entrada_texto.get()
        if not texto.strip():
            return
        dados = {
            "usuario": usuario,
            "texto": texto,
            "timestamp": datetime.now().isoformat()
        }
        try:
            requests.post(FIREBASE_URL, json=dados)
        except requests.RequestException:
            messagebox.showerror("Erro", "Não foi possível enviar a mensagem.")
        self.entrada_texto.delete(0, tk.END)

    def atualizar_mensagens(self):
        while True:
            try:
                res = requests.get(FIREBASE_URL)
                mensagens = res.json()
                self.chat_display.configure(state='normal')

                # Salvar a posição atual do scroll
                scroll_position = self.chat_display.yview()

                # Atualizar o conteúdo do chat
                self.chat_display.delete(1.0, tk.END)
                if isinstance(mensagens, dict):  # Verifica se mensagens é um dicionário
                    for msg in mensagens.values():
                        if isinstance(msg, dict) and 'usuario' in msg and 'texto' in msg:
                            self.chat_display.insert(tk.END, f"[{msg['usuario']}] {msg['texto']}\n")

                # Verificar se o scroll está no final antes de rolar automaticamente
                if scroll_position[1] == 1.0:
                    self.chat_display.see(tk.END)

                self.chat_display.configure(state='disabled')
            except requests.RequestException:
                pass
            except Exception as e:
                print(f"Erro ao atualizar mensagens: {e}")
            time.sleep(2)

    def abrir_calculadora(self):
        calculadora_path = os.path.join(os.path.dirname(__file__), "Apps", "Calculadora.py")
        subprocess.Popen(["python", calculadora_path])

    def abrir_snakegame(self):
        snakegame_path = os.path.join(os.path.dirname(__file__), "Apps", "SnakeGame.py")
        subprocess.Popen(["python", snakegame_path])

    def abrir_simulador(self):
        simulador_path = os.path.join(os.path.dirname(__file__), "Apps", "Solaris.py")
        subprocess.Popen(["python", simulador_path])

    def abrir_inforpc(self):
        inforpc_path = os.path.join(os.path.dirname(__file__), "Apps", "InforPC.py")
        subprocess.Popen(["python", inforpc_path])

    def abrir_chat(self):
        chat_path = os.path.join(os.path.dirname(__file__), "Apps", "Chat.py")
        subprocess.Popen(["python", chat_path])


def splash_screen():
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.geometry("300x150+500+300")
    splash.configure(bg=BG_COLOR)

    label = tk.Label(splash, text="Carregando...", font=("Fixedsys", 14), bg=BG_COLOR, fg=TEXT_COLOR)
    label.pack(expand=True)

    def update_loading_text(i=0):
        textos = ["Iniciando CassSoft™...", "Carregando aplicações...", "Pronto pra rodar!"]
        if i < len(textos):
            label.config(text=textos[i])
            splash.after(800, lambda: update_loading_text(i + 1))

    update_loading_text()

    def abrir_janela_principal():
        splash.destroy()
        main_window.deiconify()

    splash.after(2500, abrir_janela_principal)


if __name__ == "__main__":
    # Carregar a URL do Firebase do arquivo config.json
    config_path = os.path.join(os.path.dirname(__file__), "Apps", "config.json")
    try:
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            FIREBASE_URL = config.get("FIREBASE_URL")
            if not FIREBASE_URL:
                raise ValueError("A URL do Firebase não foi encontrada no arquivo de configuração.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo de configuração: {e}")
        sys.exit(1)

    instalar_dependencias()
    main_window = CassSoft95()
    main_window.withdraw()
    splash_screen()
    main_window.mainloop()
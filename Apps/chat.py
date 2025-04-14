import os
import json
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
import requests
import threading
import time

# Carregar a URL do arquivo de configuração
with open(".config.json", "r") as config_file:
    config = json.load(config_file)

FIREBASE_URL = config.get("FIREBASE_URL")

if not FIREBASE_URL:
    raise ValueError("A URL do Firebase não foi encontrada no arquivo de configuração.")

# Lista para armazenar os nomes de usuários ativos
usuarios_ativos = set()

def verificar_usuario():
    usuario = entrada_usuario.get().strip()
    if not usuario:
        messagebox.showerror("Erro", "O nome de usuário não pode estar vazio.")
        return False
    if usuario in usuarios_ativos:
        messagebox.showerror("Erro", f"O nome de usuário '{usuario}' já está em uso.")
        return False
    usuarios_ativos.add(usuario)
    return True

def enviar_mensagem(event=None):
    usuario = entrada_usuario.get().strip()
    if not verificar_usuario():
        return
    texto = entrada_texto.get()
    if not texto.strip():
        return
    dados = {
        "usuario": usuario,
        "texto": texto,
        "timestamp": datetime.now().isoformat()
    }
    requests.post(FIREBASE_URL, json=dados)
    entrada_texto.delete(0, tk.END)

def atualizar_mensagens():
    while True:
        res = requests.get(FIREBASE_URL)
        mensagens = res.json()
        chat_display.configure(state='normal')
        chat_display.delete(1.0, tk.END)
        if mensagens:
            for msg in mensagens.values():
                chat_display.insert(tk.END, f"[{msg['usuario']}] {msg['texto']}\n")
        chat_display.configure(state='disabled')
        time.sleep(2)

def alternar_modo_escuro():
    if janela["bg"] == "white":
        # Ativar modo escuro
        janela.configure(bg="black")
        frame_usuario.configure(style="Dark.TFrame")
        frame_texto.configure(style="Dark.TFrame")
        chat_display.configure(bg="black", fg="white", insertbackground="white")
        entrada_usuario.configure(style="Dark.TEntry")
        entrada_texto.configure(style="Dark.TEntry")
        label_usuario.configure(style="Dark.TLabel")
        botao_enviar.configure(style="Dark.TButton")
    else:
        # Desativar modo escuro
        janela.configure(bg="white")
        frame_usuario.configure(style="TFrame")
        frame_texto.configure(style="TFrame")
        chat_display.configure(bg="white", fg="black", insertbackground="black")
        entrada_usuario.configure(style="TEntry")
        entrada_texto.configure(style="TEntry")
        label_usuario.configure(style="TLabel")
        botao_enviar.configure(style="TButton")

# Modificar o botão de entrada de usuário para verificar o nome
def configurar_usuario():
    if verificar_usuario():
        entrada_usuario.configure(state='disabled')
        botao_configurar_usuario.configure(state='disabled')

# Interface CassSoft95
janela = tk.Tk()
janela.title("CassChat - CassSoft95™")
janela.geometry("800x650")
janela.resizable(False, False)
janela.configure(bg="white")

# Estilo retrô e modo escuro
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('MS Sans Serif', 10), padding=5)
style.configure('TEntry', font=('MS Sans Serif', 10))
style.configure('TLabel', font=('MS Sans Serif', 10))
style.configure('Dark.TButton', font=('MS Sans Serif', 10), padding=5, background="black", foreground="white")
style.configure('Dark.TEntry', font=('MS Sans Serif', 10), fieldbackground="black", foreground="white")
style.configure('Dark.TLabel', font=('MS Sans Serif', 10), background="black", foreground="white")
style.configure('Dark.TFrame', background="black")

# Entrada de usuário
frame_usuario = ttk.Frame(janela)
frame_usuario.pack(pady=10, padx=10, fill=tk.X)

label_usuario = ttk.Label(frame_usuario, text="Usuário:")
label_usuario.pack(side=tk.LEFT, padx=5)

entrada_usuario = ttk.Entry(frame_usuario)
entrada_usuario.insert(0, "Cass")
entrada_usuario.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Adicionar botão para configurar o nome de usuário
botao_configurar_usuario = ttk.Button(frame_usuario, text="Configurar Usuário", command=configurar_usuario)
botao_configurar_usuario.pack(side=tk.RIGHT, padx=5)

# Área de chat
chat_display = scrolledtext.ScrolledText(janela, state='disabled', font=('MS Sans Serif', 10))
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entrada de texto
frame_texto = ttk.Frame(janela)
frame_texto.pack(pady=10, padx=10, fill=tk.X)

entrada_texto = ttk.Entry(frame_texto)
entrada_texto.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
entrada_texto.bind("<Return>", enviar_mensagem)

botao_enviar = ttk.Button(frame_texto, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(side=tk.RIGHT, padx=5)

# Botão para alternar modo escuro
botao_modo_escuro = ttk.Button(janela, text="Modo Escuro", command=alternar_modo_escuro)
botao_modo_escuro.pack(pady=10)

# Thread para atualizar o chat
threading.Thread(target=atualizar_mensagens, daemon=True).start()

janela.mainloop()

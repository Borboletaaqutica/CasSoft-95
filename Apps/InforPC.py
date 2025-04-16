import tkinter as tk
from tkinter import ttk
import platform
import psutil
import os
import socket
from datetime import datetime, timedelta
import getpass
import ctypes

# --- CORES E ESTILO ---
BG_COLOR = "#2C2C2C"
FG_COLOR = "#F0F0F0"
ACCENT_COLOR = "#4682B4"
TITLE_BG = "#1A1A1A"
TITLE_FG = "#00FFFF"
FONT = ("Consolas", 10)
FONT_BOLD = ("Consolas", 10, "bold")


def get_system_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    uptime_str = str(timedelta(seconds=uptime.total_seconds())).split(".")[0]

    return {
        "Sistema Operacional": platform.system() + " " + platform.release(),
        "Versão do Kernel": platform.version(),
        "Arquitetura": platform.machine(),
        "Hostname": socket.gethostname(),
        "Tempo de Atividade": uptime_str,
    }


def get_hardware_info():
    return {
        "Processador": platform.processor(),
        "Núcleos Físicos": psutil.cpu_count(logical=False),
        "Núcleos Lógicos": psutil.cpu_count(logical=True),
        "RAM Total": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "RAM em Uso": f"{psutil.virtual_memory().percent}%",
    }


def get_disk_info():
    disk = psutil.disk_usage('/')
    return {
        "Espaço Total": f"{round(disk.total / (1024 ** 3), 2)} GB",
        "Espaço Usado": f"{round(disk.used / (1024 ** 3), 2)} GB",
        "Espaço Livre": f"{round(disk.free / (1024 ** 3), 2)} GB",
        "Uso de Disco": f"{disk.percent}%",
        "Sistema de Arquivos": os.name
    }


def get_network_info():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Desconhecido"
    interfaces = psutil.net_if_addrs()
    active = ", ".join(interfaces.keys())
    return {
        "Endereço IP Local": ip,
        "Interfaces Ativas": active,
    }


def get_user_info():
    is_admin = "Indisponível"
    if os.name == "posix":
        is_admin = "Sim" if os.geteuid() == 0 else "Não"
    elif os.name == "nt":
        is_admin = "Sim" if ctypes.windll.shell32.IsUserAnAdmin() != 0 else "Não"

    return {
        "Usuário": getpass.getuser(),
        "Diretório Home": os.path.expanduser("~"),
        "Permissões de Root/Admin": is_admin,
    }

# --- INTERFACE MODERNIZADA COM RETRÔ ---

root = tk.Tk()
root.title("InforPC™")
root.geometry("700x500")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Título com estilo
title = tk.Label(
    root,
    text="Infor-PC™",
    font=("Fixedsys", 18, "bold"),
    bg=TITLE_BG,
    fg=TITLE_FG,
    pady=12
)
title.pack(fill=tk.X)

# Notebook com estilo moderno
style = ttk.Style()
style.theme_use("default")
style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
style.configure("TNotebook.Tab", background=ACCENT_COLOR, foreground="white", padding=8)
style.map("TNotebook.Tab", background=[("selected", "#1E90FF")])

notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

# Função para preencher abas

def preencher_aba(frame, dados):
    for key, value in dados.items():
        row = tk.Frame(frame, bg=BG_COLOR, pady=5)
        row.pack(anchor="w", fill=tk.X, padx=10)
        tk.Label(
            row,
            text=key + ":",
            font=FONT_BOLD,
            bg=BG_COLOR,
            fg=ACCENT_COLOR,
            width=24,
            anchor="w"
        ).pack(side="left")
        tk.Label(
            row,
            text=str(value),
            font=FONT,
            bg=BG_COLOR,
            fg=FG_COLOR,
            anchor="w"
        ).pack(side="left", fill=tk.X, expand=True)

# Criar abas com dados
abas = {
    "Sistema": get_system_info(),
    "Hardware": get_hardware_info(),
    "Disco": get_disk_info(),
    "Rede": get_network_info(),
    "Usuário": get_user_info()
}

for nome, dados in abas.items():
    frame = tk.Frame(notebook, bg=BG_COLOR)
    notebook.add(frame, text=nome)
    preencher_aba(frame, dados)

root.mainloop()

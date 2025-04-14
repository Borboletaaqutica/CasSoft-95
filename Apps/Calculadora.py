import tkinter as tk
from tkinter import ttk

class Calculator95:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora")
        self.window.geometry("320x400")
        self.window.resizable(False, False)
        
        # cores do Windows 95
        self.win95_gray = "#c0c0c0"
        self.win95_dark = "#808080"
        self.win95_light = "#ffffff"
        
        self.window.configure(bg=self.win95_gray)
        
        # Tamanho dos grids
        self.window.grid_columnconfigure((0,1,2,3), weight=1)
        self.window.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        
        # Display
        self.display = tk.Entry(self.window, 
                              font=("Arial", 24),
                              justify="right",
                              bd=3,
                              relief="sunken",
                              bg="white")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Botoes
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        
        button_style = {
            'font': ("Arial", 16),
            'width': 4,
            'height': 1,
            'relief': "raised",
            'bg': self.win95_gray,
            'activebackground': self.win95_dark,
            'bd': 3,
            'padx': 10,
            'pady': 10
        }
        
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            btn = tk.Button(self.window,
                          text=button,
                          command=cmd,
                          **button_style)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
                
        # BOTAO C PRA LIMPAR
        tk.Button(self.window,
                 text="C",
                 command=self.clear,
                 **button_style).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)

    def clear(self):
        self.display.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator95()
    calc.run()

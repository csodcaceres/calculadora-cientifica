#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess
import sys
import os

class SelectorTema:
    def __init__(self, root):
        self.root = root
        self.root.title("Selector de Tema - Calculadora")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#303446")  # Fondo oscuro
        
        self._crear_interfaz()
    
    def _crear_interfaz(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#303446", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="Calculadora Científica",
            font=("Arial", 18, "bold"),
            bg="#303446",
            fg="#C6D0F5"  # Texto claro
        )
        titulo.pack(pady=(0, 20))
        
        # Subtítulo
        subtitulo = tk.Label(
            main_frame,
            text="Selecciona un tema para la calculadora",
            font=("Arial", 12),
            bg="#303446",
            fg="#C6D0F5"  # Texto claro
        )
        subtitulo.pack(pady=(0, 30))
        
        # Botones de tema
        botones_frame = tk.Frame(main_frame, bg="#303446")
        botones_frame.pack(fill="x", pady=10)
        
        # Tema oscuro
        btn_tema_oscuro = tk.Button(
            botones_frame,
            text="Tema Oscuro",
            font=("Arial", 12, "bold"),
            bg="#1E1E2E",
            fg="#C6D0F5",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=1,
            command=self.abrir_tema_oscuro
        )
        btn_tema_oscuro.grid(row=0, column=0, padx=10, pady=10)
        
        # Tema claro
        btn_tema_claro = tk.Button(
            botones_frame,
            text="Tema Claro",
            font=("Arial", 12, "bold"),
            bg="#F0F0F0",
            fg="#333333",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=1,
            command=self.abrir_tema_claro
        )
        btn_tema_claro.grid(row=0, column=1, padx=10, pady=10)
        
        # Botón para abrir la versión de consola
        btn_consola = tk.Button(
            main_frame,
            text="Versión Consola",
            font=("Arial", 10),
            bg="#8CAAEE",
            fg="#303446",
            padx=10,
            pady=5,
            command=self.abrir_consola
        )
        btn_consola.pack(pady=(30, 0))
    
    def abrir_tema_oscuro(self):
        try:
            self.root.destroy()  # Cierra la ventana actual
            if sys.platform.startswith('win'):
                subprocess.Popen(['python', 'calculadora_gui_simple.py'])
            else:
                subprocess.Popen(['python3', 'calculadora_gui_simple.py'])
        except Exception as e:
            print(f"Error al abrir calculadora: {e}")
    
    def abrir_tema_claro(self):
        try:
            self.root.destroy()  # Cierra la ventana actual
            if sys.platform.startswith('win'):
                subprocess.Popen(['python', 'calculadora_tema_claro.py'])
            else:
                subprocess.Popen(['python3', 'calculadora_tema_claro.py'])
        except Exception as e:
            print(f"Error al abrir calculadora: {e}")
    
    def abrir_consola(self):
        try:
            self.root.destroy()  # Cierra la ventana actual
            if sys.platform.startswith('win'):
                os.system('start cmd /k python calculadora.py')
            else:
                os.system('gnome-terminal -- python3 calculadora.py')
        except Exception as e:
            print(f"Error al abrir calculadora: {e}")

def main():
    root = tk.Tk()
    app = SelectorTema(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
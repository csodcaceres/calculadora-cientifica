#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from calculadora import Calculadora

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.calculadora = Calculadora()
        
        # Variables para almacenar los valores de entrada
        self.valor1 = tk.StringVar()
        self.valor2 = tk.StringVar()
        self.resultado = tk.StringVar()
        self.resultado.set("0")
        
        self._crear_interfaz()
        
    def _crear_interfaz(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=20, pady=20, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True)
        
        # Título
        titulo = tk.Label(main_frame, text="Calculadora Python", font=("Arial", 16, "bold"), bg="#f0f0f0")
        titulo.grid(row=0, column=0, columnspan=4, pady=(0, 20))
        
        # Campo de resultado
        resultado_frame = tk.Frame(main_frame, bg="#f0f0f0")
        resultado_frame.grid(row=1, column=0, columnspan=4, sticky="ew", pady=(0, 20))
        
        resultado_display = tk.Entry(resultado_frame, 
                                    textvariable=self.resultado, 
                                    font=("Arial", 24),
                                    bd=1, 
                                    justify="right",
                                    state="readonly")
        resultado_display.pack(fill="x")
        
        # Campos de entrada
        entrada_frame = tk.Frame(main_frame, bg="#f0f0f0")
        entrada_frame.grid(row=2, column=0, columnspan=4, sticky="ew", pady=(0, 20))
        
        tk.Label(entrada_frame, text="Primer número:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=(0, 10))
        tk.Entry(entrada_frame, textvariable=self.valor1, width=15).grid(row=0, column=1, sticky="w", padx=(0, 20))
        
        tk.Label(entrada_frame, text="Segundo número:", bg="#f0f0f0").grid(row=0, column=2, sticky="w", padx=(0, 10))
        tk.Entry(entrada_frame, textvariable=self.valor2, width=15).grid(row=0, column=3, sticky="w")
        
        # Botones de operaciones
        botones_frame = tk.Frame(main_frame, bg="#f0f0f0")
        botones_frame.grid(row=3, column=0, columnspan=4, pady=(0, 10))
        
        # Estilos para botones
        button_style = {
            "font": ("Arial", 12),
            "width": 10,
            "height": 2,
            "bd": 1,
            "relief": "raised"
        }
        
        # Botones de operaciones
        tk.Button(botones_frame, text="Sumar", bg="#4CAF50", fg="white", command=self.sumar, **button_style).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(botones_frame, text="Restar", bg="#2196F3", fg="white", command=self.restar, **button_style).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(botones_frame, text="Multiplicar", bg="#FF9800", fg="white", command=self.multiplicar, **button_style).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(botones_frame, text="Dividir", bg="#F44336", fg="white", command=self.dividir, **button_style).grid(row=0, column=3, padx=5, pady=5)
        
        # Botón limpiar
        tk.Button(
            main_frame, 
            text="Limpiar", 
            bg="#9E9E9E", 
            fg="white", 
            command=self.limpiar,
            font=("Arial", 12),
            width=15,
            height=1,
            bd=1,
            relief="raised"
        ).grid(row=4, column=0, columnspan=4, pady=(10, 0))
    
    def _obtener_valores(self):
        """Obtiene y valida los valores ingresados por el usuario"""
        try:
            val1 = float(self.valor1.get())
            val2 = float(self.valor2.get())
            return val1, val2
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")
            return None, None
    
    def sumar(self):
        val1, val2 = self._obtener_valores()
        if val1 is not None and val2 is not None:
            resultado = self.calculadora.sumar(val1, val2)
            self.resultado.set(str(resultado))
    
    def restar(self):
        val1, val2 = self._obtener_valores()
        if val1 is not None and val2 is not None:
            resultado = self.calculadora.restar(val1, val2)
            self.resultado.set(str(resultado))
    
    def multiplicar(self):
        val1, val2 = self._obtener_valores()
        if val1 is not None and val2 is not None:
            resultado = self.calculadora.multiplicar(val1, val2)
            self.resultado.set(str(resultado))
    
    def dividir(self):
        val1, val2 = self._obtener_valores()
        if val1 is not None and val2 is not None:
            try:
                resultado = self.calculadora.dividir(val1, val2)
                self.resultado.set(str(resultado))
            except ValueError as e:
                messagebox.showerror("Error", str(e))
    
    def limpiar(self):
        self.valor1.set("")
        self.valor2.set("")
        self.resultado.set("0")

def main():
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
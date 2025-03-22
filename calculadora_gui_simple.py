#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import math
from calculadora import Calculadora

class CalculadoraGUISimple:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E2E")  # Fondo principal más oscuro
        
        self.calculadora = Calculadora()
        
        # Variables para la calculadora
        self.valor_actual = tk.StringVar(value="0")
        self.primer_operando = 0
        self.operador = None
        self.reiniciar_pantalla = True
        
        self._crear_interfaz()
        
    def _crear_interfaz(self):
        # Estilo de botones
        estilo_boton = {
            "font": ("Arial", 12, "bold"),
            "borderwidth": 1,
            "relief": tk.RAISED,
            "width": 5,
            "height": 2,
        }
        
        # Nueva paleta de colores
        estilo_boton_operacion = estilo_boton.copy()
        estilo_boton_operacion["bg"] = "#F5A97F"  # Color melocotón
        estilo_boton_operacion["fg"] = "#1E1E2E"  # Texto oscuro
        
        estilo_boton_numero = estilo_boton.copy()
        estilo_boton_numero["bg"] = "#C9CBFF"  # Azul lavanda
        estilo_boton_numero["fg"] = "#1E1E2E"  # Texto oscuro
        
        estilo_boton_igual = estilo_boton.copy()
        estilo_boton_igual["bg"] = "#ABE9B3"  # Verde menta
        estilo_boton_igual["fg"] = "#1E1E2E"  # Texto oscuro
        
        estilo_boton_borrar = estilo_boton.copy()
        estilo_boton_borrar["bg"] = "#F28FAD"  # Rosa
        estilo_boton_borrar["fg"] = "#1E1E2E"  # Texto oscuro
        
        estilo_boton_funcion = estilo_boton.copy()
        estilo_boton_funcion["bg"] = "#96CDFB"  # Azul cielo
        estilo_boton_funcion["fg"] = "#1E1E2E"  # Texto oscuro
        
        estilo_boton_memoria = estilo_boton.copy()
        estilo_boton_memoria["bg"] = "#DDB6F2"  # Lila
        estilo_boton_memoria["fg"] = "#1E1E2E"  # Texto oscuro
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#1E1E2E", padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)
        
        # Pantalla de resultados
        pantalla = tk.Entry(
            main_frame,
            textvariable=self.valor_actual,
            font=("Arial", 24),
            borderwidth=1,
            justify="right",
            bg="#302D41",  # Fondo de pantalla oscuro
            fg="#D9E0EE",  # Texto claro
        )
        pantalla.grid(row=0, column=0, columnspan=6, pady=(0, 10), sticky="nsew")
        
        # Fila de botones de memoria y funciones especiales
        tk.Button(main_frame, text="MC", command=lambda: self.memoria_borrar(), **estilo_boton_memoria).grid(row=1, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="MR", command=lambda: self.memoria_recuperar(), **estilo_boton_memoria).grid(row=1, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="M+", command=lambda: self.memoria_sumar(), **estilo_boton_memoria).grid(row=1, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="M-", command=lambda: self.memoria_restar(), **estilo_boton_memoria).grid(row=1, column=3, padx=2, pady=2)
        tk.Button(main_frame, text="MS", command=lambda: self.memoria_guardar(), **estilo_boton_memoria).grid(row=1, column=4, padx=2, pady=2)
        tk.Button(main_frame, text="C", command=self.limpiar, **estilo_boton_borrar).grid(row=1, column=5, padx=2, pady=2)
        
        # Fila de funciones científicas
        tk.Button(main_frame, text="√", command=lambda: self.raiz_cuadrada(), **estilo_boton_funcion).grid(row=2, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="x²", command=lambda: self.cuadrado(), **estilo_boton_funcion).grid(row=2, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="xʸ", command=lambda: self.definir_operacion("potencia"), **estilo_boton_funcion).grid(row=2, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="sin", command=lambda: self.calcular_seno(), **estilo_boton_funcion).grid(row=2, column=3, padx=2, pady=2)
        tk.Button(main_frame, text="cos", command=lambda: self.calcular_coseno(), **estilo_boton_funcion).grid(row=2, column=4, padx=2, pady=2)
        tk.Button(main_frame, text="tan", command=lambda: self.calcular_tangente(), **estilo_boton_funcion).grid(row=2, column=5, padx=2, pady=2)
        
        # Fila de botones 7, 8, 9, /
        tk.Button(main_frame, text="7", command=lambda: self.agregar_digito("7"), **estilo_boton_numero).grid(row=3, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="8", command=lambda: self.agregar_digito("8"), **estilo_boton_numero).grid(row=3, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="9", command=lambda: self.agregar_digito("9"), **estilo_boton_numero).grid(row=3, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="÷", command=lambda: self.definir_operacion("dividir"), **estilo_boton_operacion).grid(row=3, column=3, padx=2, pady=2)
        tk.Button(main_frame, text="log", command=lambda: self.calcular_logaritmo(), **estilo_boton_funcion).grid(row=3, column=4, padx=2, pady=2)
        tk.Button(main_frame, text="ln", command=lambda: self.calcular_logaritmo_natural(), **estilo_boton_funcion).grid(row=3, column=5, padx=2, pady=2)
        
        # Fila de botones 4, 5, 6, *
        tk.Button(main_frame, text="4", command=lambda: self.agregar_digito("4"), **estilo_boton_numero).grid(row=4, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="5", command=lambda: self.agregar_digito("5"), **estilo_boton_numero).grid(row=4, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="6", command=lambda: self.agregar_digito("6"), **estilo_boton_numero).grid(row=4, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="×", command=lambda: self.definir_operacion("multiplicar"), **estilo_boton_operacion).grid(row=4, column=3, padx=2, pady=2)
        tk.Button(main_frame, text="(", command=lambda: self.agregar_digito("("), **estilo_boton_funcion).grid(row=4, column=4, padx=2, pady=2)
        tk.Button(main_frame, text=")", command=lambda: self.agregar_digito(")"), **estilo_boton_funcion).grid(row=4, column=5, padx=2, pady=2)
        
        # Fila de botones 1, 2, 3, -
        tk.Button(main_frame, text="1", command=lambda: self.agregar_digito("1"), **estilo_boton_numero).grid(row=5, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="2", command=lambda: self.agregar_digito("2"), **estilo_boton_numero).grid(row=5, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="3", command=lambda: self.agregar_digito("3"), **estilo_boton_numero).grid(row=5, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="-", command=lambda: self.definir_operacion("restar"), **estilo_boton_operacion).grid(row=5, column=3, padx=2, pady=2)
        tk.Button(main_frame, text="π", command=lambda: self.agregar_pi(), **estilo_boton_funcion).grid(row=5, column=4, padx=2, pady=2)
        tk.Button(main_frame, text="%", command=lambda: self.definir_operacion("porcentaje"), **estilo_boton_funcion).grid(row=5, column=5, padx=2, pady=2)
        
        # Fila de botones 0, ., +
        tk.Button(main_frame, text="0", command=lambda: self.agregar_digito("0"), **estilo_boton_numero).grid(row=6, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")
        tk.Button(main_frame, text=".", command=self.agregar_punto, **estilo_boton_numero).grid(row=6, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="+", command=lambda: self.definir_operacion("sumar"), **estilo_boton_operacion).grid(row=6, column=3, padx=2, pady=2)
        tk.Button(main_frame, text="e", command=lambda: self.agregar_e(), **estilo_boton_funcion).grid(row=6, column=4, padx=2, pady=2)
        tk.Button(main_frame, text="=", command=self.calcular_resultado, **estilo_boton_igual).grid(row=6, column=5, padx=2, pady=2)
    
    def agregar_digito(self, digito):
        valor_actual = self.valor_actual.get()
        
        if self.reiniciar_pantalla or valor_actual == "0":
            self.valor_actual.set(digito)
            self.reiniciar_pantalla = False
        else:
            self.valor_actual.set(valor_actual + digito)
    
    def agregar_punto(self):
        valor_actual = self.valor_actual.get()
        
        if self.reiniciar_pantalla:
            self.valor_actual.set("0.")
            self.reiniciar_pantalla = False
        elif "." not in valor_actual:
            self.valor_actual.set(valor_actual + ".")
    
    def agregar_pi(self):
        self.valor_actual.set(str(math.pi))
        self.reiniciar_pantalla = False
    
    def agregar_e(self):
        self.valor_actual.set(str(math.e))
        self.reiniciar_pantalla = False
    
    def limpiar(self):
        self.valor_actual.set("0")
        self.primer_operando = 0
        self.operador = None
        self.reiniciar_pantalla = True
    
    def memoria_guardar(self):
        try:
            valor = float(self.valor_actual.get())
            self.calculadora.memoria_guardar(valor)
            messagebox.showinfo("Memoria", f"Valor {valor} guardado en memoria")
            self.reiniciar_pantalla = True
        except ValueError:
            messagebox.showerror("Error", "Valor no válido")
    
    def memoria_recuperar(self):
        valor = self.calculadora.memoria_recuperar()
        self.valor_actual.set(str(valor))
        self.reiniciar_pantalla = True
    
    def memoria_sumar(self):
        try:
            valor = float(self.valor_actual.get())
            nuevo_valor = self.calculadora.memoria_sumar(valor)
            messagebox.showinfo("Memoria", f"Nuevo valor en memoria: {nuevo_valor}")
            self.reiniciar_pantalla = True
        except ValueError:
            messagebox.showerror("Error", "Valor no válido")
    
    def memoria_restar(self):
        try:
            valor = float(self.valor_actual.get())
            nuevo_valor = self.calculadora.memoria_restar(valor)
            messagebox.showinfo("Memoria", f"Nuevo valor en memoria: {nuevo_valor}")
            self.reiniciar_pantalla = True
        except ValueError:
            messagebox.showerror("Error", "Valor no válido")
    
    def memoria_borrar(self):
        self.calculadora.memoria_guardar(0)
        messagebox.showinfo("Memoria", "Memoria borrada")
    
    def raiz_cuadrada(self):
        try:
            valor = float(self.valor_actual.get())
            resultado = self.calculadora.raiz_cuadrada(valor)
            self.valor_actual.set(str(resultado))
            self.reiniciar_pantalla = True
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def cuadrado(self):
        try:
            valor = float(self.valor_actual.get())
            resultado = self.calculadora.potencia(valor, 2)
            self.valor_actual.set(str(resultado))
            self.reiniciar_pantalla = True
        except ValueError:
            messagebox.showerror("Error", "Valor no válido")
    
    def calcular_seno(self):
        try:
            valor = float(self.valor_actual.get())
            resultado = self.calculadora.seno(valor)
            self.valor_actual.set(str(resultado))
            self.reiniciar_pantalla = True
        except ValueError:
            messagebox.showerror("Error", "Valor no válido")
    
    def calcular_coseno(self):
        try:
            valor = float(self.valor_actual.get())
            resultado = self.calculadora.coseno(valor)
            self.valor_actual.set(str(resultado))
            self.reiniciar_pantalla = True
        except ValueError:
            messagebox.showerror("Error", "Valor no válido")
    
    def calcular_tangente(self):
        try:
            valor = float(self.valor_actual.get())
            resultado = self.calculadora.tangente(valor)
            self.valor_actual.set(str(resultado))
            self.reiniciar_pantalla = True
        except ValueError:
            messagebox.showerror("Error", "Valor no válido")
    
    def calcular_logaritmo(self):
        try:
            valor = float(self.valor_actual.get())
            resultado = self.calculadora.logaritmo(valor, 10)
            self.valor_actual.set(str(resultado))
            self.reiniciar_pantalla = True
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def calcular_logaritmo_natural(self):
        try:
            valor = float(self.valor_actual.get())
            resultado = self.calculadora.logaritmo(valor, math.e)
            self.valor_actual.set(str(resultado))
            self.reiniciar_pantalla = True
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def definir_operacion(self, operacion):
        try:
            valor_actual = float(self.valor_actual.get())
            
            if self.operador is not None:
                self.calcular_resultado()
                valor_actual = float(self.valor_actual.get())
            
            self.primer_operando = valor_actual
            self.operador = operacion
            self.reiniciar_pantalla = True
        except ValueError:
            messagebox.showerror("Error", "Valor no válido")
            self.reiniciar_pantalla = True
    
    def calcular_resultado(self):
        if self.operador is None:
            return
        
        try:
            segundo_operando = float(self.valor_actual.get())
            resultado = 0
            
            if self.operador == "sumar":
                resultado = self.calculadora.sumar(self.primer_operando, segundo_operando)
            elif self.operador == "restar":
                resultado = self.calculadora.restar(self.primer_operando, segundo_operando)
            elif self.operador == "multiplicar":
                resultado = self.calculadora.multiplicar(self.primer_operando, segundo_operando)
            elif self.operador == "dividir":
                resultado = self.calculadora.dividir(self.primer_operando, segundo_operando)
            elif self.operador == "potencia":
                resultado = self.calculadora.potencia(self.primer_operando, segundo_operando)
            elif self.operador == "porcentaje":
                resultado = self.calculadora.porcentaje(self.primer_operando, segundo_operando)
            
            # Formatear el resultado para evitar decimales innecesarios
            if resultado == int(resultado):
                self.valor_actual.set(str(int(resultado)))
            else:
                self.valor_actual.set(str(resultado))
            
            self.operador = None
            self.reiniciar_pantalla = True
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.reiniciar_pantalla = True
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.reiniciar_pantalla = True

def main():
    root = tk.Tk()
    app = CalculadoraGUISimple(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
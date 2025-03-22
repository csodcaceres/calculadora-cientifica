#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.memoria = 0  # Para guardar valores en memoria

    def sumar(self, a, b):
        """Suma dos números y devuelve el resultado."""
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        """Resta dos números y devuelve el resultado."""
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        """Multiplica dos números y devuelve el resultado."""
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        """Divide dos números y devuelve el resultado."""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        self.resultado = a / b
        return self.resultado
    
    def potencia(self, a, b):
        """Eleva a a la potencia b y devuelve el resultado."""
        self.resultado = a ** b
        return self.resultado
    
    def raiz_cuadrada(self, a):
        """Calcula la raíz cuadrada de a y devuelve el resultado."""
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        self.resultado = math.sqrt(a)
        return self.resultado
    
    def porcentaje(self, a, b):
        """Calcula el porcentaje de a sobre b."""
        self.resultado = (a * b) / 100
        return self.resultado
    
    def seno(self, a):
        """Calcula el seno de un ángulo en radianes."""
        self.resultado = math.sin(a)
        return self.resultado
    
    def coseno(self, a):
        """Calcula el coseno de un ángulo en radianes."""
        self.resultado = math.cos(a)
        return self.resultado
    
    def tangente(self, a):
        """Calcula la tangente de un ángulo en radianes."""
        self.resultado = math.tan(a)
        return self.resultado
    
    def logaritmo(self, a, base=10):
        """Calcula el logaritmo de a en la base especificada."""
        if a <= 0:
            raise ValueError("El argumento debe ser positivo")
        if base <= 0 or base == 1:
            raise ValueError("La base debe ser positiva y distinta de 1")
        
        if base == 10:
            self.resultado = math.log10(a)
        elif base == math.e:
            self.resultado = math.log(a)
        else:
            self.resultado = math.log(a, base)
        
        return self.resultado
    
    def memoria_guardar(self, valor):
        """Guarda un valor en la memoria de la calculadora."""
        self.memoria = valor
        return self.memoria
    
    def memoria_recuperar(self):
        """Recupera el valor almacenado en la memoria."""
        return self.memoria
    
    def memoria_sumar(self, valor):
        """Suma un valor a la memoria."""
        self.memoria += valor
        return self.memoria
    
    def memoria_restar(self, valor):
        """Resta un valor a la memoria."""
        self.memoria -= valor
        return self.memoria

def menu():
    """Muestra el menú principal de la aplicación."""
    print("\n=== CALCULADORA PYTHON ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Porcentaje")
    print("8. Funciones trigonométricas")
    print("9. Logaritmo")
    print("10. Memoria")
    print("11. Salir")
    return input("Seleccione una opción (1-11): ")

def menu_trigonometria():
    """Muestra el menú de funciones trigonométricas."""
    print("\n=== FUNCIONES TRIGONOMÉTRICAS ===")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Volver al menú principal")
    return input("Seleccione una opción (1-4): ")

def menu_memoria():
    """Muestra el menú de operaciones de memoria."""
    print("\n=== OPERACIONES DE MEMORIA ===")
    print("1. Guardar valor en memoria")
    print("2. Recuperar valor de memoria")
    print("3. Sumar a memoria")
    print("4. Restar a memoria")
    print("5. Volver al menú principal")
    return input("Seleccione una opción (1-5): ")

def main():
    """Función principal del programa."""
    calc = Calculadora()
    
    while True:
        opcion = menu()
        
        if opcion == '11':
            print("¡Hasta luego!")
            break
            
        if opcion not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
            print("Opción no válida. Intente de nuevo.")
            continue
        
        try:
            if opcion == '6':  # Raíz cuadrada
                a = float(input("Ingrese el número: "))
                try:
                    print(f"Resultado: {calc.raiz_cuadrada(a)}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif opcion == '8':  # Funciones trigonométricas
                opcion_trig = menu_trigonometria()
                if opcion_trig not in ('1', '2', '3'):
                    continue
                    
                a = float(input("Ingrese el ángulo en radianes: "))
                if opcion_trig == '1':
                    print(f"Resultado: {calc.seno(a)}")
                elif opcion_trig == '2':
                    print(f"Resultado: {calc.coseno(a)}")
                elif opcion_trig == '3':
                    print(f"Resultado: {calc.tangente(a)}")
            elif opcion == '9':  # Logaritmo
                a = float(input("Ingrese el número: "))
                base_opcion = input("¿Desea cambiar la base (10 por defecto)? (s/n): ")
                
                if base_opcion.lower() == 's':
                    base = float(input("Ingrese la base: "))
                    try:
                        print(f"Resultado: {calc.logaritmo(a, base)}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    try:
                        print(f"Resultado: {calc.logaritmo(a)}")
                    except ValueError as e:
                        print(f"Error: {e}")
            elif opcion == '10':  # Memoria
                opcion_mem = menu_memoria()
                
                if opcion_mem == '1':
                    valor = float(input("Ingrese el valor para guardar en memoria: "))
                    calc.memoria_guardar(valor)
                    print(f"Valor {valor} guardado en memoria.")
                elif opcion_mem == '2':
                    print(f"Valor en memoria: {calc.memoria_recuperar()}")
                elif opcion_mem == '3':
                    valor = float(input("Ingrese el valor para sumar a memoria: "))
                    nuevo_valor = calc.memoria_sumar(valor)
                    print(f"Nuevo valor en memoria: {nuevo_valor}")
                elif opcion_mem == '4':
                    valor = float(input("Ingrese el valor para restar a memoria: "))
                    nuevo_valor = calc.memoria_restar(valor)
                    print(f"Nuevo valor en memoria: {nuevo_valor}")
            else:  # Operaciones con dos operandos
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                
                if opcion == '1':
                    print(f"Resultado: {calc.sumar(a, b)}")
                elif opcion == '2':
                    print(f"Resultado: {calc.restar(a, b)}")
                elif opcion == '3':
                    print(f"Resultado: {calc.multiplicar(a, b)}")
                elif opcion == '4':
                    try:
                        print(f"Resultado: {calc.dividir(a, b)}")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif opcion == '5':
                    print(f"Resultado: {calc.potencia(a, b)}")
                elif opcion == '7':
                    print(f"El {a}% de {b} es: {calc.porcentaje(a, b)}")
        except ValueError:
            print("Error: Ingrese solo números válidos.")

if __name__ == "__main__":
    main() 
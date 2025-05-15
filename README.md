# Calculadora Python

Una aplicación de calculadora simple escrita en Python.

## Características

- Operaciones matemáticas:
  - Operaciones básicas: suma, resta, multiplicación y división
  - Funciones potencia y raíz cuadrada
  - Operaciones porcentuales
  - Funciones trigonométricas (seno, coseno, tangente)
  - Logaritmos (base 10 y natural)
  - Constantes matemáticas (π, e)
  - Sistema de memoria (guardar, recuperar, sumar, restar, borrar)
  
- Múltiples versiones disponibles:
  - Interfaz de línea de comandos
  - Interfaz gráfica con formulario
  - Interfaz gráfica de calculadora científica con temas:
    - Tema oscuro con estilo moderno
    - Tema claro con estilo clásico
  - Selector de temas para elegir la apariencia
  
- Manejo de errores (como división por cero)
- Pruebas unitarias

## Requisitos

- Python 3.6+
- UV (gestor de entornos virtuales)
- Tkinter (incluido con Python para las versiones gráficas)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tuusuario/calculadora-python.git
   cd calculadora-python
   ```

2. Crea un entorno virtual con UV:
   ```
   uv venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```
     source .venv/bin/activate
     ```

## Uso

### Selección de tema

Para iniciar el selector de temas y elegir entre las diferentes versiones:

```
python selector_tema.py
```

### Versión de línea de comandos

Para ejecutar la calculadora en modo consola:

```
python calculadora.py
```

Sigue las instrucciones en pantalla para realizar las operaciones deseadas.

### Versión gráfica con formulario

Para ejecutar la calculadora con interfaz gráfica de formulario:

```
python calculadora_gui.py
```

Esta interfaz ofrece:
- Campos para ingresar dos números
- Botones para operaciones básicas (suma, resta, multiplicación, división)
- Visualización clara del resultado
- Botón para limpiar todos los campos

### Versión gráfica de calculadora científica (tema oscuro)

Para ejecutar la calculadora científica con tema oscuro:

```
python calculadora_gui_simple.py
```

### Versión gráfica de calculadora científica (tema claro)

Para ejecutar la calculadora científica con tema claro:

```
python calculadora_tema_claro.py
```

Las interfaces científicas ofrecen:
- Teclado numérico (0-9)
- Botones para operaciones básicas (+, -, ×, ÷)
- Funciones científicas (trigonometría, logaritmos, potencias)
- Constantes matemáticas (π, e)
- Sistema de memoria para almacenar resultados
- Pantalla para visualizar números y resultados
- Soporte para números decimales

## Pruebas

Para ejecutar las pruebas unitarias:

```
python test_calculadora.py
```

## Estructura del proyecto

```
calculadora-python/
├── calculadora.py          # Implementación principal de la calculadora (consola)
├── calculadora_gui.py      # Versión gráfica con formulario
├── calculadora_gui_simple.py # Versión gráfica de calculadora científica (tema oscuro)
├── calculadora_tema_claro.py # Versión gráfica de calculadora científica (tema claro)
├── selector_tema.py        # Selector de temas y versiones
├── test_calculadora.py     # Pruebas unitarias
└── README.md               # Documentación del proyecto
```

## Licencia

Este proyecto es libre

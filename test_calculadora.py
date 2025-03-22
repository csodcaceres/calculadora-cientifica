#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba."""
        self.calc = Calculadora()
        
    def test_sumar(self):
        """Prueba la función de suma."""
        self.assertEqual(self.calc.sumar(3, 5), 8)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(-1, -1), -2)
        
    def test_restar(self):
        """Prueba la función de resta."""
        self.assertEqual(self.calc.restar(5, 3), 2)
        self.assertEqual(self.calc.restar(1, 1), 0)
        self.assertEqual(self.calc.restar(-1, -1), 0)
        
    def test_multiplicar(self):
        """Prueba la función de multiplicación."""
        self.assertEqual(self.calc.multiplicar(3, 5), 15)
        self.assertEqual(self.calc.multiplicar(0, 5), 0)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        
    def test_dividir(self):
        """Prueba la función de división."""
        self.assertEqual(self.calc.dividir(6, 3), 2)
        self.assertEqual(self.calc.dividir(5, 2), 2.5)
        
        # Prueba de división por cero
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)
            
if __name__ == "__main__":
    unittest.main() 
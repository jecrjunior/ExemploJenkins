# -*- coding: utf-8 -*-
''' Módulo de teste para o módulo calculadora
'''
import unittest, random as rand

class TestCalculadora(unittest.TestCase):
   ''' TestCase para a classe Calculadora
   '''
   def test_somar(self):
       ''' Testa o método de instância: somar
       '''
       calc = Calculadora()
       valor1 = rand.randint(1, 50)
       valor2 = rand.randint(51, 100)
       self.assertEqual(calc.somar(valor1, valor2), valor1 + valor2)

# Debugging

# identificar erros no codigo ou entender seu funcionamento

#print

def dividir(a,b):
    print(f"Dividindo {a} por {b}")
    
    if b == 0:
        print("Erro: Divisão por 0")
        return None
    
    
    resultado = a / b
    print(f"O resultado da divisão foi {resultado}")
    return resultado

dividir(10,2)
dividir(10,0)

# pdb (python debugger)
import pdb

def dividir2(a,b):
    #pdb.set_trace()
    
    if b == 0:
        return None
    
    
    resultado = a / b
    return resultado


dividir2(10,2)
dividir2(10,0)

# testes unitarios

import unittest

def somar(a, b):
    return a + b

class TesteSomar(unittest.TestCase):
    def teste_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)
    def teste_somar_negativos(self):
        self.assertEqual(somar(-1, -1), -2)
    def teste_somar_zero(self):
        self.assertEqual(somar(2, 0), 0)
        
#if __name__ == "__main__":
 #   print("Iniciando teste")
 #   unittest.main()


import logging

logging.basicConfig(level=logging.INFO) 

def dividir(a, b):
    try:
        resultado = a / b
        logging.info(f"Divisão bem-sucedida: {a} / {b} = {resultado}")
        return resultado
    except ZeroDivisionError: 
        logging.error("Erro: tentativa de devisão por zero.")
        return None

dividir(10,2)
dividir(10,0)
       

def multiplicar(a,b):
    return a * b


resultado = multiplicar(1,2)
print(resultado)

def soma(a,b):
    return a + b


class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 2), 4)
        
    def test_soma_negativos(self):
        self.assertEqual(soma(-2, -2), -4)
        
    def test_soma_zero(self):
        self.assertEqual(soma(2, 0), 2)
        
#if __name__ == "__main__":
#    print("Iniciando teste")
#    unittest.main()
    
import pdb

def subtrair(a,b):
    pdb.set_trace()
    return a -b

resultado = subtrair(10,5)
print(resultado)

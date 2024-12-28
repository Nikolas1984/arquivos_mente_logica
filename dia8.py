#função padrão
def funcao_imprimir():
    print("Hello world")

#Chamada de função     
funcao_imprimir()

#função  com parametro
def saudacao(nome):
    print(f"Ola {nome}, seja bem vindo ")
    
saudacao("Severino")

#parametros opcionais com valor padrao     
def saudacao2(nome,mensagem ="Seja bem vindo."):
    print(f"Olá , {nome}! {mensagem}")

saudacao2("Valeria" )
#chamando func e alterando o valor padrão
saudacao2("Valeria","Sussa na bazuca?")

#retorno de valores
def soma (a,b):
    resultado = a + b
    return resultado

resultado = soma(3,2)
print("Resultado = ",resultado)

#Se uma função não possui um retorno, ela por padrao retora None no python, em outras linguagens ela retorna null ou zero
def multi (a,b):
    resultado = a * b

resultado = multi(1,2)
print(resultado)

#escopo de variaveis
#variavel global
variavel_global = "Ola, mundo"


def global_var():
    print(variavel_global)

global_var()

#variavel local
def calcular_area():
    largura = 5
    altura = 3
    area = largura * altura
    print("Área:", area)
    
calcular_area()
#print(area) da erro pois a variavel nao é reconhecida

#Variaveis locais e globais com o mesmo nome
numero = 10

def mostrar_numero():
    numero = 5
    print("Numero dentro da função", numero)


mostrar_numero()
print("Numero fora da função = ",numero)

contador = 0

def incrementar():
    global contador
    contador += 1

print("contador antes da func ",contador)    
incrementar()
print("Contador: ", contador)

#Calculadora com funções

def soma (a,b):
    soma = a + b
    print(f"A soma entre {a} e {b} é igual a :", soma)

def multi (a,b):
    multi = a * b
    print(f"A multiplicação entre {a} e {b} é igual a :", multi)

def div (a,b):
    div = a / b
    print(f"A divisão entre {a} e {b} é igual a :", div)

def sub (a,b):
    sub = a - b
    print(f"A subtração entre {a} e {b} é igual a :", sub)


#Loop para ler os valores
while True:
    numero_um = float(input("Digite o primeiro numero: "))
    numero_dois = float(input("Digite o segundo numero: "))
    operacao = input("Digite a operação desejada entre +,-,/ e * : ")
    
    if(operacao == "-"):
        sub(numero_um,numero_dois)
        
    elif(operacao == "+"):
        soma(numero_um,numero_dois)
        
    elif(operacao == "/"):
       div(numero_um,numero_dois)
     
    elif(operacao == "*"):
       multi(numero_um,numero_dois)  
    
    else:
        print("Digite uma operação vàlida")
        
    operacao = input("Deseja realizar outro calculo? S/N ")
    if(operacao == "S"):
        continue
    elif(operacao == "N"):
        break
    else:
        print("Opção invàlida, reiniciando programa")
        continue
    
 # verificar se o numero é primo       
def primo(numero):
    if numero < 1:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um numero inteiro: "))

if primo(numero):
    print(f"O numero {numero} é um numero primo")
else:
    print(f"O numero {numero} não é um numero primo")
    
    
#Conversor de temperaturas

def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_para_celsius(f):
    return (f-32) * 5/9

def celsius_para_kelvin(c):
    return c + 273.15 

def kelvin_para_celsius(k):
    return k - 237.15

temperatura = float(input("Digite a temperatura desejada: "))
unidade = input("Digite a unidade atual (C,K,F): ").upper()
converter = input("Digite a unidade na qual deseja converter (C,K,F): ").upper()

if(unidade == "C"):
    if(converter == "F"):
        resultado = celsius_para_fahrenheit(temperatura)
    elif(converter == "K"):
        resultado = celsius_para_kelvin(temperatura)
elif(unidade == "F"):
    if(converter == "C"):
        resultado = fahrenheit_para_celsius(temperatura)
elif(unidade == "K"):
    if(converter == "C"):
        resultado = kelvin_para_celsius(temperatura)
    elif converter == "F":
        celsius = kelvin_para_celsius(temperatura)
        resultado = celsius_para_fahrenheit(celsius)
else:
    resultado = "Operação inválida"
    
print(f"Temperatura convertida: {resultado} {converter}")

#funcao recursiva para calcular fatorial

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * fatorial(n - 1)
    
num = int(input("Digite um número inteiro positivo"))
if num >= 1:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}.")
else :
    print("Numero inválido")
    
#gerador de senhas aleatorias
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada"))
senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada: ",senha_gerada)

import math

def distancia(ponto1, ponto2):
    x1,y1 = ponto1
    x2,y2 = ponto2
    return math.sqrt((x2 - x1)**2 + (y2-y1) **2)

x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

distancia_pontos = distancia((x1,y1),(x2,y2))
print(f"A distancia enter os pontos é: {distancia_pontos}")

def palindromo(texto):
    texto = ''.join(char.lower() for char in texto if char.isalnum())
    return texto == texto[::-1]

frase = input("Diite uma frase ou palavra ")
if palindromo(frase):
    print("É um palindromo")
else:
    print("Não é um palindromo")
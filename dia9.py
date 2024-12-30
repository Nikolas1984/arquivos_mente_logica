#modulo = conjunto de funções que realizam determinadas ações/ operacoes
#biblioteca = composta por varios modulos

import math
numero = 16
raiz_quadrada = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")


#podemos importar apenas algumas funcoes do modulo

from math import sqrt, pi

print(f"O valor de pi é {pi}")
print(f"A raiz quadrada de 25 é {sqrt(25)}")

#podemos dar apelidos para os modulos importados

import math as m

print(f"Cosseno de 0 é {m.cos(0)}")

#bibliotecas
import random

#dado simulado
dado = random.randint(1,6)
print(f"O resultado do dado é: {dado}")

from datetime import datetime

agora = datetime.now()
print(f"Data e hora atuais: {agora}")

import os
arquivos = os.listdir('.')
print("Arquivos no diretorio at",arquivos)

#biblioteca com o pip
#pip install nome_da_biblioteca
import requests

resposta = requests.get('https://api.github.com')
print(f"Status da Resposta: {resposta.status_code}")

#criar modulos
#precisamos criar um arquivo com as funcoes desejadas

import meu_modulo

mensagem = meu_modulo.saudacao("Thiago")
soma = meu_modulo.soma(3,7)

print(mensagem)
print("O resultado da soma é: ",soma)


import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1,100)
    tentativas = 0
    
    print("Bem vindo ao jogo da adivinhação")
    print("Tente adivinhar o numero entre 1 e 100.")
    
    while True:
        palpite = int(input("Digite o palpite: "))
        tentativas += 1
        
        if palpite == numero_secreto:
            print(f"Parabens, voce acertou em {tentativas} tentativas",)
            break
        elif palpite < numero_secreto:
            print(f"O numero é maior que {palpite}")
        elif palpite > numero_secreto:
            print(f"O numero é menor que {palpite}")
            
jogo_adivinhacao()

import os
def manipular_arquivos():
    # Criando uma pasta
    os.mkdir('nova_pasta')
    print("Pasta 'nova_pasta' criada.")
    
    # Mudando para o novo diretório
    os.chdir('nova_pasta')
    
    # Criando um arquivo
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write("Este é um arquivo dentro da nova pasta.")
    print("Arquivo 'arquivo.txt' criado dentro de 'nova_pasta'.")
    
    # Listando arquivos
    arquivos = os.listdir('.')
    print("Arquivos no diretório atual:", arquivos)

manipular_arquivos()
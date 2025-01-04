# Em python, uma string pode ser declarada com aspa simples ou aspas duplas

frase_1 = "Ola, Mundo"
frase_2 = "Ta maluco"
print(frase_1)
print(frase_2)

#concatenar

ola = "Ola, "
paula = 'Paula'
concatenar = ola + paula
print(concatenar)

# Em python podemos repetir strings

risada = "Ha" * 3
print(risada)

#fatiar e indexar

frase = "Antedeguemon"
frase_primeiro_caractere = frase[0]
print(frase_primeiro_caractere)

#fatiar
palavra = "Programação"
fatia = palavra[0:6]
print(fatia)

#Tamanho da string utiliza a funcao len()
frase = 'aprendendo python'
tamanho_frase = len(frase)
print(tamanho_frase)

#Inserido valores dentro da string
idade = 25
mensagem = "Eu tenho {} anos".format(idade)
print(mensagem)

#f-strings versao mais simples do format

nome = "Carlos"
cidade = "São Paulo"
mensagem = f"Meu nome é {nome} e moro em {cidade}"
print(mensagem) 

#metodos comuns de strings em python

#upper() Transforma todos os caracteres em maiusculas
#lower()Transforma todos os caracteres em minusculos
#title() Transforma a primeira letra de cada palavra em maiuscula
#capitalize() Transforma a primeira letra da frase em maiuscula
texto = 'Bom dia'
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())

#Removendo espaços em branco
#strip()
texto = " Olá  "
print(texto.strip())

#Substituindo partes da string
#replace()

frase = "Aprender Java é divertido"
nova_frase = frase.replace("Java","Python")
print(nova_frase)

#Encontrando substrings 
frase = 'Onde está o Wally?'
posicao = frase.find ("Wally")
print(f"Wally está na posição {posicao}")

#dividindo e juntando strings
#split() divide a string em uma lista
dados = "Maça,banana,laranja"
lista_frutas = dados.split(",")
print(dados)
print(lista_frutas)

#join junta os elementos de uma lista em uma string

lista_palavras = ["Python", "é", "legal"]
frase = " ".join(lista_palavras)
print(frase)

#contador de vogais
contador = 0
frase = input("Digite a frase desejada: ").lower()
vogais = "aeiou"

for i in frase:
    if i in vogais:
        contador += 1
print(f"A frase tem {contador} vogais")

#inversor de string
frase = input("Digite outra frase: ")
palavras = frase.split()
frase_invertida = " ".join(reversed(palavras))
print(f"Frase invertida: {frase_invertida}")

#palindromo
palavra = input("Digite a palavra desejada: ").lower()
palavra_sem_espaco = palavra.replace(" ", "")

if (palavra_sem_espaco == palavra_sem_espaco[::-1]):
    print(f"A palavra {palavra} é um palindromo")
else:
    print(f"A palavra {palavra} não um palindromo")

#senha forte

senha = input("Digite uma senha: ")

tem_maiusuclua = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_simbolo = any(not c.isalnum() for c in senha)
tamanho_adequado = len(senha) >= 8

if(tem_maiusuclua and tem_maiusuclua and tem_numero and tem_simbolo and tamanho_adequado):
    print("Senha forte")
    
else:
    print("Senha fraca. Tente novamente")
 
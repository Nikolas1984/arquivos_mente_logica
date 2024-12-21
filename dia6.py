#listas e tuplas

#Listas são arrays padrao, que podem ser do tipo int, float e string, podendo ser alterados e inseridos

#Ja tuplas são imutaveis, nao podemos alterar os dados nelas depois da criação

#Array
lista = ["Azul", "Preto", "Branco"]

print(lista)
print(lista[0])

for cor in lista:
    print("Cor: ",cor)

lista.append("Marrom")
print(lista)
lista.remove("Azul")
print(lista)

#Tuple
print("Tupla:")
tupla = ("a","b","c")

print(tupla)
print(tupla[1])

for letra in tupla:
    print("Letra: ",letra)


#Converter lista em tupla  

lista_frutas = ["maçã", "banana", "laranja"]
tupla_frutas = tuple(lista_frutas)
print(tupla_frutas) 

#Converter Tupla para Lista
lista_letra = list(tupla)
print(lista_letra) 

#A função enumerate() permite obter o índice e o valor ao mesmo tempo.

for indice, fruta in enumerate(lista_frutas):
    print(f"Fruta {indice}: {fruta}")
    
lista_convidados = ["Ana","Bia", "Carlos", "Diggo"]

for nome in lista_convidados:
    print(f"Ola {nome}! voce está convidado")
    
entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)

print("Maior número:", maior_numero)
print("Menor número:", menor_numero )
print("Soma total dos números:",soma_numeros)
print("Media dos números:",media_numeros)

frase = input("Digite uma frase").lower()
letras = {}

for caracteres in frase:
    if caracteres.isalpha():
        if caracteres in letras :
            letras[caracteres] += 1
        else:
            letras[caracteres] = 1
            
for letra, contagem in letras.items():
    print(f"A letra '{letra}' aparece '{contagem}' vez(es)")
    
entrada = input("Digite números separados pro espaço: ")
numeros = [float(num) for num in entrada.split()]

#Ordem Crescente
nuumeros_crescente = sorted(numeros)
print("Numeros em ordem crescente:",nuumeros_crescente)

#Ordem Decrescente
numeros_decrescente = sorted(numeros,reverse=True)
print("Numeros em ordem decrescente",numeros_decrescente)

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ) 

numero_mes = int(input("Digite um numero entre 1 e 12"))

if 1 <= numero_mes <=12:
    print(f"O mes correspondente é {meses[numero_mes-1]}.")
    
else:
    print("Numero inválido, por favor inserir um numero entre 1 e 12")
    
lista_tarefas = []

while True:
    print("Menu")
    print("Digite 1 para incluir uma tarefa")
    print("Digite 2 para remover uma tarefa" )
    print("Digite 3 para listar as tarefas disponiveis")
    print("Digite 4 para sair do programa")
    menu = int(input())

    if menu == 1:
        tarefa = input("Digite a tarefa ser incluida: ")
        lista_tarefas.append(tarefa)
        print(f"A tarefa {tarefa} foi incluida")
    
    elif menu == 2:
        tarefa = input("Digite a tarefa a ser excluida: ")
        if tarefa in lista_tarefas:
            lista_tarefas.remove(tarefa)
            print("Tarefa removida com sucesso")
        
        else:
            print("Tarefa não encontrada")
        
    elif menu == 3:
        print("\nLista de Tarefas")
        for idx, tarefa in enumerate(lista_tarefas,start=1):
            print(f"{idx}. {tarefa}")

    elif menu == 4:
        print("Progragama finalizado")
        break
    else:
        print("Opção inválida, por favor insira novamente")
        
        
notas = []

while True:
    entrada = (input("Digite uma noita (ou 'sair' para finalizar o programa)"))
    if entrada.lower() == 'sair':
        print("Arrivederci")
        break
    else: 
        try:
            nota = float(entrada)
            if 0 <= nota <=10:
                notas.append(nota)
            else: 
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
if notas:
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)
    notas_acima_media = [nota for nota in notas if nota > media]
    
    print("\nResultados:")
    print("Maior nota:",maior_nota)
    print("Menor nota: ", menor_nota)
    print("Média da turma: ", media)
    print("Notas acima da media: " ,notas_acima_media)
    
else:
    print("Nenhuma nota foi inserida")
    
texto = input("Digite um texto: ").lower()
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
        
print("\nContagem de palavras:")        
for palavra, contagem in contagem_palavras.items():
    print(f"A palavra '{palavra}' aparece {contagem} vez(es).")
# algoritmos - para resolver problemas complexos de forma perfomatica

# recursao - fucao chama ela mesma, para resolver um problema

def contar_regressivamente(n):
    if n <= 0:
        print("Fim")
    else:
        print(n)
        contar_regressivamente(n-1)
        
        
contar_regressivamente(10)


# fatorial -> 5 = 5 * 4 * 3 * 2 * 1

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)   
    
    
print(fatorial(5)) 

# Fibonacci

# algoritmos e estruturas de dados sao assuntos de entrevista de emprego

# pesquisa binaria recursiva

# lista que procura um numero
# O algoritmo divide a lista em 2, e procura o numero nessas partes

# Inicio -> onde eu quero (indice) comecar minha busca
# fim -> ate qual indice irei procurar o alvo

def pesquisa_binaria(lista, alvo, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1 # indice do elementeo final
        
    if inicio > fim:
        return - 1
            
    meio = (inicio + fim) // 2
    
    if lista [meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return pesquisa_binaria(lista, alvo, meio + 1, fim) # pesquisando do lado direito
    else:
        return pesquisa_binaria(lista, alvo, inicio, fim - 1) # pesquisando do lado esquerdo
    
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f"Indice do elemento 7: {[pesquisa_binaria(lista, 7)]}")
print(f"Indice do elemento 7: {[pesquisa_binaria(lista, 15)]}")

def fibonacci(n):
    if n == 0:
         return 0 # caso base
    elif n == 1:
         return 1 # caso base
     
    else: 
        return fibonacci(n-1) + fibonacci(n-2) # caso recursivo
     

print(fibonacci(7))

# exercicio 1 - solicitar numero do usuario e calcular o fatorial
def solicitar_numero():
    numero = int(input("Digite o numero que deseja saber o fatorial/fibonacci: "))
    if numero < 0:
        print("Fatorial/Fibonacci não existe para numeros negativos")
    else:
        return numero

numero = solicitar_numero()
print(fatorial(numero))

# exercicio 2 - solicitar o numero do usuario e calcular sua posicao na sequencia fibonacci

numero = solicitar_numero()
print(f"Fibonacci de {numero} é igual a {fibonacci(numero)}")

# exercicio 3 - Contagem regressiva ate zero

def contagem_regressiva(n):
    if n <= 0:
        print("Fim")
    else:
        print(n)
        contar_regressivamente(n-1)




numero = int(input("Digite um numero positivo inteiro"))
contagem_regressiva(numero)


#exercicio 4 - imprimir um triangulo de estrelas

def imprimir_triangulo(n):
    if n > 0:
        imprimir_triangulo(n-1)
        print('*' * n)
        
linhas = int(input("Digite o numero de linhas para o triangulo: "))
if linhas <= 0:
    print("Numero de linhas deve ser positivo")
else:
    imprimir_triangulo(linhas)
    
def soma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

entrada = input("Digite uma lista de numeros separados por espaço: ")
lista = [int(num) for num in entrada.split()]
resultado = soma_lista(lista)
print(f"A soma dos elementos da lsita é {resultado}")
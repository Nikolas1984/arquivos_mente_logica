#Dicionarios sao objetos mesmo

notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.0
}

#conjuntos , eles nao permitem valores duplicados

#lista
frutas = ["maçã","banana","laranja","maçã","banana"]

#transformar lista em conjunto
frutas_unicas = set(frutas)
print(frutas_unicas)

aluno = {
    "nome": "Daniel",
    "idade": 20,
    "curso": "Engenharia"
}

#Acessando valores do dicionario
print(aluno["nome"])

#Adicionando e atgualizanod
aluno["nota"] = 9.5

#atualizanod
aluno["idade"] = 21

#del remove itens do objeto
del aluno["curso"]
print(aluno)

idade = aluno.pop("idade")
print(idade)

#percorrendo dicionario

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
    
#Conjunto
numeros = {1,2,3,4,5}

lista = {1,2,3,4,5}
numeros_unicos = set(lista)
print(numeros_unicos) 

numeros.add(6)

numeros.remove(2)
print(numeros)

#Combinando elementos de 2 conjuntos
conjunto_a = {1,2,3}
conjunto_b = {3,4,5}
uniao = conjunto_a.union(conjunto_b)
print(uniao)

#interseção = elementos comuns aos dois conjuntos
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

#diferença
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)

#contar ocorrencias (quantas vezes algo se repete)
texto  = "banana maçã laranja banana maçã banana"
palavras = texto.split()

contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)
# Encontrar valores unicos
emails = ["a@exemplo.com", "b@exemplo.com", "a@exemplo.com","c@exemplo.com"]
emails_unicos = set(emails)
print(emails_unicos)

#agenda telefonica.
agenda = {}

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso")

def buscar_contato():
    nome = input("Digit o nome do contato a buscar: ")
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado.")
        
def remover_contato():
    nome = input("Digite o contato a ser removido")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso")
    else:
        print("Contato não encontrado")

while True:
    print("\n1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Sair do programa")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
         remover_contato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida")

#  Palavras unicas    
frase = input("Digite uma frase: ")
palavras = frase.split()
palavras_unicas = set(palavras)
print("Palavras únicas:", palavras_unicas)

#Uniao e intersecção de conjuntos
numeros1 = input("Digite números separados por espaço para o primeiro conjunto: ").split()
numeros2 = input("Digite números separados por espaço para o segundo conjunto: ").split()

conjunto1 = set(numeros1)
conjunto2 = set(numeros2)

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)

print("União dos conjuntos", uniao)
print("Intersecção dos conjuntos:") 

#contador de caracteres
texto = input("Digite um texto: ")

contagem = {}

for caractere in texto:
    if caractere in contagem:
        contagem[caractere] +=1
    else:
        contagem[caractere] = 1

print("Contagem de caracteres:")
for caractere, quantidade in contagem.items():
    print(f"'{caractere}': {quantidade}")

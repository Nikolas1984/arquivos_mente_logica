#arquivo = open('dados.txt', 'modo')

arquivo = open('diario.txt', 'r')

conteudo = arquivo.read()
print(conteudo)

linha = arquivo.readline()
while linha:
    print(linha.strip())
    linha = arquivo.readline
    

arquivo = open("saida.txt", 'w')
arquivo.write('Escrevendo uma linha no arquivo.\n')
arquivo.write('Escrevendo outra linha.\n')
arquivo.close()

arquivo = open('saida.txt','a')
arquivo.write('Esta linha será adicionada no final do arquivo.\n')
arquivo.close()

with open('diario.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
with open('receitas.csv', 'r') as arquivo:
    for linha in arquivo:
        colunas = linha.strip().split(',')
        print(colunas)
        
with open('bern.png', 'rb') as origem:
    with open ('copia_bern.png', 'wb') as destino:
        destino.write(origem.read())
        
import json

dados = {
    'nome': 'João',
    'idade': 30,
    'cidades' : ['São Paulo', 'Rio de Janeiro']
}

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent = 4)
    
import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)
    
import csv as csv

with open('contatos.csv','w', newline = '') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Nome','Telefone','Email'])
    escritor.writerow(['Ana','9999-8888','ana@example.com'])
    escritor.writerow(['Pedro','8888-7777','pedro@example.com'])

import csv
with open('contatos.csv','r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
        
nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
else:
    palavras = conteudo.lower().split()
    contagem = {}
    
    for palavra in palavras:
        palavra = palavra.strip('.,!?";:-()')
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
            
    for palavra, quantidade in contagem.items():
        print(f"{palavra}: {quantidade}")
        
import csv

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    with open('contatos.csv','a', newline = '') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([nome,telefone, email])
    print("Contato inserido com sucesso")
    
def listar_contatos():
    try:
        with open('contatos.csv','r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(f"Nome: {linha[0]}, Telefone: {linha[1]}, Email: {linha[2]}")
    
    except FileNotFoundError:
        print("Nenhum contato encontrado")
        
while True:
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        break
    else:
        print("Digite uma opção válida")
        
#Leitor de arquivos json
import json

try:
    with open('produtos.json', 'r') as arquivo:
        produtos = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado")
else:
    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']}")
        print(f"Quantidade: {produto['quantidade']}")
        print("-" * 20)

#Copiador de arquivos
origem = input("Digite o nome do arquivo de origem: ")
destino = input("Digite o nome do arquivo final: ")

try:
    with open(origem, 'rb') as arquivo_origem:
        conteudo = arquivo_origem.read()
    with open(destino, 'wb') as arquivo_destino:
        arquivo_destino.write(conteudo)
except FileNotFoundError:
    print("Arquivo de origem não encontrado")
else:
    print(f"Arquivo {destino} criado com sucesso")
    
#Calculadora de notas
import csv

notas_alunos = []

try:
    with open('notas.csv', 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            nome = linha['Nome']
            nota1 = float(linha['Nota1'])
            nota2 = float(linha['Nota2'])
            nota3 = float(linha['Nota3'])
            media = (nota1 + nota2 + nota3) / 3
            notas_alunos.append({'Nome': nome, 'Média': round(media,2)})
except FileNotFoundError:
    print("Arquivo de notas não encontrado.")
else:
    with open('medias.csv','w', newline='') as arquivo_csv:
        campos = ['Nome', 'Média']
        escritor = csv.DictWriter(arquivo_csv, fieldnames = campos)
        escritor.writeheader()
        for aluno in notas_alunos:
            escritor.writerow(aluno)
    print("Médias calculadas e salvas no arquivo 'medias.csv'.")
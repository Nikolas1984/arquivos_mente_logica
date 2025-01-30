#Exceções (try catch)

#Try,except,else e finally

#try:
    #ccodigo que pode gerar uma excecao
#except TipoDeExcecao:
    #codigo a se executado se ocorrer uma excecao
#else:
    #codigo a ser executado caso ela nao ocorra
#finally:
    #Codigo que sempre sera executado
    
 #exemplo pratico
 
try:
    arquivo = open('dados.txt','r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não fo encontrado")
else:
    print("Arquivo lido com sucesso")
    print(conteudo)
finally:
    print("Operação de leitura finalizada")

try:
    numero = int(input("Digite um número inteiro:"))
    resultado = 100 / numero
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"O resultado é: {resultado}")
finally:
    print("Operação de divisão finalizada.")
    
try:
    arquivo = open('dados.txt','r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
else:
    print("Arquivo lido com sucesso!")
finally:
    if 'arquivo' in locals():
        arquivo.close()
        print("Aruqivo fechado.")

def calculadora():
    try:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        operacao = input("Digite a operação desejada entre  '+', '-', '*' ou '/' : ")
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            raise ValueError("Operador inválido")
        
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    else:
        print(f"O resultado é: {resultado}")
    
calculadora()

def ler_arquivo(nome_arquivo):
    try:
        with open (nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
    except PermissionError:
        print("Erro: Permissão negada para ler o arquivo.")
    except Exception as e:
        print("Ocorreu um erro inesperado: {e}")
#ler_arquivo(dados.txt)

def celcius_para_fahrenheit():
    try:
        celcius = float(input("Digite a temperatura em celsius: "))
        faherenheit = celcius * 9 / 5 + 32
    except ValueError:
        print("Erro: Por favor, insira um valor númerico.")
    else:
        print(f"A temperatura em fahrenheit é: {faherenheit:.2f} F")
    
celcius_para_fahrenheit()

class UsuarioNaoEncontradoError(Exception):
    pass

class SenhaIncorretaError(Exception):
    pass

usuarios = {
'admin': '1234',
'usuario1': 'senha1',
'usuario2': 'senha2'
}

def login():
    try:
        nome_usuario = input("Nome de usuário: ")
        senha = input("Senha: ")
        
        if nome_usuario not in usuarios:
            raise UsuarioNaoEncontradoError("Usuario não encontrado.")
        elif usuarios[nome_usuario] != senha:
            raise SenhaIncorretaError("Senha incorreta.")
    except UsuarioNaoEncontradoError as e:
        print(f"Erro: {e}")
    except SenhaIncorretaError as e:
        print(f"Erro {e}")
    else:
        print("Login realizado com sucesso.")
        
login()

lista = ['maçã', 'banana', 'laranja']

def acessar_elemento():
    try:
        indice = int(input("Digite um indice: "))
        elemento = lista[indice]
    except ValueError:
        print("Erro: Por favor, insira um número inteiro.")
    except IndexError:
        print("Erro: Indice fora do intervalo da lista.")
    else:
        print(f"O elemento no índice {indice} é {elemento}.")

acessar_elemento()
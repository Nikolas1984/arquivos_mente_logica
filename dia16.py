#padroes de projetos

#formas de programar que trazem beneficios para o projeto

#singleton
#garante que uma classe tenha apenas uma instancia

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Instancia Singleton criada com sucesso")
        return cls._instance
    

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)

#padrao factory
#define uma interface para criar objetos, mas permite que subclasses decidam qual objetos criar (superclasse)

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    
#fábrica de transportes, criar: carros,barcos e avioes
# a fabrica exige um metodo mover

class carro(Transporte):
    def mover(self):
        print("O carro está se movendo")
        
class barco(Transporte):
    def mover(self):
        print("O barco está se movendo")
        
class aviao(Transporte):
    def mover(self):
        print("O avião está se movendo")

class FabricaTrasporte:
    def criar_transporte(self,tipo):
        if tipo == "carro":
            return carro()
        elif tipo == "barco":
            return barco()
        elif tipo == "avião":
            return aviao()
        else:
            raise ValueError("Tipo de transporte desconhecido")
        

fabrica = FabricaTrasporte()

#criando o factory method
transporte1 = fabrica.criar_transporte("carro")
transporte2 = fabrica.criar_transporte("barco")
transporte3 = fabrica.criar_transporte("avião")

transporte1.mover()
transporte2.mover()
transporte3.mover()
    

#observer, define
# uma dependencia um-para-muitos entre objetos, quando um obj muda de estado, todos seus dependentes sao notificados e atualizados automaticamente

class Observador:
    def atualizar(self,mensagem):
        pass

class Aluno(Observador): #uma classe herda a outra no python quando ela recebe a mesma como parametro
    def __init__(self,nome):
        self.nome = nome
        
    def atualizar(self, mensagem):
        print(f"{self.nome} recebeu a mensagem: {mensagem}")

class Professor:
    def __init__(self):
        self.observadores = []
    
    def adicionar_observador(self,observador):
        self.observadores.append(observador)
    
    def remover_observador(self,observador):
        self.observadores.remove(observador)    
        
    def notificar_observadores(self,mensagem):
        for observador in self.observadores:
            observador.atualizar(mensagem)

#Testando o Observer
professor = Professor()
aluno01 = Aluno("Ana")
aluno02 = Aluno("Pedro")

professor.adicionar_observador(aluno01)
professor.adicionar_observador(aluno02)


professor.notificar_observadores("A aula será ás 14h.")

#boas praticas

#1 - nomes significativos, nas funçoes, variaveis e classes, para deixar o codigo mais compreensivel

#nao recomendado
def calc(a,b):
    return a + b

#recomendado
def calcular_soma(numero1, numero2):
    return numero1 + numero2

#2 Modularizaçao, dividr o codigo em modulos e funçoes menor, pois promove a reutilizaçao de codigo e facilita a manutencao
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()
    
def contar_palavras(texto):
    return len(texto.split())

#uso das funçoes
#conteudo = ler_arquivo('texto.txt')
#numero_palavras = contar_palavras(conteudo)
#print(f"O texto tem {numero_palavras} palavras.")


#3 comentarios e Documentaçao Adicione comentarios para explicar partes complexas do codigo e utilize docstrings para docuemntar funcoes e classes
def calcular_media(notas):
    """
    Calcula a media das notas fornecedias.
    
    Parametros:
    notas (list): Lista de numeros representando as notas.
    
    Retorna:
    float: media das notas
    
    """
    total = sum(notas)
    quantidade = len(notas)
    return total / (quantidade)

#4 Consistencia mantenha um estilo de codificacao consistente no projeto. Utilize ferramentas como o pep8 para python, que fornece diretrizes de estilo

#5 Evite codigo repetitivo, para evitar erros e facilitar correcoes futuras


#Exercicios
#1 implementar o padrao singleton na classe Database

class Database:
    _instance = None
        
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls.conexao = "Conexão com o banco de dados estabelecida"
        return cls._instance   
        
    def conectar(self):
        print(self.conexao)
        
db1 = Database()
db2 = Database()

db1.conectar()
db2.conectar()
print(db1 is db2)

#2 Implementar o padrao factory Method na criação de forma geometricas

#criando a classe principal
class FormasGeometricas(ABC):
    @abstractmethod
    def criar_forma(self):
        pass
 
 #criando as subclasses que vao utilizar o metodo   
class Circulo(FormasGeometricas):
    def criar_forma(self):
        print("A forma circulo foi criada")

class Quadrado(FormasGeometricas):
    def criar_forma(self):
        print("A forma Quadrado foi criado")
    
class Triangulo(FormasGeometricas):
    def criar_forma(self):
        print("A forma Triangulo foi criado")
    
#criando o metodo factory
class FabricarFormaGeometrica:
    def criar_forma_geometrica(self,forma):
        if(forma == "circulo"):
            return Circulo()
        elif(forma == "quadrado"):
            return Quadrado()
        elif(forma == "triangulo"):
            return Triangulo()

#iniciando em uma  variavel a factory
fabrica_forma = FabricarFormaGeometrica()

#instanciando os objetos        
circulo01 = fabrica_forma.criar_forma_geometrica("circulo")
quadrado01 = fabrica_forma.criar_forma_geometrica("quadrado")
triangulo01 = fabrica_forma.criar_forma_geometrica("triangulo")

#utilizando o metodo criar forma da classe principal
circulo01.criar_forma()
quadrado01.criar_forma()
triangulo01.criar_forma()   

#3 implementar o metodo observador na classe notificador
#inicializando o observador
class Observador02(ABC):
    def atualizar(self):
        pass
    
class Notificador:
    def __init__(self):
        self.observadores = [] #recebe uma lista de objetos observadores
        
    def adicionar_observador(self,observador): #adiciona um observador no fim da lista
        self.observadores.append(observador)
    
    def remover_observador(self,observador): #remove um observador
        self.observadores.remove(observador)
        
    def notificar(self,mensagem): #notifica o observador
        for observador in self.observadores:
            observador.atualizar(mensagem)    
            
            
class Usuario(Observador): #inicializa o observador
    def __init__(self,nome):
        self.nome = nome

    def atualizar(self,mensagem):
        print(f"{self.nome} recebeu a mensagem: {mensagem}")
            
notificador = Notificador()
usuario01 = Usuario("Naruto")
usuario02 = Usuario("Kira")

notificador.adicionar_observador(usuario01)
notificador.adicionar_observador(usuario02)

notificador.notificar("Nova atualização disopnivel")
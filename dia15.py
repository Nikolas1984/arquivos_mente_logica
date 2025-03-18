#Orientaçao a objetos

class pessoa:
    
    def __init__(self,nome,idade):
        #inicializando o objeto
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Ola meu nome é {self.nome} e eu tenho {self.idade} anos")
        
    def aniversario(self):
        self.idade += 1
        print(f"Parabains, voce fez {self.idade} anos!")
            
#criar classe retangulo, que aceita as propriedades largura e altura, no qual possui o metodo que calcula a area
class retangulo:
    
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
        
    def area (self):
        area = self.altura * self.largura
        print(f"A area do retangulo é: {area}")

#classe aluno que adicionar uma nota e calcula a media
class Aluno:
    def __init__(self,nome,notas):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota(self,nota):
        self.notas.append(nota)
    
    def calcular_notas(self):
        if self.notas:
            return sum(self.notas)/ len(self.notas)

pessoa1 = pessoa("Severino", 22)

pessoa1.apresentacao()
pessoa1.aniversario()

retangulo01 = retangulo(2,3)

retangulo01.area()

aluno01 = Aluno("Severino", [10,10,10])

nota = int(input(f"Digite a nota a ser inserida no aluno {aluno01.nome}: "))
aluno01.adicionar_nota(nota)
aluno01.adicionar_nota(10)
aluno01.adicionar_nota(8)

media = aluno01.calcular_notas()
print(f"A média do aluno {aluno01.nome} é {media:.2f}")


class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def exibir_informacoes(self):
        print(f"Titulo: {self.titulo}")    
        print(f"Autor: {self.autor}")  
        print(f"Ano de publicação: {self.ano}" ) 
        
livro01 = Livro("Hora do medo", "Simas Turbo", 1984)
livro01.exibir_informacoes()   

class Cachorro:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        
    def latir(self):
        print(f"AU! AU! O {self.nome} está latindo")    

    def aniversario(self):
        self.idade += 1
        print(f"Feliz Auniversario {self.nome}, parabains pelos {self.idade} anos")
        
cachorro01 = Cachorro("Spike", 4)
    
cachorro01.latir()
cachorro01.aniversario()

#como essa classe nao possui atributos, nao precisamos iniciala
class calculadora:
    def soma(self,a,b):
        return a + b
    
    def sub(self,a,b):
        return a - b
    
    def multi(self,a,b):
        return a * b
    
    def div(self,a,b):
        if a != 0 and b !=0:
            return a / b
        else:
            print("Erro! Divisão por zero.")
            return None
calculadora01 = calculadora()
print(calculadora01.soma(1,2))
print(calculadora01.sub(1,2))
print(calculadora01.div(0,0))
print(calculadora01.multi(1,3))

    
#Variaveis

Nome = "Nikolas"
Idade = 23
Altura = 1,70
Estudante = False

print("Ola meu nome é", Nome, ", Eu tenho", Idade, "Anos", "Tenho", Altura, "de Altura") 

#Tipos de dados
#int, float, string, boolean

#Verificar o tipo do dado (casting)
print(type(Nome))

#Operador
print(5 + 1.2)
print(10-8)
print(10/2)
print(5*5)

#calculo simples
data_nascimento = 2024 - Idade

print("Nasci em", data_nascimento)


#Comparações
#data_nascimento = int (input("Digite sua idade"))

#maior_de_idade = data_nascimento >= 18


#print(maior_de_idade)

#Calculadora
primeiro_numero = int(input("Insira o primeiro numero: "))
segundo_numero = int(input("Insira o segundo numero: "))

print("Soma = ", primeiro_numero + segundo_numero)
print("Subtração = ", primeiro_numero - segundo_numero)
print("Divisão = ", primeiro_numero / segundo_numero )
print("Multiplicação = ", primeiro_numero * segundo_numero )  


#Conversor de Temperaturas
Celsius = float(input("Insira a temperatura em celsius: "))

Fahrenheit= Celsius * 9/5 + 32
print("Temperatura = ", Fahrenheit)


#Area de um circulo
pi = 3.14159
raio = float(input("Insira o raio do circulo"))
area = pi * raio **2
print("Area do circulo = ", area)
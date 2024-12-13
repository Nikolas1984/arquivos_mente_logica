#valor dos itens
pao = 3.50
leite = 4.20
cafe = 2.80

#Calculo da compra
total = pao + leite + cafe 
troco = 20 - total

#imprimindo valores gerados
print("Total: ", total)
print("Troco: ", troco)

#dados estudante
frequencia = 80
nota_media = 8.5

aprovado = (frequencia >= 75.0) and (nota_media >= 7)

print("Aprovado: ", aprovado)

#oferta

quantidade_de_itens = 8
valor_de_itens = 120

desconto = (quantidade_de_itens > 10)  or (valor_de_itens > 100)

print("Possui desconto? ", desconto)


#Senha de acesso

senha_inserida = "123456abc"
senha_correta = "123456abc"
usario_bloqueado = False

senha = (senha_inserida == senha_correta) and not usario_bloqueado

print("Usuario possui acesso? ", senha)


#divisáo exata

quantidade_de_amigos = 3
valor_da_conta = 150

total_cada = valor_da_conta / quantidade_de_amigos
divisao_exata = (valor_da_conta % quantidade_de_amigos) == 0

print("total de cada um: ", total_cada)
print("Divisáo exata", divisao_exata)


#Idade da pessoa

idade = int(input("Digite a sua idade"))

validar_idade = idade >= 16

print("Maior de idade:", validar_idade)

#Calcular IMC
peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc =float(peso/(altura ** 2)) 

peso_ideal = imc >=18.5 and imc <= 24.9

print("Imc: ",imc)
print("Peso Ideal?: ",peso_ideal)

#Numero par

numero_par = int(input("Digite o numero: "))
par = numero_par % 2 == 0

print("Numero par ?", par)
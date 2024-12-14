#condiçoes

idade = 17

if(idade >= 18):
    print("Maior de idade")
else:
    print("Menor de idade")
    
nota = 85

if(nota >= 90):
    print("Sua nota é A")
elif(nota >= 80):
    print("Sua nota é B")
elif(nota >=70):
    print("Sua nota é C")
else:
    print("Voce está abaixo da media")
    

#Calculo de desconto

Valor_compra = 750

if(Valor_compra >= 1000):
    desconto = Valor_compra * 0.10
    print("Desconto de 10%, valor do desconto: ",desconto)
elif(Valor_compra >= 500 and Valor_compra <= 999):
    desconto = Valor_compra * 0.05
    print("Desconto de 5%, valor do desconto: ",desconto)

else:
    print("Sem desconto")
    
    
#dia da semana

dia_da_semana = "sabado"
chovendo = False

if(dia_da_semana == "sabado" or dia_da_semana == "domingo" and not chovendo):
    print("Va para o parque")
else:
    print("Fique em casa")

#Negativo, positvo ou zero

numero_digitado = int(input("Digite o numero desejado: "))

if(numero_digitado > 0):
    print("O numero", numero_digitado, "é positivo")
elif(numero_digitado < 0):
     print("O numero", numero_digitado, "é negativo")
else:
    print("O numero digitado é zero")
    
#Calculadora simples

primeiro_numero = int(input("Digite o primeiro numero "))
segundo_numero = int(input("Digite o segundo numero "))
operacao = str(input("Digite a operação desejada (+,-,/,*) "))

if(operacao == "+"):
    resultado = primeiro_numero + segundo_numero
    print("Resultado =",resultado)
elif(operacao == "-"):
    resultado = primeiro_numero - segundo_numero
    print("Resultado =",resultado)
elif(operacao == "/"):
    if(segundo_numero !=0):
        resultado = primeiro_numero / segundo_numero
        print("Resultado =",resultado)
    else:
        print("Divisão por 0 é inválida")
        
elif(operacao == "*"):
    resultado = primeiro_numero * segundo_numero
    print("Resultado =",resultado)
else:
    print("Operação invalida")

#classificação de idade

idade = int(input("Digite sua idade: "))

if(idade >= 0 and idade	<= 12):
    print("Voce é criança")
elif(idade >= 13 and idade <= 17):
    print("Voce é adolescente")
elif(idade >= 18 and idade <= 59):
    print("Voce é um adulto")
elif(idade >= 60):
    print("Voce é idoso")


#Verificando ano bissexto
ano = int(input("Digite o ano: "))

if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "É um ano bissexto")
else:
    print(ano, "Não é um ano bissexto")


#Caixa eletronico

valor_saque = int(input("Digite o valor do saque: R$ "))

if(valor_saque <= 0):
    print("Valor inválido")
else:
    cedulas_100 = valor_saque // 100
    valor_saque %= 100
    cedulas_50 = valor_saque // 50
    valor_saque %= 50
    cedulas_20 = valor_saque // 20
    valor_saque %= 20
    cedulas_10 = valor_saque // 10
    valor_saque %= 10
    cedulas_5 = valor_saque // 5
    valor_saque %= 5
    cedulas_2 = valor_saque // 2
    valor_saque %= 2
if valor_saque != 0:
    print("Não é possível sacar o valor especificado com as cédulas disponíveis.")
else:
    print("Cédulas entregues:")
if cedulas_100 > 0:
    print(f"{cedulas_100} x R$100")
if cedulas_50 > 0:
    print(f"{cedulas_50} x R$50")
if cedulas_20 > 0:
    print(f"{cedulas_20} x R$20")
if cedulas_10 > 0:
    print(f"{cedulas_10} x R$10")
if cedulas_5 > 0:
    print(f"{cedulas_5} x R$5")
if cedulas_2 > 0:
    print(f"{cedulas_2} x R$2")
    
#Emprestimo bancario

valor_emprestimo = float(input("Digite o valor do emprestimo "))
renda_mensal = float(input("Digite o valor da renda mensal "))
qtnd_parcelas = int(input("Digite a quantidade de parcelas "))

valor_parcela = valor_emprestimo/qtnd_parcelas
limite_emprestimo = (renda_mensal * 0.30)

if(valor_emprestimo <=  limite_emprestimo):
    print("Emprestimo aprovado")
    print(f"Valor parcela: R${valor_parcela:.2f}")
else:
    print("Emprestimo negado")
    print(f"Valor parcela: R${valor_parcela:.2f} excede 30 % da renda mensal")


import random

opções = ["pedra","papel","tesoura"]

escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opções)

print(f"Voce escolheu: {escolha_jogador}",)
print(f"O computador escolheu: {computador}")

if(computador == escolha_jogador):
    print("Empate!")
elif(escolha_jogador == "papel" and computador == "pedra") or (escolha_jogador == "pedra" and computador == "tesoura") or (escolha_jogador == "tesoura" and computador == "papel"):
    print("Voce ganhou :)")
elif escolha_jogador in opções:
    print("Voce perdeu :(")
else:
    print("Escolha inválida")
    

distancia = int(input("Digite a distancia da corrida em km: "))

tarifa_basica = 4.00
tarifa_por_km = distancia * 0.25
valor_total = tarifa_basica + tarifa_por_km

print(f"Valor total da corrida: {valor_total:.2f}",)


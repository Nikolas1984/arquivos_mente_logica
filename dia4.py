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


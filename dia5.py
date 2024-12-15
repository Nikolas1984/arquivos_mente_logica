#Laços de repetição

#loop for

#for variavel in sequencia

frutas = ["maça","banana","pera"]

for fruta in frutas:
    print("A fruta é uma ",fruta)

for numero in range(5):
    print("numero",numero)
    
#loop while executa enquanto a condição for verdadeira

i = 0

while(i <= 5):
    print(i)
    i = i + 1

#break
for numero in range(10):
    if numero == 5:
        break
    print("numero",numero)   
    

#continue
for numero in range(5):
    if numero == 2:
        continue
    print("numero",numero)
    
for numero in range(1,11):
    print(numero)
 
 #Soma dos numeros   
numero_digitado = int(input("Digite o numero a ser somado"))
soma = 0

for i in range(1,numero_digitado+1):
    soma+= i   
print("A soma dos numeros de 1 a",numero_digitado, "é", soma)

#Numero digitado
numero_digitado = int(input("Digite o numero que deseja saber a tabuada"))
i = 0

for i in range(1,11):
    print(i, "*",numero_digitado,"=",i*numero_digitado)
    
numero_par = 0
numero_impar = 0  
for i in range(1,21):
    if(i % 2 == 0):
        numero_par += 1
    else:
        numero_impar += 1

print("Entre 1 e 20 existem",numero_par,"pares e", numero_impar, "impares")


#numero aleatorio

#import random
#numero_computador = int(random.randint(1,100))
#tentativas = 0
#while True:
 #   numero_digitado = int(input("Adivinhe o numero entre 1 e 100: "))
 #   tentativas += 1
  #  if(numero_computador == numero_digitado):
   #     print("Voce acertou o numero em ", tentativas, "Tentativas")
    #    break
    #elif numero_computador > numero_digitado:
     #   print("O numero é maior que", numero_digitado)
    #elif numero_computador < numero_digitado:
     #   print("O numero é menor que", numero_digitado)

#Fatorial

n = int(input("Digite o fatorial do numero inteiro positivo: " ))
fatorial = 1

for i in range(1,n+1): 
    fatorial = i * fatorial
    print(fatorial)
 
if(n == 0 or n == 1):
    print("Fatorial de",n,"é: 1")
     
else:     
    print("Fatorial de",n,"é:",fatorial)
    
#Fibonnaci

n = int(input("Digite quantos elementos da sequencia de fibbonaci quer ver: "))
termo_zero = 0
termo_um = 1
contador = 0

if(n <= 0):
    print("Por favor insira um numero positivo")

elif n == 1:
    print(termo_um)
while(contador < n):
    print(termo_um)
    proximo_termo = termo_zero + termo_um
    termo_zero = termo_um
    termo_um = proximo_termo
    contador += 1
    
#Jogo da forca
palavra_secreta = "python"
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 6

while(tentativas > 0 and "_" in letras_descobertas):
    print("Palavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()
    
    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_descobertas[idx] = letra
                print("Voce acertou uma letra.")
    else:
        tentativas -= 1
        print(f"Voce errou. Voce possui {tentativas} tentativas restantes") 
        
if "_" not in letras_descobertas:
    print("Parabens! Voce adivinhou a palavra", palavra_secreta)
else:  
    print("Voce perdeu! A palavra era: ",palavra_secreta)
import random

numero_computador = int(random.randint(1,100))
tentativas_maximas = 14
tentativas = 0
pontuacao = 0
historico_pontuacoes = []


print("Bem vindo ao jogo da adivinhação! Escolha a dificuldade desejada.")
print("1 - Facil = 14 tentativas")
print("2 - Normal = 7  tentativas")
print("3 - Dificil = 5 tentativas")

#loop para escolher a dificuldade

while True:
    dificuldade = input("Digite a dificuldade solicitada: ")
    
    if(dificuldade == "1"):
        tentativas_maximas = 14
        break
    elif(dificuldade == "2"):
        tentativas_maximas = 7
        break
    elif(dificuldade == "3"):
        tentativas_maximas = 5
        break
    else:
        print("Opção inválida, por favor digite 1, 2 ou 3")



#loop para executar o jogo
while True:
    if(tentativas_maximas > 0):
        numero_jogador = input("Digite um número entre 1 e 100: ")
        
        if not numero_jogador.isdigit():
            print("Digite um numero valido")
            continue
        
        numero_jogador = int(numero_jogador)
        
        if numero_jogador < 1 or numero_jogador > 100:
            print("Por favor, digite um numero entre 1 e 100")
            continue
            
        tentativas += 1
        tentativas_maximas -= 1
        
        #Caso o jogador acerte o numero, calcula e armazena a pontuação
        if(numero_jogador == numero_computador):
            print(f"Parabens, voce acertou o numero em {tentativas} tentativa(s)")
            pontuacao = tentativas_maximas * 10 * (int(dificuldade))
            print("Pontuação: ", pontuacao)
            historico_pontuacoes.append(pontuacao)
            tentativas_maximas = 0
            pontuacao = 0
        elif numero_computador < numero_jogador :
            print("Voce errou, o numero é menor que ", numero_jogador)
            print("Tentativas restantes: ", tentativas_maximas)
        elif numero_computador > numero_jogador :
            print("Voce errou, o numero é maior que ", numero_jogador)
            print("Tentativas restantes: ", tentativas_maximas)
    
    else:
        print("Fim de jogo!")
        
        
        for idx, pontos in enumerate(historico_pontuacoes, start=1):
            print(f"Partida {idx}: {pontos} pontos")

        tentar_novamente = input("Gostaria de tentar novamente? Digite 'S' ou 'N': ")
        if(tentar_novamente == "S"):
            if(dificuldade == "1"):
                tentativas_maximas = 14
            elif(dificuldade == "2"):
                tentativas_maximas = 7
            elif(dificuldade == "3"):
                tentativas_maximas = 5
            tentativas = 0
            pontuacao = 0
            numero_computador = int(random.randint(1,100))
            continue
        elif(tentar_novamente == "N"):
            print("Fim de jogo")
            break
        else:
            print("Opção inválida")
    
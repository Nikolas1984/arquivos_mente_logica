#gerenciador de tarefas

import csv
import os
import json
from datetime import datetime

#funcao para carregar as tarefas
def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json','r') as arquivo:
            try:
                tarefas = json.load(arquivo)
                if isinstance(tarefas,list):
                    return tarefas
                else:
                    return []
            except json.JSONDecodeError:
                return []
    return []
    
#lista todas as tarefas
def listar_tarefas(tarefas):
    print("\nTarefas Pendentes:")
    tarefas_pendentes = [t for t in tarefas if not t['concluida']]
    tarefas_pendentes = sorted(tarefas_pendentes, key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'))
    for tarefa in tarefas_pendentes:
        data_obj = datetime.strptime(tarefa['data'], '%d/%m/%Y')
        status_atrasado = " [Atrasada]" if data_obj.date() < datetime.now().date() else "" #verifca se a tarefa esta atrasada
        print(f"Id {tarefa['id']}, Titulo: {tarefa['titulo']}, Data: {tarefa['data']}{status_atrasado}")
    
    print("\n Tarefas Concluídas: ")
    tarefas_concluidas = [t for t in tarefas if t['concluida']] 
    tarefas_concluidas = sorted(tarefas_concluidas, key =lambda x: datetime.strptime(x['data'], '%d/%m/%Y')) #ordenando a lista de tarefas pela data, lambda significa funcao rapida
    for tarefa in tarefas_concluidas:
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}, Data: {tarefa['data']}") 
    
    #listar tarefas antigo
    #print("Tarefas:")
    #for tarefa in tarefas:
        #status = "Concluida" if tarefa['concluida'] else "Pendente"
        #print(f"ID:{tarefa['id']} , Titulo: {tarefa['titulo']}, Status: {status}, Data de conclusão: {tarefa['data']}")

#pesquisar tarefas por termo
def pesquisar_tarefas(tarefas):
    termo = input("Digite o termo de pesquisa: ").lower()
    resultados = [t for t in tarefas if termo in t['titulo'].lower() or termo in t['descricao'].lower()]
    if resultados:
        print(f"\nTarefas que contem '{termo}':")
        for tarefa in resultados:
            status = "Concluida" if tarefa['concluida'] else "Pendente"
            print(f"ID: {tarefa['id']}, Titulo {tarefa['titulo']}, Status: {status}, Data: {tarefa['data']}")
    else:
        print("Nenhuma tarefa encontrada com o termo especificado.")
        
#Ordenar tarefas
def ordenar_tarefas(tarefas):
    tarefas.sort(key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'))
    salvar_tarefas(tarefas)
    print("tarefas ordenadas por data de conclusão com sucesso!")

#escreve e salva tarefas no arquivo
def salvar_tarefas(tarefas):
  with open('tarefas.json', 'w' ) as arquivo:
    json.dump(tarefas, arquivo, indent=4)
 
 #gerar o id unico da tarefa   
def gerar_id(tarefas):
    if tarefas:
        ultimo_id = tarefas[-1]['id']
        return ultimo_id + 1
    else:
        return 1
    
#adicionar tarefas
def adicionar_tarefas(tarefas):
    print("Adicionar nova tarefa") 
    titulo = input("Titulo: ") 
    descricao = input("Descrição: ")
    data = input("Data de conclusão (dd/mm/aaaa): ")
    try:
        data_obj = datetime.strptime(data, '%d/%m/%Y')
        data = data_obj.strftime('%d/%m/%Y')
        if data_obj.date() < datetime.now().date():
            print("Data de conclusão não pode ser no passado.")
            return
    except ValueError:
        print("Data em formato inválido. Utilize dd/mm/aaaa.")
        return   
    id = gerar_id(tarefas)
    tarefa = {
        'id' : id,
        'titulo': titulo,
        'descricao' : descricao,
        'concluida': False,
        'data': data
        }
    
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")
 
 #concluir tarefa
def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa para concluir: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['concluida']:
                    print("A tarefa já está concluida")
                else:
                    tarefa['concluida'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluida com sucesso")
                return 
        print("Tarefa não encontrada")
    except ValueError:
        print("Id invàlido.")
 
 #excluir tarefa
def excluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser excluida: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                tarefas.remove(tarefa)
                salvar_tarefas(tarefas)
                print("Tarefa excluida com sucesso")
                return
        print("Tarefa não encontrada")       
    except ValueError:
        print("Id invàlido.")
 
  #editar tarefa
def editar_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o id da tarefa a ser editada: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                titulo = input("Digite o novo titulo da tarefa: ")
                descricao = input("Digite a nova descricao da tarefa: ")
                data_conclusao = input("Digite a nova data de conclusão no formato dd/mm/aaaa: ")
                try:
                    data_obj = datetime.strptime(data_conclusao, '%d/%m/%Y')
                    if data_obj.date() < datetime.now().date():
                        print("Data de conclusão não pode ser no passado")
                        return
                    tarefa['data'] = data_obj.strftime('%d/%m/%Y')
                except ValueError:
                    print("Data em formato inválido. Utilize dd/mm/aaaa.")
                    return
                
                tarefa['titulo'] = titulo
                tarefa['descricao'] = descricao
                salvar_tarefas(tarefas)
                print("Tarefa editada com sucesso")
                return
        print("Tarefa não encontrada")    
    except ValueError:
        print("Id inválido")

#exportar tarefa em csv
def exportar_tarefas(tarefas):
    try:
        with open('tarefas_exportadas.csv', 'w', newline='') as arquivo_csv:
            campos = ['ID', 'Titulo', 'Descricao', 'Data de Conclusao', 'Concluida']
            escritor = csv.DictWriter(arquivo_csv,fieldnames=campos)
            escritor.writeheader()
            for tarefa in tarefas:
                escritor.writerow({'ID': tarefa['id'], 'Titulo': tarefa['titulo'], 'Descricao': tarefa['descricao'], 'Data de Conclusao': tarefa['data'], 'Concluida': 'Sim' if tarefa['concluida'] else 'Não'})
        print("Tarefas exportadas com sucesso para 'Tarefas_exportadas.csv'.")
    except Exception as e:
        print(f"Ocorreu um erro ao exportar as tarefas: {e}")
 
 #importar tarefas de um csv
def importar_tarefas(tarefas):
    nome_arquivo = input("Digite o nome do arquivo CSV para importar: ")
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                try:
                    tarefa ={
                        'id':gerar_id(tarefas),
                        'titulo': linha['Titulo'],
                        'descricao': linha['Descricao'],
                        'data': linha['Data de Conclusao'],
                        'concluida': True if linha['Concluida'].lower == 'sim' else False
                        }
                    tarefas.append(tarefa)
                except KeyError:
                    print("Formato de arquivo inválido. Certifique-se de que o CSV contém as colunas corretas.")
                    return
        salvar_tarefas(tarefas)
        print(f"Tarefas importadas com sucesso do arquivo '{nome_arquivo}'")    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao importar as tarefas: {e}")
 
    
#menu principal
def menu ():
    print("=== Gerenciador de tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Excluir Tarefa")
    print("5. Editar tarefa")
    print("6. Pesquisar Tarefa")    
    print("7. Ordenar Tarefas por data")
    print("8. Exportar Tarefas para CSV")
    print("9. Importar Tarefas de um10 CSV")
    print("10. Sair do programa")
    return input("Escolha uma opção: ")
    
 #main loop das ações 
def main():
    tarefas = carregar_tarefas()  
    while True :
        opcao = menu()
        
        if opcao == '1' : adicionar_tarefas(tarefas)   
        elif opcao == '2': listar_tarefas(tarefas)
        elif opcao == '3': concluir_tarefa(tarefas)
        elif opcao == '4': excluir_tarefa(tarefas)
        elif opcao == '5': editar_tarefa(tarefas)
        elif opcao == '6': pesquisar_tarefas(tarefas)
        elif opcao == '7': ordenar_tarefas(tarefas)
        elif opcao == '8': exportar_tarefas(tarefas)
        elif opcao == '9': importar_tarefas(tarefas)
        elif opcao == '10':
            print("Obrigado")
            break
        else:
            print("Opção inválida!")
            
if __name__ == '__main__':
    main()
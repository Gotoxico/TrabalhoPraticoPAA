import os
from Menus import *
from Grafico import *

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    tipo = 0
    cont = 0
    tipoVetorDicionario = {
        1 : 'Aleatório',
        2 : 'Crescente',
        3 : 'Decrescente'
    }
   

    while True:
        #Menu de inicialização
        opcaoInit = menuDeInicializacao()
        os.system('cls' if os.name == 'nt' else 'clear')

        if opcaoInit == '3':
            exit()
        
        if opcaoInit == '1':
            arquivos = []
            nomes = []
            while True:    
                opcao, tipo = menuDeExecucao()
                if opcao == '10':
                    break
                cont += 1
                nomeAlgoritmo, nomeArquivo = menu(opcao, tipo)
                arquivos.append(nomeArquivo)
                nomes.append(nomeAlgoritmo)
            
            if cont > 0:
                plotarGrafico(arquivos, nomes)
                cont = 0
            #limpar terminal
            os.system('cls' if os.name == 'nt' else 'clear')

        elif opcaoInit == '2':
            nomes = []
            arquivos = []
            while True:

                opcao, tipo = menuDeExecucao()
                if opcao == '10':
                    break
                cont += 1
                if opcao == '0':
                    nomeAlgoritmo = 'TimSort (Python)'
                elif opcao == '1':
                    nomeAlgoritmo = 'Bubble Sort sem melhorias'
                elif opcao == '2':
                    nomeAlgoritmo = 'Bubble Sort com melhorias'
                elif opcao == '3':
                    nomeAlgoritmo = 'Quick Sort com pivô elemento inicial'
                elif opcao == '4':
                    nomeAlgoritmo = 'Quick Sort com pivô elemento central'
                elif opcao == '5':
                    nomeAlgoritmo = 'Insertion Sort'
                elif opcao == '6':
                    nomeAlgoritmo = 'Shell Sort'
                    print("\n\n====================================")
                    print("|1 - Teorema 1 baseado em 2^k - 1   |")
                    print("|2 - Teorema 2 baseado em 2^p * 3^q |")
                    print("=====================================")
                    teorema = input("Digite qual teorema será utilizado: ")
                    nomeAlgoritmo += ' Teorema {}'.format(teorema)
                elif opcao == '7':
                    nomeAlgoritmo = 'Selection Sort'
                elif opcao == '8':
                    nomeAlgoritmo = 'Heap Sort'
                elif opcao == '9':
                    nomeAlgoritmo = 'Merge Sort'
                
                nomeArquivo = 'CSVs\\{}\\{}\\Resultado{}{}.csv'.format(
                    remover_acentos(nomeAlgoritmo.strip().title().replace(" ", "")),
                    remover_acentos(tipoVetorDicionario[int(tipo)]),
                    tipoVetorDicionario[int(tipo)],
                    nomeAlgoritmo
                    
            )   
                 
                arquivos.append(nomeArquivo)
                nomes.append(nomeAlgoritmo + " " + tipoVetorDicionario[int(tipo)])
                print('\n\n',arquivos, end='\n\n')


            if cont > 0:
                for(arquivo, nome) in zip(arquivos, nomes):
                    print(arquivo, nome, end='\n\n')

                plotarGrafico(arquivos, nomes)
                cont = 0
            #limpar terminal
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            continue

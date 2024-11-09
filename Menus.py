from timeit import default_timer
from Algoritmos import *
from Arrays import *
from Util import *
import pandas

# Menu de inicialização
def menuDeInicializacao():
    print("=====================================================================================================")
    print("|                                       INICIO DA EXECUCAO                                          |")
    print("=====================================================================================================")
    print("|Escolha qual operação deseja realizar:                                                             |")
    print("|1 - Executar algoritmos e plotar gráfico a partir dos resultados da execução;                      |")
    print("|2 - Plotar gráfico a partir de arquivos CSVs já prontos;                                           |")
    print("|3 - Sair                                                                                           |")
    print("=====================================================================================================")
    opcao = input("Escolha: ")
    return opcao


#Menu de execução
def menuDeExecucao():
    print("\n\n=====================================================================================================")
    print("|0 - Tim (Python)                                                                                   |")
    print("|1 - Bubble Sort sem melhorias                                                                      |")
    print("|2 - Bubble Sort com melhorias                                                                      |")
    print("|3 - Quick Sort com pivô elemento inicial                                                           |")
    print("|4 - Quick Sort com pivô elemento central                                                           |")
    print("|5 - Insertion Sort                                                                                 |")
    print("|6 - Shell Sort                                                                                     |")
    print("|7 - Selection Sort                                                                                 |")
    print("|8 - Heap Sort                                                                                      |")
    print("|9 - Merge Sort                                                                                     |")
    print("|10 - Sair                                                                                          |")
    print("=====================================================================================================")
    opcao = input("Escolha qual algoritmo será utilizado: ")
    if opcao == '10':
        return '10', 0
    
    print("\n\n==================================================")
    print("|1 - Aleatório                                   |")  
    print("|2 - Crescente                                   |")
    print("|3 - Decrescente                                 |")
    print("==================================================")
    
    tipo = int(input("Escolha o tipo de array: "))
    return opcao, tipo




#Escrever no CSV o tempo de execução de cada algoritmo, o tamanho da array e a organização dos valores
def menu(opcao, tipo):
    print(type(opcao))
    nomeAlgoritmo = ''
    tempoExecucao = []
    i = 1
    tipoVetorDicionario = {
        1 : 'Aleatório',
        2 : 'Crescente',
        3 : 'Decrescente'
    }
    tamanhoVetor = []
    tamanhoArray = 0
    while True:
        tamanhoArray += i * 1000

        array = criarArray(tipo, tamanhoArray)
        arrayOrdenadoMerge = []
    
        if opcao == '0':
            nomeAlgoritmo = "TimSort (Python)"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            array.sort()
            
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')
        elif opcao == '1':
            #Adicionado as listas os parâmetros de execução
            nomeAlgoritmo = "Bubble Sort sem melhorias"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            bubbleSort(array)
            
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')
            
        elif opcao == '2':
            nomeAlgoritmo = "Bubble Sort com melhorias"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            bubbleSortMelhoria(array)
        
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')

        elif opcao == '3':
            nomeAlgoritmo = "Quick Sort com pivô elemento inicial"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            quickSortPivoInicioStack(array)
    
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')

        elif opcao == '4':
            nomeAlgoritmo = "Quick Sort com pivô elemento central"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            quickSortPivoCentralStack(array)
        
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')
        elif opcao == '5':

            nomeAlgoritmo = "Insertion Sort"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            insertionSort(array)
        
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')

        elif opcao == '6':
            
            tamanhoVetor.append(len(array))

            increments = []
            if i == 1:
                print("\n\n============================================================================")
                print("|1 - Teorema 1 baseado em 2^k - 1                                           |")
                print("|2 - Teorema 2 baseado em 2^p * 3^q                                         |")
                print("=============================================================================")
                teorema = int(input('Digite qual teorema será utilizado: '))
                nomeAlgoritmo = "Shell Sort Teorema {}".format(teorema)
 
            if teorema == 1:
                increments = gerar_array_teorema1_formacao(8)
            elif teorema == 2:
                increments = gerar_array_teorema2_formacao(20)
            
           

            inicio = default_timer()
            #Insira Shell Sort
            shellSort(array, len(array), increments, len(increments))
        
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')

        elif opcao == '7':
            nomeAlgoritmo = "Selection Sort"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            #Insira Selection Sort
            SelectionSort(array)
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')

        elif opcao == '8':
            nomeAlgoritmo = "Heap Sort"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            #Insira Heap Sort
            heap_sort(array)
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')

        elif opcao == '9':
            nomeAlgoritmo = "Merge Sort"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            mergeSort(array, 0, len(array) - 1)
    
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio, end='')

        if i == 10:
            #printar nomeAlgoritmo com o atributo tittle e sem espaços
            print("\n=========")
            print("|Saindo |")
            print("=========")
            dicionario = {'Algoritmo': nomeAlgoritmo, 'tempoExecucao': tempoExecucao, 'Tamanho Vetor': tamanhoVetor}
            df = pandas.DataFrame(dicionario)

            nomeArquivo = 'CSVs\\{}\\{}\\Resultado{}{}1.csv'.format(
                    remover_acentos(nomeAlgoritmo.strip().title().replace(" ", "")),
                    remover_acentos(tipoVetorDicionario[int(tipo)]),
                    remover_acentos(tipoVetorDicionario[int(tipo)]),
                    nomeAlgoritmo
                    
            )
            df.to_csv(nomeArquivo)
            return nomeAlgoritmo + " " + tipoVetorDicionario[int(tipo)], nomeArquivo.strip()    
        print(' ({})'.format(i))
        i += 1
       




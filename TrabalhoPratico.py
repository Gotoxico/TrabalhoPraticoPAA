from numpy import random
from timeit import default_timer
import pandas
import matplotlib.pyplot as plt

#Tradução código do geeksforgeeks "https://www.geeksforgeeks.org/bubble-sort-algorithm/"
def bubbleSort(array):
    tamanho = len(array)

    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

#Tradução código do geeksforgeeks "https://www.geeksforgeeks.org/bubble-sort-algorithm/"
def bubbleSortMelhoria(array):
    tamanho = len(array)

    for i in range(tamanho):
        alterou = False
        for j in range(0, tamanho - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                alterou = True
        if(alterou == False):
            break

#Transcrição código slides
def particaoPivoInicio(array, limiteInferior, limiteSuperior):
    pivo = array[limiteInferior]
    baixo = limiteInferior
    alto = limiteSuperior

    while baixo < alto:
        while baixo < limiteSuperior and array[baixo] <= pivo:
            baixo += 1
        while limiteInferior < alto and array[alto] > pivo:
            alto -= 1
        if baixo <= alto:
            array[baixo], array[alto] = array[alto], array[baixo]

    array[limiteInferior], array[alto] = array[alto], array[limiteInferior]
    return alto   

#Transcrição código slides
def quickSortPivoInicio(array, limiteInferior, limiteSuperior):
    if limiteInferior < limiteSuperior:
        q = particaoPivoInicio(array, limiteInferior, limiteSuperior)
        quickSortPivoInicio(array, limiteInferior, q - 1)
        quickSortPivoInicio(array, q + 1, limiteSuperior) 

#Pequenas modificações ao código dos slides
def particaoPivoCentral(array, limiteInferior, limiteSuperior):
    pivo = array[(limiteInferior + limiteSuperior)//2]
    baixo = limiteInferior
    alto = limiteSuperior

    while baixo <= alto:
        while array[baixo] <= pivo:
            baixo += 1
        while array[alto] > pivo:
            alto -= 1
        if baixo <= alto:
            array[baixo], array[alto] = array[alto], array[baixo]
            baixo += 1
            alto -= 1
    
    return baixo

#Pequenas modificações ao código dos slides
def quickSortPivoCentral(array, limiteInferior, limiteSuperior):
    if limiteInferior < limiteSuperior:
        q = particaoPivoCentral(array, limiteInferior, limiteSuperior)
        quickSortPivoCentral(array, limiteInferior, q - 1)
        quickSortPivoCentral(array, q, limiteSuperior)

#Transcrição código slides
def insertionSort(array):
    for k in range(1, len(array)):
        y = array[k]
        i = k - 1
        while i >= 0 and array[i] > y:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = y

#Transcrição do código do slide
def shellSort(array, n, increments, numinc):
    incr = 0, j, k, span, y

    while incr < numinc:
        span = increments[incr]
        j = span
        while j < n:
            y = array[j]
            k = j - span
            while k >= 0:
                array[k + span] = array[k]
                k-=span
            array[k + span] = y
            j += 1
        incr += incr


#Escrever no CSV o tempo de execução de cada algoritmo, o tamanho da array e a organização dos valores
def menu():
    nomeAlgoritmo = []
    tamanhoVetor = []
    tempoExecucao = []

    tipoVetorDicionario = {
        1 : 'Aleatório',
        2 : 'Crescente',
        3 : 'Decrescente'
    }
    while True:
        print("1 - 1000\n2 - 5000\n3 - 10000\n4 - 15000\n5 - 20000\n6 - 25000\n")
        opcao = input("Escolha um tamanho para a array (1-6): ")
        tamanho = tamanhoArray(opcao)
        print("1 - Aleatório\n2 - Crescente\n3 - Decrescente")
        opcao2 = input("Escolha ordenação da array (1-3): ")
        array = criarArray(opcao2, tamanho)

        """for i in range(0, len(array)):
            print(array[i])"""

        print("1 - Bubble Sort sem melhorias\n2 - Bubble Sort com melhorias\n3 - Quick Sort com pivô elemento inicial\n4 - Quick Sort com pivô elemento central\n5 - Insertion Sort\n6 - Shell Sort\n7 - Selection Sort\n8 - Heap Sort\n9 - Merge Sort\n10 - Sair")

        opcao3 = input("Escolha uma opcao (1-10): ")
        
        if opcao3 == '1':
            #Adicionado as listas os parâmetros de execução
            nomeAlgoritmo.append("Bubble Sort sem melhorias")
            tamanhoVetor.append(len(array))

            inicio = default_timer()

            bubbleSort(array)
            """for i in range(0, len(array)):
                print(array[i])"""
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)
            
        elif opcao3 == '2':
            nomeAlgoritmo.append("Bubble Sort com melhorias")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            bubbleSortMelhoria(array)
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        elif opcao3 == '3':
            nomeAlgoritmo.append("Quick Sort com pivô elemento inicial")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            quickSortPivoInicio(array)
            final = default_timer()
            tempoExecucao.append(final - inicio)

        elif opcao3 == '4':
            nomeAlgoritmo.append("Quick Sort com pivô elemento central")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            quickSortPivoCentral(array)
            final = default_timer()
            tempoExecucao.append(final - inicio)
        elif opcao3 == '5':
            nomeAlgoritmo.append("Insertion Sort")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            insertionSort(array)
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        elif opcao3 == '6':
            nomeAlgoritmo.append("Shell Sort")
            tamanhoVetor.append(len(array))
            
            inicio = default_timer()
            #Insira Shell Sort
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        elif opcao3 == '7':
            nomeAlgoritmo.append("Selection Sort")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            #Insira Selection Sort
            final = default_timer()
            tempoExecucao.append(final - inicio)

        elif opcao3 == '8':
            nomeAlgoritmo.append("Heap Sort")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            #Insira Heap Sort
            final = default_timer()
            tempoExecucao.append(final - inicio)

        elif opcao3 == '9':
            nomeAlgoritmo.append("Merge Sort")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            #Insira Merge Sort
            final = default_timer()
            tempoExecucao.append(final - inicio)

        elif opcao3 == '10':
            print("Saindo")
            dicionario = {'Algoritmo': nomeAlgoritmo, 'tempoExecucao': tempoExecucao, 'Tamanho Vetor': tamanhoVetor}
            df = pandas.DataFrame(dicionario)
            print(df)
            nomeArquivo = 'Resultado' + tipoVetorDicionario[int(opcao2)] + '.csv'
            df.to_csv(nomeArquivo)
            return nomeArquivo
            break
        else:
            print("Opção inválida")

def tamanhoArray(opcao):
    if opcao == '1':
        return 1000
    elif opcao == '2':
        return 5000
    elif opcao == '3':
        return 10000
    elif opcao == '4':
        return 15000
    elif opcao == '5':
        return 20000
    elif opcao == '6':
        return 25000

def criarArray(opcao, tamanho):
    array = []
    if opcao == '1':
        return random.randint(tamanho, size=(tamanho))
    elif opcao == '2':
        for i in range(0, tamanho):
            array.append(i)
        return array
    else:
        for i in range(tamanho, 0, -1):
            array.append(i)
        return array

if __name__ == "__main__":
    #print(pandas.read_csv('data.csv').info())
    #pandas.read_csv('data.csv').plot()
    #plt.show()
    
    #for i in range(0, len(array)):
    #    print(array[i])
    nomeArquivo = menu()
    df = pandas.read_csv(nomeArquivo)
    df.plot(x = 'Tamanho Vetor', y = 'tempoExecucao', kind = 'line', title = 'Tempo de Execução X Tamanho Vetor')
    plt.xlabel('Tamanho Vetor')
    plt.ylabel('Tempo de Execucação (Segundos)')
    plt.show()
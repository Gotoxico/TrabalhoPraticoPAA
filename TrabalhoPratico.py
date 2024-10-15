from numpy import random
from timeit import default_timer
import pandas
import matplotlib.pyplot as plt
from math import floor

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

def particaoPivoInicio(array, limiteInferior, limiteSuperior):
    pivo = array[limiteInferior]
    baixo = limiteInferior + 1  # Começa a partir do próximo elemento após o pivô
    alto = limiteSuperior

    while True:
        # Movimenta o ponteiro baixo para a direita
        while baixo <= limiteSuperior and array[baixo] <= pivo:
            baixo += 1

        # Movimenta o ponteiro alto para a esquerda
        while alto >= limiteInferior and array[alto] > pivo:
            alto -= 1

        if baixo < alto:
            # Troca os valores
            array[baixo], array[alto] = array[alto], array[baixo]
        else:
            break

    # Coloca o pivô no local correto
    array[limiteInferior], array[alto] = array[alto], array[limiteInferior]
    return alto

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
    span = j = incr = 0
    for incr in range(numinc):
        span = increments[incr]
        for i in range(span, n):
            temp = array[i]
            j = i
            while j >= span and array[j - span] > temp:
                array[j] = array[j - span]
                j -= span
            array[j] = temp

def gerar_array_teorema1_formacao(tamanho):
    """Gera o array do Teorema 1 seguindo a lei de formação: 2^k - 1."""
    array = []
    k = 1
    while True:
        valor = 2 ** k - 1
        if k == tamanho:
            break
        array.append(valor)
        k += 1
    return array

def gerar_array_teorema2_formacao(tamanho):
    """Gera o array do Teorema 2 seguindo a lei de formação: 2^p * 3^q."""
    array = set()
    p = 0
    while True:
        q = 0
        while True:
            valor = 2 ** p * 3 ** q
            if valor >= tamanho:
                break
            array.add(valor)
            q += 1
        if 2 ** p >= tamanho:
            break
        p += 1
    return sorted(array)
    
def mergeSort(array, esquerda, direita):
    meio = 0
    if esquerda < direita:
        meio = (esquerda + direita) // 2
        mergeSort(array, esquerda, meio)
        mergeSort(array, meio + 1, direita)
        merge(array, esquerda, meio, direita)
        
def merge(array, esquerda, meio, direita):
    tamanhoEsquerda = meio - esquerda + 1
    tamanhoDireita = direita - meio

    arrayEsquerda = [0] * tamanhoEsquerda
    arrayDireita = [0] * tamanhoDireita

    for i in range(tamanhoEsquerda):
        arrayEsquerda[i] = array[esquerda + i]

    for j in range(tamanhoDireita):
        arrayDireita[j] = array[meio + 1 + j]

    i = 0
    j = 0
    k = esquerda

    while i < tamanhoEsquerda and j < tamanhoDireita:
        if arrayEsquerda[i] <= arrayDireita[j]:
            array[k] = arrayEsquerda[i]
            i = i + 1

        else:
            array[k] = arrayDireita[j]
            j = j + 1

        k = k + 1

    while i < tamanhoEsquerda:
        array[k] = arrayEsquerda[i]
        i = i + 1
        k = k + 1

    while j < tamanhoDireita:
        array[k] = arrayDireita[j]
        j = j + 1
        k = k + 1

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

        for i in range(0, len(array)):
            print(array[i])

        print("1 - Bubble Sort sem melhorias\n2 - Bubble Sort com melhorias\n3 - Quick Sort com pivô elemento inicial\n4 - Quick Sort com pivô elemento central\n5 - Insertion Sort\n6 - Shell Sort\n7 - Selection Sort\n8 - Heap Sort\n9 - Merge Sort\n10 - Sair")

        opcao3 = input("Escolha uma opcao (1-10): ")
        
        if opcao3 == '1':
            #Adicionado as listas os parâmetros de execução
            nomeAlgoritmo.append("Bubble Sort sem melhorias")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            bubbleSort(array)
            for i in range(0, len(array)):
                print(array[i])
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)
            
        elif opcao3 == '2':
            nomeAlgoritmo.append("Bubble Sort com melhorias")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            bubbleSortMelhoria(array)
            for i in range(0, len(array)):
                print(array[i])
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        elif opcao3 == '3':
            nomeAlgoritmo.append("Quick Sort com pivô elemento inicial")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            quickSortPivoInicio(array, 0, len(array)-1)
            for i in range(0, len(array)):
                print(array[i])
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        elif opcao3 == '4':
            nomeAlgoritmo.append("Quick Sort com pivô elemento central")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            quickSortPivoCentral(array, 0, len(array)-1)
            for i in range(0, len(array)):
                print(array[i])
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)
        elif opcao3 == '5':
            nomeAlgoritmo.append("Insertion Sort")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            insertionSort(array)
            for i in range(0, len(array)):
                print(array[i])
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        elif opcao3 == '6':
            nomeAlgoritmo.append("Shell Sort")
            tamanhoVetor.append(len(array))

            teorema = 0
            while teorema < 1 or teorema > 2:
                teorema = int(input('Digite se será utilizidado o teorema 1 ou 2 de formação do array de incrementos (1 ou 2): '))

            increments = []
            if teorema == 1:
                increments = gerar_array_teorema1_formacao(8)
                print("Vetor do Teorema 1:\n", increments)
            elif teorema == 2:
                increments = gerar_array_teorema2_formacao(20)
                print("Vetor do Teorema 2:\n", increments)
            

            inicio = default_timer()
            #Insira Shell Sort
            shellSort(array, len(array), increments, len(increments))
            for i in range(0, len(array)):
                print(array[i])
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        elif opcao3 == '7':
            nomeAlgoritmo.append("Selection Sort")
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            #Insira Selection Sort
            for i in range(0, len(array)):
                print(array[i])
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
            mergeSort(array, 0, len(array) - 1)
            for i in range(0, len(array)):
                print(array[i])
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        elif opcao3 == '10':
            print("Saindo")
            dicionario = {'Algoritmo': nomeAlgoritmo, 'tempoExecucao': tempoExecucao, 'Tamanho Vetor': tamanhoVetor}
            df = pandas.DataFrame(dicionario)
            print(df)
            nomeArquivo = 'C:\\Users\\user\\OneDrive - Unesp\\Documentos\\GitHub\\TrabalhoPraticoPAA\\CSVs\\' + 'Resultado' + tipoVetorDicionario[int(opcao2)] + '.csv'
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
        for i in range(0, tamanho):
            array.append(i)
        random.shuffle(array)
        return array
    elif opcao == '2':
        for i in range(0, tamanho):
            array.append(i)
        return array
    else:
        for i in range(tamanho, 0, -1):
            array.append(i)
        return array

def scriptTeste():


    nomeArquivo = menu()
    df = pandas.read_csv(nomeArquivo)
    df.plot(x = 'Tamanho Vetor', y = 'tempoExecucao', kind = 'line', title = 'Tempo de Execução X Tamanho Vetor')
    plt.xlabel('Tamanho Vetor')
    plt.ylabel('Tempo de Execucação (Segundos)')
    plt.show()
    

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

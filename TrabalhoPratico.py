import numpy as np
import random
from timeit import default_timer
import pandas
import matplotlib.pyplot as plt
from math import floor
#import sys

#sys.setrecursionlimit(1000000)
from sklearn.linear_model import LinearRegression


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

def particaoPivoInicioStack(array, limiteInferior, limiteSuperior):
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

def quickSortPivoInicioStack(array):
    stack = []

    # Inicializa a pilha com os limites do array completo
    stack.append((0, len(array) - 1))

    while stack:
        # Pop the top of the stack, getting the limits for the subarray
        limiteInferior, limiteSuperior = stack.pop()

        if limiteInferior < limiteSuperior:
            # Chama a partição com os limites correto
            q = particaoPivoInicioStack(array, limiteInferior, limiteSuperior)

            # Adiciona as duas partições resultantes na pilha
            stack.append((limiteInferior, q - 1))  # Lado esquerdo
            stack.append((q + 1, limiteSuperior))  # Lado direito

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

def particaoPivoCentralStack(array, limiteInferior, limiteSuperior):
    pivo = array[(limiteInferior + limiteSuperior)//2]
    baixo = limiteInferior
    alto = limiteSuperior

    while baixo <= alto:
        while array[baixo] < pivo:
            baixo += 1
        while array[alto] > pivo:
            alto -= 1
        if baixo <= alto:
            array[baixo], array[alto] = array[alto], array[baixo]
            baixo += 1
            alto -= 1
    
    return baixo

def quickSortPivoCentralStack(array):
    stack = []

    stack.append((0, len(array) - 1))

    while stack:
        limiteInferior, limiteSuperior = stack.pop()

        if limiteInferior < limiteSuperior:
            q = particaoPivoCentralStack(array, limiteInferior, limiteSuperior)

            stack.append((limiteInferior, q - 1))
            stack.append((q, limiteSuperior))

#Transcrição código slides
def insertionSort(array):
    for k in range(1, len(array)):
        y = array[k]
        i = k - 1
        while i >= 0 and array[i] > y:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = y

#Transcrição código slides
def SelectionSort(array):
    for i in range(len(array)):
        menor = array[i]
        index = i
        for j in range(i + 1, len(array)):
            if array[j] < menor:
                menor = array[j]
                index = j
        array[index] = array[i]
        array[i] = menor

#Transcrição código slides aula5 - parte 2
def  insertionSort(array):
    tamanho = len(array)
    for i in range(1, tamanho, +1):
        y = array[i]
        j = i - 1
        while j >= 0 and array[j] > y:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = y


#Código de impressão de array
#printar sem \n
def printArrayFull(array):
    for i in range(0, len(array)):
        print('{}, '.format(array[i]), end='')




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

#Função para transforma array em hesp maximo
def heapify(array, n , i):
    """
    :param array: O array a ser modificado
    :param n: O tamanho do heap
    :param i: O índice atual a ser ajustado
    """
    maior = i
    esquerda = 2* i + 1 # Filho à esquerda
    direita = 2 * i + 2 #Filho à direita

    # Se o filho à esquerda existe e é maior que a raiz
    if esquerda < n and array[esquerda] > array[maior]:
        maior = esquerda

    #Se o filho à direita existe e é maior que a raiz atual
    if direita < n and array[direita] > array[maior]:
        maior = direita

    # Se o maior não for a raiz
    if maior != i:
        array[i], array[maior] = array[maior], array[i]  # Troca
        heapify(array, n, maior)  # Recursivamente aplica o heapify na subárvore afetada

#Ordenação por Heap Sort
def heap_sort(array):
    n = len(array)

    # Constrói o heap (reorganiza o array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extrai os elementos um por um
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Troca
        heapify(array, i, 0)

    
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
def menu(opcao, tipo):
    nomeAlgoritmo = ''
    tamanhoVetor = []
    tempoExecucao = []
    i = 1
    tipoVetorDicionario = {
        1 : 'Aleatório',
        2 : 'Crescente',
        3 : 'Decrescente'
    }
    tamanhoArray = 0
    while True:
        tamanhoArray += i * 1000


        array = criarArray(tipo, tamanhoArray)
        arrayOrdenadoMerge = []
        
        if opcao == '1':
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
            print(len(array)-1)
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
            nomeAlgoritmo = "Shell Sort"
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
            # print('{}\n\n'.format(array))

        elif opcao == '9':
            nomeAlgoritmo = "Merge Sort"
            tamanhoVetor.append(len(array))

            inicio = default_timer()
            mergeSort(array, 0, len(array) - 1)
            # for i in range(0, len(array)):
            #     print(array[i])
            final = default_timer()
            tempoExecucao.append(final - inicio)
            print(final - inicio)

        if i == 15:
            print("Saindo")
            dicionario = {'Algoritmo': nomeAlgoritmo, 'tempoExecucao': tempoExecucao, 'Tamanho Vetor': tamanhoVetor}
            df = pandas.DataFrame(dicionario)
            print(df)
            nomeArquivo = 'C:\\Users\\kauan\\OneDrive\\Área de Trabalho\\Unesp-Loche\\segundo ano\\Segundo Semestre\\POOII - Escola\\TrabalhoPraticoPAA\\CSVs\\' + 'Resultado' + tipoVetorDicionario[int(tipo)] + nomeAlgoritmo + '.csv'
            df.to_csv(nomeArquivo)
            return nomeArquivo
        print(' ({})'.format(i))
        i += 1
       

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
        for i in range(tamanho): # Gera `tamanho` números únicos entre 0 e `tamanho - 1`
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



def menuDeExecucao():
    print("\n\nINICIO DA EXECUCAO\n\n")
    print("1 - Bubble Sort sem melhorias\n2 - Bubble Sort com melhorias\n3 - Quick Sort com pivô elemento inicial\n4 - Quick Sort com pivô elemento central\n5 - Insertion Sort\n6 - Shell Sort\n7 - Selection Sort\n8 - Heap Sort\n9 - Merge Sort\n10 - Sair\n")
    opcao = input("Escolha qual algoritmo será executado: ")

    print("1 - Aleatório\n2 - Crescente\n3 - Decrescente\n")
    tipo = input("Escolha o tipo de array: ")
    return opcao, tipo



if __name__ == "__main__":
    opcao = 0
    tipo = 0
    tipoVetorDicionario = {
        1 : 'Aleatório',
        2 : 'Crescente',
        3 : 'Decrescente'
    }
    while True:    
        opcao, tipo = menuDeExecucao()
        if opcao == 10:
            break
        nomeArquivo = menu(opcao , tipo)
        df = pandas.read_csv(nomeArquivo)
        df['Tempo de Execução'] = df['tempoExecucao'].rolling(window=5).mean()  # Ajuste o tamanho da janela 'window' conforme necessário
        df.plot(x='Tamanho Vetor', y='Tempo de Execução', kind='line', title='Tempo de Execução Suavizado X Tamanho Vetor')
        plt.xlabel('Tamanho Vetor')
        plt.ylabel('Tempo de Execução (Segundos)')
        plt.show()
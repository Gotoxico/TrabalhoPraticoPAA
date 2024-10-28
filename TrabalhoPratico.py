import numpy as np
import random
from timeit import default_timer
import pandas
import matplotlib.pyplot as plt
from math import floor
from scipy.interpolate import make_interp_spline
import time
import os
import re



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
        tamanhoArray += i * 1000000

        array = criarArray(tipo, tamanhoArray)
        arrayOrdenadoMerge = []
    
        if opcao == '0':
            nomeAlgoritmo = "Sort python"
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
            nomeAlgoritmo = "Shell Sort Teorema 2"
            tamanhoVetor.append(len(array))

            increments = []
            if i == 1:
                teorema = int(input('Digite se será utilizidado o teorema 1 ou 2 de formação do array de incrementos (1 ou 2): '))
 
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

        if i == 10:
            print("Saindo")
            dicionario = {'Algoritmo': nomeAlgoritmo, 'tempoExecucao': tempoExecucao, 'Tamanho Vetor': tamanhoVetor}
            df = pandas.DataFrame(dicionario)
            print(df)
            nomeArquivo = 'C:\\Users\\user\\OneDrive - Unesp\\Documentos\\GitHub\\TrabalhoPraticoPAA\\CSVs\\' + 'Resultado' + tipoVetorDicionario[int(tipo)] + nomeAlgoritmo + '.csv'
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
    print("0 - Tim (Python)\n1 - Bubble Sort sem melhorias\n2 - Bubble Sort com melhorias\n3 - Quick Sort com pivô elemento inicial\n4 - Quick Sort com pivô elemento central\n5 - Insertion Sort\n6 - Shell Sort\n7 - Selection Sort\n8 - Heap Sort\n9 - Merge Sort\n10 - Sair\n")
    opcao = input("Escolha qual algoritmo será executado: ")
    if opcao == '10':
        return 10, 0
    print("1 - Aleatório\n2 - Crescente\n3 - Decrescente\n")
    tipo = input("Escolha o tipo de array: ")
    return opcao, tipo

def adicionar_espacos(texto):
        return re.sub(r'([a-z])([A-Z])', r'\1 \2', texto)

if __name__ == "__main__":
    
    opcao = 0
    tipo = 0
    tipoVetorDicionario = {
        1 : 'Aleatório',
        2 : 'Crescente',
        3 : 'Decrescente'
    }
    arquivos = []
    while True:    
        opcao, tipo = menuDeExecucao()
        if opcao == 10:
            break
        nomeArquivo = menu(opcao , tipo)
        arquivos.append(nomeArquivo)
    
    for arquivo in arquivos:
        df = pandas.read_csv(arquivo)
        nome = df.loc[3, 'Algoritmo']
        df['Tempo de Execução'] = df['tempoExecucao'].rolling(window=5).mean()  # Ajuste o tamanho da janela 'window' conforme necessário
        plt.plot(df['Tamanho Vetor'], df['Tempo de Execução'], label=nome)  # Plotar os dados de cada CSV
    plt.xlabel('Tamanho Vetor')
    plt.ylabel('Tempo de Execução (Segundos)')
    plt.legend()
    plt.show()
    #     print('Escolha qual(is) gráfico(s) deseja construir:')
    #     print('1 - Bubble Sort sem melhorias')
    #     print('2 - Bubble Sort com melhorias')
    #     print('3 - Quick Sort com pivô elemento inicial')
    #     print('4 - Quick Sort com pivô elemento central')
    #     print('5 - Insertion Sort')
    #     print('6 - Shell Sort Teorema 1')
    #     print('7 - Shell Sort Teorema 2')
    #     print('8 - Selection Sort')
    #     print('9 - Heap Sort')
    #     print('10 - Merge Sort')
    #     print('11 - Sair')
    #     opcao = input('Escolha: ')
    #     if opcao == '11':
    #         break
    #     if opcao == '1':
    #         nomeArquivo =  'BubbleSortSemMelhorias'
    #     elif opcao == '2':
    #         nomeArquivo = 'BubbleSortComMelhorias'
    #     elif opcao == '3':
    #         nomeArquivo = 'QuickSortPivoInicial'
    #     elif opcao == '4':
    #         nomeArquivo = 'QuickSortPivoCentral'
    #     elif opcao == '5':
    #         nomeArquivo = 'InsertionSort'
    #     elif opcao == '6':
    #         nomeArquivo = 'ShellSortTeorema1'
    #     elif opcao == '7':
    #         nomeArquivo = 'ShellSortTeorema2'
    #     elif opcao == '8':
    #         nomeArquivo = 'SelectionSort'
    #     elif opcao == '9':
    #         nomeArquivo = 'HeapSort'
    #     elif opcao == '10':
    #         nomeArquivo = 'MergeSort'
        
    # plt.show()
    
    
    # df = pandas.read_csv("C:\\Users\\user\\OneDrive - Unesp\\Documentos\\GitHub\\TrabalhoPraticoPAA\\CSVs\\ShellSortTeorema2\\ResultadoAleatórioShell Sort Teorema 2.csv")
    # plt.figure(figsize=(10, 6))
    # plt.plot(df['Tamanho Vetor'], df['tempoExecucao'], marker='o', linestyle='-', color='b', label='Shell Sort Teorema 2')

 
    '''nomeDiretorio = input('Digite o nome do diretório onde os arquivos CSV estão localizados: ')
    # Diretório onde os arquivos CSV estão localizados
    diretorio = f'C:/Users/user/OneDrive - Unesp/Documentos/GitHub/TrabalhoPraticoPAA/CSVs/TodosDecrescentes/Sobrepostos'

    # Listar todos os arquivos CSV no diretório
    arquivos_csv = [arq for arq in os.listdir(diretorio) if arq.endswith('.csv')]

    # Iterar sobre cada arquivo CSV
    for arquivo in arquivos_csv:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        # Ler o CSV
        df = pandas.read_csv(caminho_arquivo)
        
        # Suavizar a coluna 'tempoExecucao' com média móvel exponencialmente ponderada
        df['Tempo Execucao'] = df['tempoExecucao'].ewm(span=10, adjust=False).mean()

        # Preencher valores NaN que podem ter sido gerados pela suavização
        df['Tempo Execucao'] = df['Tempo Execucao'].bfill()

        # Plotar os dados suavizados com marcador 'o' e linha contínua '-'
        plt.plot(df['Tamanho Vetor'], df['Tempo Execucao'], linestyle='-', label=adicionar_espacos(arquivo[:-4]))

    # Ajustar o grid e os intervalos do eixo x
    plt.xticks(np.arange(0, 56000, 5000))  # Marcas no eixo x de 5000 em 5000
    plt.grid(True, which='both', axis='both', linestyle='-', linewidth=0.7)

    # Adicionar legenda, título e rótulos
    plt.legend()
    titulo = input('Digite o título do gráfico: ')
    plt.title(titulo, fontsize=14)
    plt.xlabel('Tamanho do Vetor', fontsize=12)
    plt.ylabel('Tempo de Execução (segundos)', fontsize=12)

    # Exibir o gráfico com tamanho adequado
    plt.figure(figsize=(10, 6))
    plt.show()'''

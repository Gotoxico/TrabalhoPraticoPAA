from numpy import random
import time

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

    while(baixo < alto):
        while(array[baixo] <= pivo):
            baixo += baixo
        while(array[alto] > pivo):
            alto -= alto
        if(baixo < alto):
            array[baixo], array[alto] = array[alto], array[baixo]

    array[limiteInferior] = array[alto]
    array[alto] = pivo
    return alto   

#Transcrição código slides
def quickSort(array, limiteInferior, limiteSuperior):
    if(limiteInferior < limiteSuperior):
        q = particaoPivoInicio(array, limiteSuperior, limiteSuperior)
        quickSort(array, limiteInferior, q-1)
        quickSort(array, q+1, limiteInferior) 

#Escrever no CSV o tempo de execução de cada algoritmo, o tamanho da array e a organização dos valores
def menu(array):
    while True:
        print("1 - Bubble Sort sem melhorias\n2 - Bubble Sort com melhorias\n3 - Quick Sort com pivô elemento inicial\n4 - Quick Sort com pivô elemento central\n5 - Insertion Sort\n6 - Shell Sort\n7 - Selection Sort\n8 - Heap Sort\n9 - Merge Sort\n10 - Sair")

        opcao = input("Escolha uma opcao (1-10): ")
        
        if opcao == '1':
            bubbleSort(array)
        elif opcao == '10':
            print("Saindo")
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
    opcao = input("Escolha um tamanho para a array (1-6): ")
    tamanho = tamanhoArray(opcao)
    opcao2 = input("Escolha ordenação da array (1-3): ")
    array = criarArray(opcao2, tamanho)

    menu(array)
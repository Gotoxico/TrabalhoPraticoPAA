import random

def criarArray(opcao, tamanho):
    array = []
    if opcao == 1:
        for i in range(tamanho): # Gera `tamanho` números únicos entre 0 e `tamanho - 1`
            array.append(i)

        random.shuffle(array)                        
        return array
    elif opcao == 2:
        for i in range(0, tamanho):
            array.append(i)
        return array
    else:
        for i in range(tamanho, 0, -1):
            array.append(i)
        return array
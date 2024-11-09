import os
import pandas
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def plotarGrafico(arquivos, nomes):
    for arquivo, nome in zip(arquivos, nomes):
        df = pandas.read_csv(arquivo)
        
        # Aplicar suavização com Savitzky-Golay
        df['Tempo de Execução'] = savgol_filter(df['tempoExecucao'], window_length=9, polyorder=3)
        
        plt.plot(df['Tamanho Vetor'], df['Tempo de Execução'], label=nome)  # Plotar dados suavizados para cada CSV

    # Recebe o título do usuário
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo = input("\n\nDigite o título do gráfico:  ")
    
    plt.grid()
    plt.title(titulo, fontsize=14)
    plt.xlabel('Tamanho Vetor')
    plt.ylabel('Tempo de Execução (Segundos)')
    plt.legend()
    plt.show()
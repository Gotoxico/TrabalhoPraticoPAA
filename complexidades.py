import numpy as np
import matplotlib.pyplot as plt

# Gerar os dados
n = np.linspace(1, 100, 400)  # Variação de elementos (n)

# Definir as funções de complexidade
O_1 = np.ones_like(n)  # O(1)
O_log_n = np.log(n)    # O(log n)
O_n = n                # O(n)
O_n_log_n = n * np.log(n)  # O(n log n)
O_n2 = n**2            # O(n^2)
O_2n = 2**n            # O(2^n)

# Configurar o gráfico
plt.figure(figsize=(10, 6))

# Preencher as áreas coloridas
plt.fill_between(n, O_2n, O_n2, color="red", alpha=0.3, label='Horrible')
plt.fill_between(n, O_n2, O_n_log_n, color="orange", alpha=0.3, label='Bad')
plt.fill_between(n, O_n_log_n, O_n, color="yellow", alpha=0.3, label='Fair')
plt.fill_between(n, O_n, O_log_n, color="lightgreen", alpha=0.3, label='Good')
plt.fill_between(n, O_log_n, O_1, color="green", alpha=0.3, label='Excellent')

# Plotar as funções de complexidade
plt.plot(n, O_1, color="black", label=r"$O(1)$")
plt.plot(n, O_log_n, color="black", label=r"$O(\log n)$")
plt.plot(n, O_n, color="black", label=r"$O(n)$")
plt.plot(n, O_n_log_n, color="black", label=r"$O(n \log n)$")
plt.plot(n, O_n2, color="black", label=r"$O(n^2)$")
plt.plot(n, O_2n, color="black", label=r"$O(2^n)$")

# Configurar eixos e título
plt.ylim(1, 1000)
plt.xlim(1, 100)
plt.yscale('log')  # Escala logarítmica no eixo Y para melhor visualização
plt.xlabel("Elements")
plt.ylabel("Operations")
plt.title("Complexidade de Algoritmos (Big-O)")
plt.legend(loc="upper left")

# Mostrar o gráfico
plt.show()

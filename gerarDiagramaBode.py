import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def transfer_function_power(numerador, denominador, n):
    # Inicializar os coeficientes do numerador e denominador
    num_res = numerador
    den_res = denominador

    # Multiplicar a função de transferência por ela mesma (n-1) vezes
    for _ in range(n - 1):
        num_res = np.polymul(num_res, numerador)
        den_res = np.polymul(den_res, denominador)

    # Criar a função de transferência final com os novos coeficientes
    sistema = signal.TransferFunction(num_res, den_res)
    return sistema

# Definir os coeficientes do numerador e denominador da função de transferência
numerador = [157968000]      # Coeficientes de s no numerador
denominador = [1, 17774,157968000]     # Coeficientes de s no denominador

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.axhline(y=-3, color="red", linestyle="--", linewidth=0.8) #linha vermelha em -3db
ax1.axvline(x=12566, color="blue", linestyle="--", linewidth=0.8) #linha azul na wc

for n in range(1, 2):
    # Criar a função de transferência
    sistema = transfer_function_power(numerador, denominador, n)

    # Gerar o diagrama de Bode
    frequencias, ganho, fase = signal.bode(sistema)
    frequencias = frequencias  # Converter para rad

    # Criar uma figura com dois subplots

    ax1.semilogx(frequencias, ganho)

    # Configurações adicionais do gráfico de ganho
    ax1.set_title("Diagrama de Bode")
    ax1.set_ylabel("Ganho (dB)")
    ax1.grid(True, which="both", linestyle="--", color="gray", linewidth=0.5)
    ax1.legend()

    # Plotar a fase no segundo subplot
    ax2.semilogx(frequencias, fase)
    ax2.set_xlabel("Frequência (rad)")
    ax2.set_ylabel("Fase (graus)")
    ax2.grid(True, which="both", linestyle="--", color="gray", linewidth=0.5)

# Ajustar o layout para evitar sobreposição
plt.tight_layout()
plt.show()

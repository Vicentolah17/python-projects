import numpy as np
import matplotlib.pyplot as plt

# Entrada dos pontos amostrados
# Substitua estes valores pelos pontos fornecidos na tarefa
pontos = [(1, 2), (2, 3), (3, 5), (4, 7), (5, 8)]
x_vals, y_vals = zip(*pontos)
n = len(pontos)

# Retas aleatórias
a, b = 1, 0.5  # Coeficientes para a primeira reta aleatória ŷ = a + b*x
c, d = 0.5, 1  # Coeficientes para a segunda reta aleatória ŷ = c + d*x

# Função para calcular o desvio total D para uma dada reta
def calcular_desvio_total(y_calculado, y_real):
    return sum((y_calculado - y_real) ** 2)

# Calcular ŷ (primeira reta) e o desvio total D para a primeira reta
y_hat_1 = np.array([a + b * x for x in x_vals])
D1 = calcular_desvio_total(y_hat_1, np.array(y_vals))

# Calcular ŷ (segunda reta) e o desvio total D para a segunda reta
y_hat_2 = np.array([c + d * x for x in x_vals])
D2 = calcular_desvio_total(y_hat_2, np.array(y_vals))

# Calcular a melhor reta usando ajuste linear (método dos mínimos quadrados)
m, n = np.polyfit(x_vals, y_vals, 1)  # y = m*x + n
y_best_fit = m * np.array(x_vals) + n
D_best = calcular_desvio_total(y_best_fit, np.array(y_vals))

# Exibir os resultados
print("Primeira reta aleatória (ŷ = a + b*x):")
print(f"ŷ = {a} + {b} * x")
print(f"Desvio total D1 = {D1}")

print("\nSegunda reta aleatória (ŷ = c + d*x):")
print(f"ŷ = {c} + {d} * x")
print(f"Desvio total D2 = {D2}")

print("\nMelhor reta (ajuste linear):")
print(f"y = {m} * x + {n}")
print(f"Desvio total D_best = {D_best}")

# Plotar os pontos e as retas
plt.scatter(x_vals, y_vals, color='black', label='Pontos amostrados')
plt.plot(x_vals, y_hat_1, label=f"Reta aleatória 1: ŷ = {a} + {b}x, D1 = {D1:.2f}")
plt.plot(x_vals, y_hat_2, label=f"Reta aleatória 2: ŷ = {c} + {d}x, D2 = {D2:.2f}")
plt.plot(x_vals, y_best_fit, label=f"Melhor reta (ajuste): y = {m:.2f}x + {n:.2f}, D_best = {D_best:.2f}")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Ajuste Linear Simples")
plt.show()


import math
def funcao(x):
    # definição da função f(x) a ser analisada.
   return math.cos(x) - x

def bissecao(a, b, tol, max_iter=1000):
    if funcao(a) * funcao(b) >= 0:
        print("O intervalo [a, b] não é válido.")
        return None
    
    iteracoes = 0
    x_ant = a
    while iteracoes < max_iter:
        # 3º Passo: Obtenha o ponto médio
        x_m = (a + b) / 2.0
        
        # 4º Passo: Calcular f(x_m)
        f_x_m = funcao(x_m)
        
        # 5º Passo: Verificar se f(x_m) é zero ou suficientemente próximo
        if abs(f_x_m) < tol:
            print(f"Raiz encontrada: {x_m} (iter: {iteracoes})")
            return x_m
        
        # 6º Passo: Decidir o novo intervalo
        if funcao(a) * f_x_m < 0:
            b = x_m
        else:
            a = x_m
        
        # 7º Passo: Verificar convergência |x_n - x_(n-1)|
        if abs(x_m - x_ant) < tol:
            print(f"Raiz aproximada: {x_m} (iter: {iteracoes})")
            return x_m
        
        x_ant = x_m
        iteracoes += 1
    
    print("O método não convergiu após o número máximo de iterações.")
    return None

# Exemplo de uso:
a = -5  # Limite inferior do intervalo
b = 5   # Limite superior do intervalo
tol = 1e-6  # Tolerância
raiz = bissecao(a, b, tol)


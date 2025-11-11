from mpi4py import MPI
import numpy as np
import math
import sys


def calcular_somatorio(inicio, fim):
    
    if inicio > fim:
        return 0
    
    n = fim - inicio + 1
    soma = (n * (inicio + fim)) / 2
    return int(soma)

def somatorio_butterfly():
    # Inicializa o MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size() 

    
    # I. distribuição inicial
    
    
    N_elementos = 0 
    tag_num = 100

    if size == 1:
        print("ERRO: O Somatorio Butterfly requer N >= 2 (N deve ser potencia de 2).")
        return

    
    if rank == 0:
        
        try:
            
            N_elementos = 1000 
            print(f"Mestre (Rank 0) Somara elementos de 1 ate {N_elementos}.")
        except ValueError:
            print("Erro: Entrada invalida para N_elementos.")
            sys.exit()

        
        for i in range(1, size):
            
            comm.send(N_elementos, dest=i, tag=tag_num)
        
   
    else:
        
        N_elementos = comm.recv(source=0, tag=tag_num)
    
    
    parcela_tam = math.ceil(N_elementos / size) 
    
    
    inicio = (parcela_tam * rank) + 1
    fim = parcela_tam * (rank + 1)
    
    
    if rank == size - 1:
        fim = N_elementos
    
   
    if inicio > N_elementos:
        inicio = N_elementos + 1
        fim = N_elementos # Intervalo vazio
        
    
    somatorio = calcular_somatorio(inicio, fim)
    
    print(f"Rank {rank}: Intervalo [{inicio}, {fim}], Parcela local: {somatorio}")

   
    # II. Somatório Butterfly
    
    
    metade = size # N
    
    
    while rank < metade and metade > 1:
        metade_proximo = metade // 2
        
       
        soma_troca = somatorio
        
        
        if rank >= metade_proximo:
            
            destino = rank - metade_proximo
            comm.send(soma_troca, dest=destino, tag=rank)
            print(f"Rank {rank} (envia) -> Rank {destino}. Metade={metade_proximo}")
            
            
            break
            
        
        else:
            
            origem = rank + metade_proximo
            
            
            if origem < size:
                soma_recebida = comm.recv(source=origem, tag=origem)
                
                
                somatorio += soma_recebida
                print(f"Rank {rank} (recebe) <- Rank {origem}. Resultado parcial: {somatorio}. Metade={metade_proximo}")
            
            metade = metade_proximo 
        
    # III. resultado finap
    
    
    if rank == 0:
       
        print("\n===============================")
        print(f"Resultado final do Somatorio: {somatorio}")
        print("===============================")

if __name__ == '__main__':
    somatorio_butterfly()
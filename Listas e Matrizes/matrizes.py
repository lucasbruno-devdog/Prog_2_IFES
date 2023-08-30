def criar_matriz(m, n):
    M = []
    for i in range(m):
        M.append(n*[0])
    return M    

def imprimir_matriz(M):
    i = 0
    j = 0 
    for l in M:
        for elem in l:
            print(M[i][j], end='\t')
        print()
        
def somar_matrizes(A, B):
      n_linhas = len(A)
      n_colunas = len(A[0])
      C = criar_matriz(n_linhas, n_colunas)
      
      for i in range(n_linhas):
          for j in range(n_colunas):
              C[i][j] = A[i][j] + B[i][j]
      return C        
               

def matriz_identidade(M):
    #a matriz será identidade quando todos o elementos de sua diagonal principal for 1 e os demais elemntos forem 0
    i = 0
    j = 0
    linha = len(M)
    
    while i < linha:
        elem = len(M[i])
        if (linha != elem):
            return False
        while j < elem:
            if (i == j and M[i][j] != 1):
                return False
            if (i!=j and M[i][j] != 0):
                return False
            j+=1
        i+=1
    return True        

def determinante(M):
    diagonal_principal_1 = M[0][0]*M[1][1]*M[2][2]
    diagonal_principal_2 = M[0][1]*M[1][2]*M[2][0]
    diagonal_principal_3 = M[0][2]*M[1][0]*M[2][1]
    
    total_1 = diagonal_principal_1 + diagonal_principal_2 + diagonal_principal_3
    
    diagonal_secundaria_1 = M[0][2]*M[1][1]*M[2][0]
    diagonal_secundaria_2 = M[0][0]*M[1][2]*M[2][1]
    diagonal_secundaria_3 = M[0][1]*M[1][0]*M[2][2]
    
    total_2 = diagonal_secundaria_1 + diagonal_secundaria_2 + diagonal_secundaria_3
    
    resultado = total_1 - total_2
    
    return resultado
    
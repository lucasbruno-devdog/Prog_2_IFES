def notas(m, n):
    alunos_M = []
    for i in range(m):
        notas = []
        for j in range(n):
            nota = int(input("Digite a nota {} do aluno {}: ".format(i+1, j+1)))
            notas.append(nota)
        alunos_M.append(notas)    
    return alunos_M
def media():
    m = int(input("Informe a quantidade de alunos:"))
    n = int(input("Informe quantas avaliacoes foram: "))
    alunos = notas(m, n)
    soma = 0
    
    for i in range(m):
        soma_aluno = 0
        for nota in alunos[i]:
            soma_aluno += nota
         
        media_aluno = soma_aluno / len(alunos[i])
        soma += media_aluno
        print(f'Aluno {i+1}:{media_aluno:.2f}')
        
    media_t = soma / len(alunos)
    print(f'Media da turma:{media_t:.2f}')
    
def main():
    
    media()
    
    return 0
if __name__ == "__main__":
    main()                  
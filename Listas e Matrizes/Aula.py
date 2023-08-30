def regressiva():
    l2 = []
    for i in range(1,101):   
        if (i % 2) == 0:
            l2.append(i)
    return l2[::-1]

def metade():
    l = []
    for i in range(1,11):
        print("Digite o número:")
        a = int(input())
        if (a > 0):
            l.append(a/2)
    return l

def leitura():
    i = 0
    l = []
    print("Digite um número n:")
    n = int(input())
    while i < n:
        print("Digite um número:")
        a = int(input())
        l.append(a)
        i+=1
    return l

def ocorrencias():
    l1 = [4, 5, 2, 4, 5, 3, 5, 6, 5, 8]
    cont = 0
    print("Digite um elemento:")
    n = int(input())
    return l1.count(n)
         

def máximo():
    l1 = [4, 5, 2, 4, 5, 3, 5, 6, 5, 8]
    maior = 0
    for i in l1:
      if maior < i:
          maior = i
    return maior

def posição_máximo():
    l1 = [4, 5, 2, 4, 5, 3, 5, 6, 5, 8]
    maior = 0
    for i in range(len(l1)):
      if l1[maior] < l1[i]:
          maior = i
    return maior

def inverter():
    l1 = [4, 5, 2, 4, 5, 3, 5, 6, 5, 8]
    print(l1)
    return l1[::-1]

def fibonacci():
    l = []
    fibo = 1
    x = 0
    print("Digite um número:")
    num = int(input())
    for i in range(num):
        r = x + fibo
        l.append(r)
        x = fibo
        fibo = r
        
    return l  

def ordenada_abcissa():
    orde = [4, 5, 2, 4]
    abci = [9, 1, 5, 3]
    a = 0
    b = 0
    produto = 1
    for i in abci:
        if i % 2 == 0:
            a+=1
    for o in orde:
        if o % 2 != 0:
            b+=1        
    if a >= b:
     soma = sum(abci)
     print(soma)
    else:
       for num in orde:
           produto*= num
       print(produto)        

def k_múltiplos():
    l = []
    print("Digite um número K:")
    k = int(input())
    print("Digite uma número N:")
    n = int(input())
    i = 1
    while i <= n:
        produto = i * k
        l.append(produto)
        i+=1
    return l    

def médias():
  l = []
  l2 = []
  x = 0

  print("Digite um número n:")
  n = int(input())

  while x <= n - 1:
    print("Digite as notas:")
    a = int(input())

    if a >= 0 and a <= 100:
      if a >= 60:
        l2.append(a)
      l.append(a)
      x += 1

  soma = sum(l)
  média = soma / x

  print(f'{média:.2f}')
  print(l2)


def temperaturas():
  l = []
  l2 = []
  x = 0

  print("Digite um número n:")
  n = int(input())

  while x <= n - 1:
    print("Digite as temperaturas dos dias:")
    a = int(input())
    l.append(a)
    x += 1
  soma = sum(l)
  média = soma / x

  for i in l:
    if i < média:
      l2.append(i)

  print(f'{média:.2f}°C')
  print(l2)

def iguais():
    l1 = [9, 3, 7, 10, 8, 5, 7, 4, 1, 9]
    l2 = [1, 5, 4, 10, 8, 2, 1, 9, 8, 2]
    
    cont = 0
    
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            cont+=1
    return cont    
    
def salários():
    l1 = []
    l2 = []
    x = 0

    print("Digite um número n:")
    n = int(input())

    while x <= n - 1:
        print("Digite o nome do funcionário:")
        a = input()
        l1.append(a)
        print("Digite o salário do funcionário:")
        b = int(input())
        l2.append(b)
        x+=1     

    soma = sum(l2)
    média = soma / x

    for i in range(n):
        if l2[i] > média:
            print(l1[i])  

def sublista():
    l1 = [1, 3, 3, 4, 5, 6, 7, 9, 9,10]
    l2 = []
    x = 3
    y = 8
    
    for i in l1:
        if x < i < y:
            l2.append(i)
    
    return l2
    #return l1[x:y-1] <- outra alternativa 
    
                                              
def main():
    
    #print(regressiva())
    #print(metade())
    #print(leitura())
    #print(ocorrencias())
    #print(máximo())
    #print(posição_máximo())
    #print(inverter())
    #print(fibonacci())
    #ordenada_abcissa()
    #print(k_múltiplos())
    #médias()
    #temperaturas()
    #print(iguais())
    #salários()
    #print(sublista())
    
    
    
    return 0
if __name__ == "__main__":
    main()
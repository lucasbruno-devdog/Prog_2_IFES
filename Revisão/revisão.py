def fat(n):
    result = 1
    cont = 2
    while cont <= n:
        result = result * cont
        cont += 1
        
    return result    

def comb(n, p):
    num = fat(n)
    den = fat(p)*fat(n-p)
    
    return num/den

def mult(n, k):
    cont = 1
    while cont <= n:
        result = k * cont
        cont += 1
        print(result)  

def divisor(x, y):
    if(y % x) == 0:
        return True
    else:
        return False
    
def divisores(k):
    cont = 1
    while cont <= k:
      if (k % cont) == 0:
          print(cont)
      cont+=1 
         
def mdc(m, n):
    cont = 1
    mdc = 1
    while cont <= min(m, n):
        if divisor(cont, m) and divisor(cont, n):
            mdc = cont
        cont+=1
    return mdc

def primo(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False           
        return True 

def primos(k):
    i = 2
    while i <= k:
        if primo(i):
            print(i)
        i+=1    
      
def main():
    num1 = int(input())
    num2 = int(input())
    
    print(fat(num1))
    print(comb(num1, num2))
    print(mult(num1, num2))
    print(divisor(num1, num2))
    print(divisores(num1))
    print(mdc(num1, num2))
    print(primo(num1))
    print(primos(num1))
    
    return 0
if __name__ == "__main__":
  main()
    
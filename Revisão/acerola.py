def acerola(n, f):
    litros_tomado = 0
    quantidade = f * 0.05
    litros_tomado = quantidade / n
    
    return print(f'{litros_tomado:.2f}')

def main():
    n = int(input())
    f = int(input())
    
    acerola(n, f)
    
    return 0
if __name__ == "__main__":
  main()
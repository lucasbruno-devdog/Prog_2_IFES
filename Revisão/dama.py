def modular(x):
    i = ()
    if (x < 0):
        i = -x
    else:
        i = x  
    return i

def mesma_posição(Xa, Ya, Xb, Yb):
    if(Xa == Xb ) and (Ya == Yb):
        return mesma_posição

def alinhado(Xa, Ya, Xb, Yb):
    if(Xa == Xb ) or (Ya == Yb) or (modular(Xa - Xb ) == modular(Ya - Yb)):
        return alinhado         

def main():
    print("Informe a posição inicial da dama:")
    Xa = int(input())
    Ya = int(input())
    
    print("Informe para onde moveu:")
    Xb = int(input())
    Yb = int(input())
    
    if(mesma_posição(Xa, Ya, Xb, Yb)):
        print("Saída:")
        print(0)
        
    elif(alinhado(Xa, Ya, Xb, Yb)):
        print("Saída:")
        print(1)
            
    else:
        print("Saída:")
        print(2)
    
    return 0
if __name__ == "__main__":
  main()
    
def modular(x):
    i = ()
    if (x < 0):
        i = -x
    else:
        i = x  
    return i 
   
def main():
    num1 = int(input())
    num2 = int(input())
    result = num1 - num2
    
    print(modular(result))
    
    return 0
if __name__ == "__main__":
  main()
        
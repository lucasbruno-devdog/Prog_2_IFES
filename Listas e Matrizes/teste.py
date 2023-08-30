def fibonnaci(num):
    i = 0
    a = 1
    print(a)
    for x in range (num - 1):
        p = i + a
        print(p)
        i = a
        a = p
def main():
    num = int(input())
    fibonnaci(num)
        
    return 0

if __name__ == "__main__":
    main()

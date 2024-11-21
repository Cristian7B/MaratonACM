def icfes():
    nTest = int(input())
    lista = []
    l = []
    for i in range(nTest):
        lista.append(list(map(int, input().split())))

    for elemento in lista:
        l.append(1-(((elemento[0]-1)/elemento[0])**elemento[1]))
    
    for ls in l:
        print(f"{ls:.6f}") 

icfes()
def calcular():
    ops= int(input())
    ls = []
    for i in range(ops):
        ls.append(cuantos(int(input()), list(map(int, input().split()))))
    for l in ls:
        print(l)

def cuantos(a, b):
    cantidad = 0
    contador = 1
    for i in range(1, a):
        if b[i] >= b[i-1]:
            contador += 1
        else:
            cantidad += calcularSum(contador)
            contador = 1
        
    cantidad += calcularSum(contador)
    return cantidad
    
def calcularSum(c):
    return c*(c+1)//2


calcular()

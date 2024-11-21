# --------------- Mi solución ---------------
# Error en el tiempo de ejecución

from itertools import combinations
 
def calcular():
    notasComp = list(input())
    notasBob = list(input())
    print(notasBob)
 
    for i in range(len(notasComp)):
        combComp = list(combinations(notasComp, i))  
        combBob = list(combinations(notasBob, i)) 
 
        for elemento in combComp:
            if elemento not in combBob:
                return "".join(elemento)
 
    return "-"
    
calcular()


# ---------------- Solucion ---------------- 
def find_shortest_unique_substring(S, B):
    n = len(S)
    for length in range(1, n + 1):
        substrings = {S[i:i+length] for i in range(n - length + 1)}
        
        for substring in substrings:
            if substring not in B:
                return substring  
    
    return "-"  

S = input().strip()
B = input().strip()

result = find_shortest_unique_substring(S, B)
print(result)

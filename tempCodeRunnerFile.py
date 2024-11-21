

def calcular():
    notasComp = list(input())
    notasBob = list(input())
    for i in range(len(notasComp)):
        if i + 1 > 1:
            for j in range(i+1, len(notasComp)):
                comb = notasComp[i] + notasComp[j]
                if comb not in notasBob:
                    return comb
        else:
            for element in notasComp:
                if element not in notasBob:
                    return element

        # combComp = list(combinations(notasComp, i))  
        # combBob = list(combinations(notasBob, i)) 

        # for elemento in combComp:
        #     if elemento not in combBob:
        #         return "".join(elemento)

    return "-"
print(calcular())
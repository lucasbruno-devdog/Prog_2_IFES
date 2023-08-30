def sem_repeticao(l):
    l2 = [l[0]]
    
    for i in l:
        if i != l2[-1]:
            l2.append(i)
    return l2

def troca(l1, l2):
    l1 = sem_repeticao(l1)
    l2 = sem_repeticao(l2)
    
    trocas_a = 0
    for carta in l1:
        if carta not in l2:
            trocas_a += 1
    trocas_b = 0
    for carta in l2:
        if carta not in l1:
            trocas_b += 1
    return min(trocas_a, trocas_b)
print(troca([1, 3, 5], [2, 4, 6, 8]))            
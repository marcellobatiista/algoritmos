def ordenar(lista):
    tmp = [lista[0]]
    i = 0
    while (i < len(lista)-1):
        if (lista[i+1] > tmp[0]):
            tmp.insert(0,lista[i+1])
        else:
            existe = False
            for j in enumerate(tmp):
                if lista[i+1] >= j[1]:
                    tmp.insert(j[0], lista[i+1])
                    existe = True
                    break
            if not(existe):
                tmp.append(lista[i+1])
        i += 1
    return tmp


lista = [-1,0,8,7,6,5,1,10,4,3,2,1,-1]

ordem = ordenar(lista)

print(ordem)

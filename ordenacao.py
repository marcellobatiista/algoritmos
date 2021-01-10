def ordenar(lista):
    tmp = [lista[0]]

    i = 0
    while (i < len(lista)-1):
        primeiro = tmp[0]
        sucessor = lista[i+1]
        
        if (sucessor > primeiro):
            tmp.insert(0,sucessor)
        else:
            existe = False
            for j in enumerate(tmp):
                if sucessor >= j[1]:
                    tmp.insert(j[0], sucessor)
                    existe = True
                    break
            if not(existe):
                tmp.append(sucessor)
        i += 1
    return tmp


lista = [8,0,1,0,6,-6,5,5,8,-1,-8]

ordem = ordenar(lista)

print(ordem)

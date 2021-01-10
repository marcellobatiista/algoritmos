def ordenar(lista):
    tmp = [lista[0]]

    i = 0
    while (i < len(lista)-1):
        primeiro = tmp[0]
        sucessor = lista[i+1]
        
        if (sucessor > primeiro):
            tmp.insert(0,sucessor)
        else:
            j = 1
            existe = False
            while (j <= len(tmp)-1):
                if sucessor >= tmp[j]:
                    tmp.insert(j, sucessor)
                    existe = True
                    break
                j += 1
            if not(existe):
                tmp.append(sucessor)
        i += 1
    return tmp


lista = [8,0,1,0,5,5,8,-1,-8]

ordem = ordenar(lista)

print(ordem)

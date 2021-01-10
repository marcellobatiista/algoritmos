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
                if sucessor > tmp[j]:
                    tmp.insert(j, sucessor)
                    existe = True
                elif sucessor == tmp[j]:
                    tmp.insert(j+1, sucessor)
                    existe = True
                    
                if (existe):
                    break
                    
                j += 1
            if not(existe):
                tmp.append(sucessor)
        i += 1
    return tmp


lista = [-1,-4,0,-3,-1,124,54,4,6,4,7,7,4,6,7,1,2,4,36,8,54,456,456,456]

ordem = ordenar(lista)

print(ordem)

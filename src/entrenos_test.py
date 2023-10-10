import entrenos

def imprime_con_tabulacion(lista):
    for l in lista:
        print('\t', l)

def test_lee_entrenos():
    print('test entrenos')
    listaEntrenos = entrenos.leer_entrenos('data/entrenos.csv')
    print(f'Se han leido {len(listaEntrenos)}.')
    print(f'Los tres primero registros son: ')
    imprime_con_tabulacion(listaEntrenos[:3])
    print(f'Los tres primero registros son: ')
    imprime_con_tabulacion(listaEntrenos[-3:])

test_lee_entrenos()
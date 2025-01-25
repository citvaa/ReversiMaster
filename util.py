import random
import copy
import time

import heuristika
import minimax


DUBINA = 7
VREMENSKO_OGRANICENJE = 3  # sekunde


def inicijalizacija_table():
    tabla = [[0] * 8 for _ in range(8)]
    tabla[3][3] = tabla[4][4] = 1
    tabla[3][4] = tabla[4][3] = -1
    return tabla


def prikaz_table(tabla):
    print("  0 1 2 3 4 5 6 7")
    for i in range(8):
        row = str(i) + " "
        for j in range(8):
            if tabla[i][j] == 0:
                row += ". "
            elif tabla[i][j] == 1:
                row += "X "
            else:
                row += "O "
        print(row)
    # heuristika_stanja_prikaz(tabla)
    rezultat_prikaz(tabla)


def moguci_potezi(tabla, igrac):
    if igrac not in (-1, 1):
        raise AssertionError("Nevažeći igrač")

    lista = []
    protivnik = -igrac

    pomeraji = [-1, 0, 1]
    tabla_duzina = range(8)

    for x in tabla_duzina:
        for y in tabla_duzina:
            if tabla[x][y] == protivnik:
                for dx in pomeraji:
                    for dy in pomeraji:
                        if dx == dy == 0:
                            continue

                        if 0 <= x + dx < 8 and 0 <= y + dy < 8:
                            if tabla[x + dx][y + dy] == 0:
                                m = 1
                                while True:
                                    i = x - m * dx
                                    j = y - m * dy

                                    if i < 0 or i >= 8 or j < 0 or j >= 8:
                                        break

                                    if tabla[i][j] == igrac:
                                        if (x + dx, y + dy) not in lista:
                                            lista.append((x + dx, y + dy))
                                        break

                                    if tabla[i][j] == 0:
                                        break

                                    m += 1

    return lista


def okreni_figure(tabla, x, y):
    igrac = tabla[x][y]
    protivnik = -igrac
    pomeraji = [-1, 0, 1]

    for dx in pomeraji:
        for dy in pomeraji:
            if dx == dy == 0:
                continue

            if 0 <= x + dx < 8 and 0 <= y + dy < 8 and tabla[x + dx][y + dy] == protivnik:
                m = 1
                while 0 <= x + m * dx < 8 and 0 <= y + m * dy < 8:
                    m += 1
                    if 0 <= x + m * dx < 8 and 0 <= y + m * dy < 8:
                        if tabla[x + m * dx][y + m * dy] == 0:
                            break
                    if 0 <= x + m * dx < 8 and 0 <= y + m * dy < 8 and tabla[x + m * dx][y + m * dy] == igrac:
                        n = 1
                        while n < m:
                            tabla[x + n * dx][y + n * dy] = igrac
                            n += 1


def potez_igrac(tabla):
    print('Moguci potezi: ' + str(moguci_potezi(tabla, 1)))
    while True:
        unos = input("Unesite koordinate polja za potez (format: x y): ")
        koordinate = unos.split()
        if len(koordinate) != 2:
            print("Neispravan unos. Molimo unesite ispravne koordinate.")
            continue
        x, y = koordinate
        if not x.isdigit() or not y.isdigit():
            print("Neispravan unos. Molimo unesite ispravne koordinate.")
            continue
        x = int(x)
        y = int(y)
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            print("Neispravne koordinate. Molimo unesite ispravne koordinate unutar granica table (0-7).")
            continue
        if tabla[x][y] != 0:
            print("Polje je već zauzeto. Molimo odaberite prazno polje.")
            continue
        if (x, y) not in moguci_potezi(tabla, 1):
            print("Neispravan potez. Molimo odaberite potez koji okreće protivničke figure.")
            continue
        break
    tabla[x][y] = 1
    okreni_figure(tabla, x, y)


def potez_racunar_random(tabla):
    lista = moguci_potezi(tabla, -1)
    (x, y) = random.choice(lista)
    tabla[x][y] = -1
    okreni_figure(tabla, x, y)


def potez_racunar(tabla):
    (x, y) = najbolji_potez_racunar(tabla)
    tabla[x][y] = -1
    okreni_figure(tabla, x, y)
    print('Racunar je odigrao: ' + str(x) + ' ' + str(y))
    
    
def najbolji_potez_racunar(tabla):
    vreme_pocetka = time.time()
    najbolji_potez = None
    najbolja_vrednost = float('-inf')

    for potez in moguci_potezi(tabla, -1):
        nova_tabla = tabla_nakon_odigranog_poteza(tabla, potez, -1)
        vrednost = minimax.minimax_alfa_beta(nova_tabla, DUBINA, float('-inf'), float('inf'), False, vreme_pocetka)
        if vrednost > najbolja_vrednost:
            najbolja_vrednost = vrednost
            najbolji_potez = potez

    return najbolji_potez


def tabla_nakon_odigranog_poteza(tabla, potez, igrac):
    (x, y) = potez

    if potez not in moguci_potezi(tabla, igrac):
        raise AssertionError('Izabrali ste nepostojeci potez')

    nova_tabla = copy.deepcopy(tabla)
    nova_tabla[x][y] = igrac

    okreni_figure(nova_tabla, x, y)

    return nova_tabla


def kraj(tabla, igrac):
    if len(moguci_potezi(tabla, igrac)) == 0:
        return True
    else:
        return False


def poruka_za_kraj(tabla, igrac):  # igrac koji je zadnji odigrao potez
    for x in range(8):
        for y in range(8):
            if tabla[x][y] == 0:
                if igrac == 1:
                    print('Racunar je pobedio. Igrac nema mogucih poteza')
                else:
                    print('Igrac je pobedio. Racunar nema mogucih poteza')
                exit()
    broj_igrac = 0
    broj_racunar = 0
    for x in range(8):
        for y in range(8):
            if tabla[x][y] == 1:
                broj_igrac += 1
            elif tabla[x][y] == -1:
                broj_racunar += 1
    if broj_igrac > broj_racunar:
        print('Igrac je pobedio')
    elif broj_igrac < broj_racunar:
        print('Racunar je pobedio')
    else:
        print('Nereseno je')
    exit()


def heuristika_stanja_prikaz(tabla):
    print('Heuristika stanja table: ' + str(heuristika.dynamic_heuristic_evaluation_function(tabla)))


def rezultat_prikaz(tabla):
    broj_igrac = 0
    broj_racunar = 0
    for x in range(8):
        for y in range(8):
            if tabla[x][y] == 1:
                broj_igrac += 1
            elif tabla[x][y] == -1:
                broj_racunar += 1
    print('Igrac - Racunar ' + str(broj_igrac) + ':' + str(broj_racunar))


def generisi_hash_kljuc(tabla):
    tabla_string = ''.join([''.join(map(str, red)) for red in tabla])
    hash_kljuc = hash(tabla_string)
    return hash_kljuc



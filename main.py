import heuristika
import util
import minimax


def igraj_reversi_easy():
    igrac_na_potezu = 1
    tabla = util.inicijalizacija_table()
    util.prikaz_table(tabla)
    while not util.kraj(tabla, igrac_na_potezu):
        if igrac_na_potezu == 1:
            util.potez_igrac(tabla)
            igrac_na_potezu = -1
        else:
            util.potez_racunar_random(tabla)
            igrac_na_potezu = 1
        util.prikaz_table(tabla)
    util.poruka_za_kraj(tabla, igrac_na_potezu)


def igraj_reversi_hard():
    igrac_na_potezu = 1
    tabla = util.inicijalizacija_table()
    util.prikaz_table(tabla)
    while not util.kraj(tabla, igrac_na_potezu):
        if igrac_na_potezu == 1:
            util.potez_igrac(tabla)
            igrac_na_potezu = -1
        else:
            util.potez_racunar(tabla)
            igrac_na_potezu = 1
        util.prikaz_table(tabla)
    util.poruka_za_kraj(tabla, igrac_na_potezu)


def meni():
    print('Igra Reversi(Othello)')
    print('1. Lako')
    print('2. Tesko')
    while True:
        opcija = input("Izaberite tezinu (1-2): ")
        if opcija == '1':
            igraj_reversi_easy()
        elif opcija == '2':
            igraj_reversi_hard()
        else:
            print('Pogresan unos. Unesite vrednost ponovo')


if __name__ == '__main__':
    meni()


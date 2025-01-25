import time

import util
import heuristika


eval_mapa = {}


def minimax_alfa_beta(tabla, dubina, alfa, beta, maximizing, vreme_pocetka):
    hash_kljuc = util.generisi_hash_kljuc(tabla)
    if hash_kljuc in eval_mapa:
        return eval_mapa[hash_kljuc]

    if dubina == 0 or util.kraj(tabla, -1):
        vrednost = heuristika.dynamic_heuristic_evaluation_function(tabla)
        eval_mapa[hash_kljuc] = vrednost
        return vrednost

    if time.time() - vreme_pocetka >= util.VREMENSKO_OGRANICENJE:
        vrednost = heuristika.dynamic_heuristic_evaluation_function(tabla)
        eval_mapa[hash_kljuc] = vrednost
        return vrednost

    if maximizing:
        max_eval = float('-inf')
        for potez in util.moguci_potezi(tabla, -1):
            nova_tabla = util.tabla_nakon_odigranog_poteza(tabla, potez, -1)
            eval = minimax_alfa_beta(nova_tabla, dubina - 1, alfa, beta, False, vreme_pocetka)
            max_eval = max(max_eval, eval)
            alfa = max(alfa, eval)
            if beta <= alfa:
                break
        eval_mapa[hash_kljuc] = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for potez in util.moguci_potezi(tabla, 1):
            nova_tabla = util.tabla_nakon_odigranog_poteza(tabla, potez, 1)
            eval = minimax_alfa_beta(nova_tabla, dubina - 1, alfa, beta, True, vreme_pocetka)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alfa:
                break
        eval_mapa[hash_kljuc] = min_eval
        return min_eval

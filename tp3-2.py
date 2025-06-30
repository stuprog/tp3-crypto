
import math
from collections import Counter


def calculer_entropie(texte: str) -> float:

    if not texte:
        return 0.0
    frequences = Counter(texte)
    total = len(texte)
    return -sum((f / total) * math.log2(f / total) for f in frequences.values())


def calculer_redondance(texte: str, taille_alphabet: int = 26) -> float:

    if not texte:
        return 0.0
    h = calculer_entropie(texte)
    return 1.0 - (h / math.log2(taille_alphabet))


def indice_coincidence(texte: str) -> float:

    n = len(texte)
    if n < 2:
        return 0.0
    frequences = Counter(texte)
    somme = sum(f * (f - 1) for f in frequences.values())
    return somme / (n * (n - 1))



if __name__ == "__main__":
    texte_exemple = "WELCOME TO THE CRYPTO".upper()

    h = calculer_entropie(texte_exemple)
    r = calculer_redondance(texte_exemple)
    ic = indice_coincidence(texte_exemple)

    print("Texte analysé :", texte_exemple)
    print(f"Entropie             : {h:.4f} bits")
    print(f"Redondance           : {r:.4f}")
    print(f"Indice de coïncidence: {ic:.4f}")


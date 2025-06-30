import numpy as np


def chiffrement_hill(texte: str, matrice_cle: np.ndarray) -> str:

    texte = texte.upper().replace(" ", "")


    if matrice_cle.shape != (2, 2):
        raise ValueError("La matrice de clé doit être 2x2.")


    if len(texte) % 2 != 0:
        texte += 'X'

    texte_chiffre = ''

    for i in range(0, len(texte), 2):
        bloc = [ord(texte[i]) - 65, ord(texte[i + 1]) - 65]  # A → 0, B → 1, ..., Z → 25
        vecteur = np.array(bloc)
        chiffré = np.dot(matrice_cle, vecteur) % 26
        texte_chiffre += ''.join(chr(c + 65) for c in chiffré)

    return texte_chiffre



if __name__ == "__main__":
    texte_clair = "CRYPTOGRAPHIE"
    matrice = np.array([[3, 3], [2, 5]])  # matrice  2x2

    texte_chiffre = chiffrement_hill(texte_clair, matrice)

    print("=== Chiffrement de Hill (Lester Hill) ===")
    print("Texte clair      :", texte_clair)
    print("Matrice utilisée :\n", matrice)
    print("Texte chiffré    :", texte_chiffre)

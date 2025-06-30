def pgcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a


def chiffrement_affine(texte: str, a: int, b: int) -> str:

    if pgcd(a, 26) != 1:
        raise ValueError("a doit être premier avec 26 pour que le chiffrement affine soit valide.")

    texte = texte.upper().replace(" ", "")
    resultat = ''

    for char in texte:
        if char.isalpha():
            x = ord(char) - 65  # A → 0
            chiffre = (a * x + b) % 26
            resultat += chr(chiffre + 65)
        else:
            resultat += char  # on garde les caractères non alphabétiques tels quels

    return resultat


if __name__ == "__main__":
    texte = "CRYPTOGRAPHIE"
    a = 7
    b = 3

    try:
        texte_chiffre = chiffrement_affine(texte, a, b)
        print("=== Chiffrement Affine ===")
        print("Texte clair     :", texte)
        print(f"Paramètres      : a = {a}, b = {b}")
        print("Texte chiffré   :", texte_chiffre)
    except ValueError as e:
        print("Erreur :", e)

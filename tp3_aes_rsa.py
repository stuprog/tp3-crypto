from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

def aes_chiffrer_dechiffrer(message: str):
    cle = get_random_bytes(16)
    cipher = AES.new(cle, AES.MODE_EAX)
    texte_chiffre, tag = cipher.encrypt_and_digest(message.encode())
    cipher_dechiffrer = AES.new(cle, AES.MODE_EAX, nonce=cipher.nonce)
    texte_dechiffre = cipher_dechiffrer.decrypt(texte_chiffre).decode()
    return texte_chiffre, texte_dechiffre

def rsa_chiffrer_dechiffrer(message: str):
    cle_privee = RSA.generate(2048)
    cle_publique = cle_privee.publickey()
    cipher_rsa = PKCS1_OAEP.new(cle_publique)
    texte_chiffre = cipher_rsa.encrypt(message.encode())
    cipher_rsa_dechiffrer = PKCS1_OAEP.new(cle_privee)
    texte_dechiffre = cipher_rsa_dechiffrer.decrypt(texte_chiffre).decode()
    return texte_chiffre, texte_dechiffre

if __name__ == "__main__":
    message = "Information confidentielle"
    aes_c, aes_d = aes_chiffrer_dechiffrer(message)
    rsa_c, rsa_d = rsa_chiffrer_dechiffrer(message)

    print("=== AES ===")
    print("Chiffré (b64):", base64.b64encode(aes_c).decode())
    print("Déchiffré   :", aes_d)

    print("\n=== RSA ===")
    print("Chiffré (b64):", base64.b64encode(rsa_c).decode())
    print("Déchiffré   :", rsa_d)

from Crypto.PublicKey import RSA as CryptoRSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class RSA:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.cipher = None
        
    def get_public_key(self):
        return self.public_key.export_key().decode()
    
    def get_private_key(self):
        return self.private_key.export_key().decode()

    def generate_keys(self, key_size=2048):
        key = CryptoRSA.generate(key_size)
        self.public_key = key.publickey()
        self.private_key = key
        self.cipher = PKCS1_OAEP.new(key.publickey())

    def encrypt(self, plaintext):
        ciphertext = self.cipher.encrypt(plaintext.encode())
        return base64.b64encode(ciphertext).decode()

    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)
        cipher = PKCS1_OAEP.new(self.private_key)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext.decode()

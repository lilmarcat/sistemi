from Ciphers.CipherInterface import CipherInterface

class VigenereCipher(CipherInterface):
    def __init__(self):
        self.key = ""

    def set_key(self, key: str) -> None:
        self.key = key.upper()

    def get_key(self) -> str:
        return self.key

    def pad_key(self, data: str) -> str:
        repeated_key = self.key * (len(data) // len(self.key)) + self.key[:len(data) % len(self.key)]
        return repeated_key.upper()

    def encrypt(self, data: str) -> str:
        padded_key = self.pad_key(data)
        result = ""
        for i in range(len(data)):
            char_index = ord(data[i].upper()) - 65
            key_index = ord(padded_key[i]) - 65
            encrypted_char_index = (char_index + key_index) % 26
            encrypted_char = chr(encrypted_char_index + 65)
            if data[i].islower():
                encrypted_char = encrypted_char.lower()
            result += encrypted_char
        return result

    def decrypt(self, encrypted_data: str) -> str:
        padded_key = self.pad_key(encrypted_data)
        result = ""
        for i in range(len(encrypted_data)):
            char_index = ord(encrypted_data[i].upper()) - 65
            key_index = ord(padded_key[i]) - 65
            decrypted_char_index = (char_index - key_index) % 26
            decrypted_char = chr(decrypted_char_index + 65)
            if encrypted_data[i].islower():
                decrypted_char = decrypted_char.lower()
            result += decrypted_char
        return result

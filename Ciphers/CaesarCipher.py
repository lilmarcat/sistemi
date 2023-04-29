from Ciphers.CipherInterface import CipherInterface

class CaesarCipher(CipherInterface):
    def __init__(self):
        self.key = 0

    def set_key(self, key: int) -> None:
        self.key = key

    def get_key(self) -> int:
        return self.key

    def encrypt(self, data: str) -> str:
        result = ""
        for char in data:
            if char.isalpha():
                if char.isupper():
                    shifted_char = chr((ord(char) + self.key - 65) % 26 + 65)
                else:
                    shifted_char = chr((ord(char) + self.key - 97) % 26 + 97)
                result += shifted_char
            else:
                result += char
        return result

    def decrypt(self, encrypted_data: str) -> str:
        result = ""
        for char in encrypted_data:
            if char.isalpha():
                if char.isupper():
                    shifted_char = chr((ord(char) - self.key - 65) % 26 + 65)
                else:
                    shifted_char = chr((ord(char) - self.key - 97) % 26 + 97)
                result += shifted_char
            else:
                result += char
        return result
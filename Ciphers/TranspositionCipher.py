from Ciphers.CipherInterface import CipherInterface
import math

class TranspositionCipher(CipherInterface):
    def __init__(self):
        self.key = None

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def encrypt(self, plaintext):
        ciphertext = ''
        num_columns = len(self.key)
        num_rows = math.ceil(len(plaintext) / num_columns)
        num_blanks = (num_rows * num_columns) - len(plaintext)
        plaintext += ' ' * num_blanks
        column_order = [i[0] for i in sorted(enumerate(self.key), key=lambda x:x[1])]
        for column in column_order:
            for row in range(num_rows):
                index = (row * num_columns) + column
                ciphertext += plaintext[index]
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        num_columns = len(self.key)
        num_rows = math.ceil(len(ciphertext) / num_columns)
        column_order = [i[0] for i in sorted(enumerate(self.key), key=lambda x:x[1])]
        column_lengths = [num_rows for i in range(num_columns)]
        num_short_columns = num_columns * num_rows - len(ciphertext)
        for i in range(num_short_columns):
            column_lengths[column_order[i]] -= 1
        plaintext_matrix = [''] * num_columns
        index = 0
        for column in column_order:
            for row in range(column_lengths[column]):
                plaintext_matrix[column] += ciphertext[index]
                index += 1
        for row in range(num_rows):
            for column in range(num_columns):
                if row >= column_lengths[column]:
                    continue
                plaintext += plaintext_matrix[column][row]
        return plaintext.rstrip()

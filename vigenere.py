import tkinter as tk

def vigenere_cypher(text, key, mode):
    # Creazione della matrice di Vigenere
    vigenere_table = []
    for i in range(26):
        row = []
        for j in range(26):
            row.append(chr((i + j) % 26 + ord('A')))
        vigenere_table.append(row)

    # Rimuove eventuali spazi e converte il testo in maiuscolo
    text = text.upper().replace(" ", "")

    # Si ripete la chiave fino alla lunghezza del testo
    key = key.upper()
    key *= len(text) // len(key) + 1
    key = key[:len(text)]

    # Cifratura o decifratura
    result = ""
    for i in range(len(text)):
        row = ord(text[i]) - ord('A')
        col = ord(key[i]) - ord('A')
        if mode == "encrypt":
            result += vigenere_table[row][col]
        else:
            for j in range(26):
                if vigenere_table[j][col] == text[i]:
                    result += chr(j + ord('A'))
                    break

    return result
    # Implementazione della cifratura e decifratura di Vigenere
    # (il codice è lo stesso del programma precedente)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Creazione dei widget dell'interfaccia

        # Etichette
        self.plaintext_label = tk.Label(self, text="Testo in chiaro:")
        self.plaintext_label.grid(row=0, column=0, sticky=tk.W)
        self.key_label = tk.Label(self, text="Chiave:")
        self.key_label.grid(row=1, column=0, sticky=tk.W)
        self.ciphertext_label = tk.Label(self, text="Testo cifrato/decifrato:")
        self.ciphertext_label.grid(row=2, column=0, sticky=tk.W)

        # Caselle di testo
        self.plaintext_entry = tk.Entry(self, width=50)
        self.plaintext_entry.grid(row=0, column=1, columnspan=2)
        self.key_entry = tk.Entry(self, width=50)
        self.key_entry.grid(row=1, column=1, columnspan=2)
        self.ciphertext_entry = tk.Entry(self, width=50, state=tk.DISABLED)
        self.ciphertext_entry.grid(row=2, column=1, columnspan=2)

        # Pulsanti
        self.encrypt_button = tk.Button(self, text="Cifra", command=self.encrypt)
        self.encrypt_button.grid(row=3, column=0, pady=10)
        self.decrypt_button = tk.Button(self, text="Decifra", command=self.decrypt)
        self.decrypt_button.grid(row=3, column=1, pady=10)
        self.clear_button = tk.Button(self, text="Pulisci", command=self.clear)
        self.clear_button.grid(row=3, column=2, pady=10)

    def encrypt(self):
        # Cifratura del testo e aggiornamento della casella di testo corrispondente
        plaintext = self.plaintext_entry.get()
        key = self.key_entry.get()
        ciphertext = vigenere_cypher(plaintext, key, "encrypt")
        self.ciphertext_entry.config(state=tk.NORMAL)
        self.ciphertext_entry.delete(0, tk.END)
        self.ciphertext_entry.insert(0, ciphertext)
        self.ciphertext_entry.config(state=tk.DISABLED)

    def decrypt(self):
        # Decifratura del testo e aggiornamento della casella di testo corrispondente
        ciphertext = self.plaintext_entry.get()
        key = self.key_entry.get()
        plaintext = vigenere_cypher(ciphertext, key, "decrypt")
        self.ciphertext_entry.config(state=tk.NORMAL)
        self.ciphertext_entry.delete(0, tk.END)
        self.ciphertext_entry.insert(0, plaintext)
        self.ciphertext_entry.config(state=tk.DISABLED)

    def clear(self):
        # Pulizia delle caselle di testo
        self.plaintext_entry.delete(0, tk.END)
        self.key_entry.delete(0, tk.END)
        self.ciphertext_entry.config(state=tk.NORMAL)
        self.ciphertext_entry.delete(0)
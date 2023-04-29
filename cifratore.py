
import tkinter as tk

def caesar_cipher(text, shift, encrypt=True):
    """Implementazione del cifrario di Giulio Cesare
    
    Args:
    text (str): Testo da cifrare o decifrare
    shift (int): Numero di posizioni da spostare per cifrare/decifrare il testo
    encrypt (bool): Flag per indicare se cifrare (True) o decifrare (False) il testo
    
    Returns:
    str: Testo cifrato o decifrato
    """
    if not encrypt:
        shift = -shift
    
    cipher_text = ""
    for char in text:
        if char.isalpha():
            # Calcola il nuovo valore ASCII della lettera
            ascii_val = ord(char) + shift
            
            # Se il nuovo valore ASCII eccede il range delle lettere
            # (65-90 per le maiuscole, 97-122 per le minuscole),
            # torna all'inizio del range.
            if char.isupper():
                if ascii_val > ord('Z'):
                    ascii_val = ascii_val - 26
                elif ascii_val < ord('A'):
                    ascii_val = ascii_val + 26
            elif char.islower():
                if ascii_val > ord('z'):
                    ascii_val = ascii_val - 26
                elif ascii_val < ord('a'):
                    ascii_val = ascii_val + 26
            
            # Aggiunge la lettera cifrata/decifrata al testo finale
            cipher_text += chr(ascii_val)
        else:
            # Aggiunge i caratteri non alfabetici senza cifrarli
            cipher_text += char
            
    return cipher_text

def encrypt_text():
    plaintext = input_text.get("1.0", "end-1c")  # Legge il testo inserito dall'utente
    shift = int(shift_entry.get())  # Legge lo spostamento inserito dall'utente
    ciphertext = caesar_cipher(plaintext, shift)  # Cifra il testo
    output_text.delete("1.0", "end")  # Cancella il testo precedente nell'area di output
    output_text.insert("end", ciphertext)  # Inserisce il testo cifrato nell'area di output

def decrypt_text():
    ciphertext = input_text.get("1.0", "end-1c")  # Legge il testo inserito dall'utente
    shift = int(shift_entry.get())  # Legge lo spostamento inserito dall'utente
    plaintext = caesar_cipher(ciphertext, shift, encrypt=False)  # Decifra il testo
    output_text.delete("1.0", "end")  # Cancella il testo precedente nell'area di output
    output_text.insert("end", plaintext)  # Inserisce il testo decifrato nell'area di output

# Creazione della finestra principale
root = tk.Tk()
root.title("Cifrario di Giulio Cesare")

# Creazione dei widget per l'input
input_label = tk.Label(root, text="Testo da cifrare/decifrare:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=0, column=1, padx=5, pady=5)

# Creazione dei widget per lo spostamento
shift_label = tk.Label(root, text="Spostamento:")
shift_label.grid(row=1, column=0, padx=5, pady=5)
shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1, padx=5, pady=5)

# Creazione dei widget per la scelta dell'azione
action_label = tk.Label(root, text="Azione:")
action_label.grid(row=2, column=0, padx=5, pady=5)
encrypt_button = tk.Button(root, text="Cifrare", command=encrypt_text)
encrypt_button.grid(row=2, column=1, padx=5, pady=5)
decrypt_button = tk.Button(root, text="Decifrare", command=decrypt_text)
decrypt_button.grid(row=2, column=2, padx=5, pady=5)

# Creazione dell'area di output
output_label = tk.Label(root, text="Risultato:")
output_label.grid(row=3, column=0, padx=5, pady=5)
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()

    

plaintext = "CIAO MONDO!"
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print(ciphertext)  # Output: "FLDR PRQGR!"
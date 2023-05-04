import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from Ciphers.CaesarCipher import CaesarCipher
from Ciphers.VigenereCipher import VigenereCipher
from Ciphers.TranspositionCipher import TranspositionCipher
from Ciphers.RSA_cipher import RSA




class CipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher GUI")
        self.create_widgets()
        

    def create_widgets(self):
        # Create notebook widget with tabs for each cipher
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)

        # Create Caesar cipher tab
        caesar_tab = ttk.Frame(notebook)
        notebook.add(caesar_tab, text='Caesar Cipher')
        caesar_key_label = ttk.Label(caesar_tab, text='Shift:')
        caesar_key_label.pack(side='left')
        self.caesar_key_entry = ttk.Entry(caesar_tab, width=5)
        self.caesar_key_entry.pack(side='left')
        self.caesar_encrypt_button = ttk.Button(caesar_tab, text='Encrypt', command=self.caesar_encrypt)
        self.caesar_encrypt_button.pack(side='left')
        self.caesar_decrypt_button = ttk.Button(caesar_tab, text='Decrypt', command=self.caesar_decrypt)
        self.caesar_decrypt_button.pack(side='left')
        self.caesar_input_text = tk.Text(caesar_tab, height=5)
        self.caesar_input_text.pack(fill='both', expand=True)
        self.caesar_output_text = tk.Text(caesar_tab, height=5)
        self.caesar_output_text.pack(fill='both', expand=True)

        # Create Vigenere cipher tab
        vigenere_tab = ttk.Frame(notebook)
        notebook.add(vigenere_tab, text='Vigenere Cipher')
        vigenere_key_label = ttk.Label(vigenere_tab, text='Key:')
        vigenere_key_label.pack(side='left')
        self.vigenere_key_entry = ttk.Entry(vigenere_tab, width=10)
        self.vigenere_key_entry.pack(side='left')
        self.vigenere_encrypt_button = ttk.Button(vigenere_tab, text='Encrypt', command=self.vigenere_encrypt)
        self.vigenere_encrypt_button.pack(side='left')
        self.vigenere_decrypt_button = ttk.Button(vigenere_tab, text='Decrypt', command=self.vigenere_decrypt)
        self.vigenere_decrypt_button.pack(side='left')
        self.vigenere_input_text = tk.Text(vigenere_tab, height=5)
        self.vigenere_input_text.pack(fill='both', expand=True)
        self.vigenere_output_text = tk.Text(vigenere_tab, height=5)
        self.vigenere_output_text.pack(fill='both', expand=True)

        # Create Transposition cipher tab
        transposition_tab = ttk.Frame(notebook)
        notebook.add(transposition_tab, text='Transposition Cipher')
        transposition_key_label = ttk.Label(transposition_tab, text='Key:')
        transposition_key_label.pack(side='left')
        self.transposition_key_entry = ttk.Entry(transposition_tab, width=10)
        self.transposition_key_entry.pack(side='left')
        self.transposition_encrypt_button = ttk.Button(transposition_tab, text='Encrypt', command=self.transposition_encrypt)
        self.transposition_encrypt_button.pack(side='left')
        self.transposition_decrypt_button = ttk.Button(transposition_tab, text='Decrypt', command=self.transposition_decrypt)
        self.transposition_decrypt_button.pack(side='left')
        self.transposition_input_text = tk.Text(transposition_tab, height=5)
        self.transposition_input_text.pack(fill='both', expand=True)
        self.transposition_output_text = tk.Text(transposition_tab, height=5)
        self.transposition_output_text.pack(fill='both', expand=True)

        # Create RSA tab
        """
        rsa_tab = ttk.Frame(notebook)
        self.rsa_cipher = RSA()
        notebook.add(rsa_tab, text='RSA Cipher')
        rsa_key_label = ttk.Button(rsa_tab, text='Generate new keys', command=self.rsa_generate_keys)
        rsa_key_label.pack(side='left')
        self.rsa_encrypt_button = ttk.Button(rsa_tab, text='Encrypt', command=self.rsa_encrypt)
        self.rsa_encrypt_button.pack(side='left')
        self.rsa_decrypt_button = ttk.Button(rsa_tab, text='Decrypt', command=self.rsa_decrypt)
        self.rsa_decrypt_button.pack(side='left')
        self.rsa_input_text = tk.Text(rsa_tab, height=5)
        self.rsa_input_text.pack(fill='both', expand=True)
        self.rsa_output_text = tk.Text(rsa_tab, height=5)
        self.rsa_output_text.pack(fill='both', expand=True)
        """
        rsa_tab = ttk.Frame(notebook)
        self.rsa_cipher = RSA()
        self.rsa_cipher.generate_keys()
        notebook.add(rsa_tab, text='RSA Cipher')

        # Create a frame for the left components
        rsa_left_frame = ttk.Frame(rsa_tab)
        rsa_left_frame.pack(side='left')

        # Add the "Generate new keys" button to the left frame
        rsa_key_label = ttk.Button(rsa_left_frame, text='Generate new keys', command=self.rsa_generate_keys)
        rsa_key_label.grid(row=0, column=0, sticky="w", padx=10)
        self.rsa_public_key_label = ttk.Label(rsa_left_frame, text='Public Key: ')
        self.rsa_public_key_label.grid(row=1, column=0, sticky="w", padx=10)
        self.rsa_private_key_label = ttk.Label(rsa_left_frame, text='Private Key: ')
        self.rsa_private_key_label.grid(row=2, column=0, sticky="w", padx=10)
        self.rsa_public_key_text = ttk.Label(rsa_left_frame, text=f'{str(self.rsa_cipher.get_public_key())}')
        #self.rsa_public_key_text = ttk.Label(rsa_left_frame, text='')
        self.rsa_public_key_text.grid(row=1, column=1, sticky="w", padx=10)
        self.rsa_private_key_text = ttk.Label(rsa_left_frame, text=f'{str(self.rsa_cipher.get_private_key())}')
        #self.rsa_private_key_text = ttk.Label(rsa_left_frame, text='')
        self.rsa_private_key_text.grid(row=2, column=1, sticky="w", padx=10)

        
        # Add the encrypt and decrypt buttons to the right of the RSA tab
        self.rsa_encrypt_button = ttk.Button(rsa_left_frame, text='Encrypt', command=self.rsa_encrypt)
        self.rsa_encrypt_button.grid(row=3, column=0, sticky="w", padx=10)
        self.rsa_decrypt_button = ttk.Button(rsa_left_frame, text='Decrypt', command=self.rsa_decrypt)
        self.rsa_decrypt_button.grid(row=3, column=1, sticky="w", padx=10)

        # Add the input and output textboxes to the center of the RSA tab
        self.rsa_input_text = tk.Text(rsa_tab, height=5)
        self.rsa_input_text.pack(fill='both', expand=True)
        self.rsa_output_text = tk.Text(rsa_tab, height=5)
        self.rsa_output_text.pack(fill='both', expand=True)


    def caesar_encrypt(self):
        try:
            shift = int(self.caesar_key_entry.get())
            plaintext = self.caesar_input_text.get('1.0', 'end-1c')
            cipher = CaesarCipher()
            cipher.set_key(shift)
            ciphertext = cipher.encrypt(plaintext)
            self.caesar_output_text.delete('1.0', 'end')
            self.caesar_output_text.insert('1.0', ciphertext)
        except ValueError:
            self.caesar_output_text.delete('1.0', 'end')
            self.caesar_output_text.insert('1.0', 'Invalid shift value')

    def caesar_decrypt(self):
        try:
            shift = int(self.caesar_key_entry.get())
            #ciphertext = self.caesar_input_text.get('1.0', 'end-1c')
            ciphertext = self.caesar_output_text.get('1.0', 'end-1c')
            cipher = CaesarCipher()
            cipher.set_key(shift)
            plaintext = cipher.decrypt(ciphertext)
            #self.caesar_output_text.delete('1.0', 'end')
            #self.caesar_output_text.insert('1.0', plaintext)
            self.caesar_input_text.delete('1.0', 'end')
            self.caesar_input_text.insert('1.0', plaintext)
        except ValueError:
            #self.caesar_output_text.delete('1.0', 'end')
            #self.caesar_output_text.insert('1.0', 'Invalid shift value')
            self.caesar_input_text.delete('1.0', 'end')
            self.caesar_input_text.insert('1.0', 'Invalid shift value')

    def vigenere_encrypt(self):
        key = self.vigenere_key_entry.get()
        plaintext = self.vigenere_input_text.get('1.0', 'end-1c')
        cipher = VigenereCipher()
        cipher.set_key(key)
        ciphertext = cipher.encrypt(plaintext)
        self.vigenere_output_text.delete('1.0', 'end')
        self.vigenere_output_text.insert('1.0', ciphertext)

    def vigenere_decrypt(self):
        key = self.vigenere_key_entry.get()
        #ciphertext = self.vigenere_input_text.get('1.0', 'end-1c')
        ciphertext = self.vigenere_output_text.get('1.0', 'end-1c')
        cipher = VigenereCipher()
        cipher.set_key(key)
        plaintext = cipher.decrypt(ciphertext)
        #self.vigenere_output_text.delete('1.0', 'end')
        #self.vigenere_output_text.insert('1.0', plaintext)
        self.vigenere_input_text.delete('1.0', 'end')
        self.vigenere_input_text.insert('1.0', plaintext)

    def transposition_encrypt(self):
        key = self.transposition_key_entry.get()
        plaintext = self.transposition_input_text.get('1.0', 'end-1c')
        cipher = TranspositionCipher()
        cipher.set_key(key)
        ciphertext = cipher.encrypt(plaintext)
        self.transposition_output_text.delete('1.0', 'end')
        self.transposition_output_text.insert('1.0', ciphertext)

    def transposition_decrypt(self):
        key = self.transposition_key_entry.get()
        #ciphertext = self.transposition_input_text.get('1.0', 'end-1c')
        ciphertext = self.transposition_output_text.get('1.0', 'end-1c')
        cipher = TranspositionCipher()
        cipher.set_key(key)
        plaintext = cipher.decrypt(ciphertext)
        #self.transposition_output_text.delete('1.0', 'end')
        #self.transposition_output_text.insert('1.0', plaintext)
        self.transposition_input_text.delete('1.0', 'end')
        self.transposition_input_text.insert('1.0', plaintext)

    def rsa_generate_keys(self):
        self.rsa_cipher.generate_keys()
        self.rsa_public_key_text.config(text=str(self.rsa_cipher.get_public_key()))
        self.rsa_private_key_text.config(text=str(self.rsa_cipher.get_private_key()))
        
        
    def rsa_encrypt(self):
        # Get the public key and plaintext
        plaintext = self.rsa_input_text.get('1.0', tk.END)

        # Encrypt the plaintext using the public key
        ciphertext = self.rsa_cipher.encrypt(plaintext)

        # Display the ciphertext in the output box
        self.rsa_output_text.delete('1.0', tk.END)
        self.rsa_output_text.insert('1.0', ciphertext)

    def rsa_decrypt(self):
        # Get the private key and ciphertext
        ciphertext = self.rsa_output_text.get('1.0', tk.END)

        # Decrypt the ciphertext using the private key
        plaintext = self.rsa_cipher.decrypt(ciphertext)

        # Display the plaintext in the output box
        self.rsa_input_text.delete('1.0', tk.END)
        self.rsa_input_text.insert('1.0', plaintext)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1250x900")
    icon = PhotoImage(file="icona.gif")
    root.iconphoto(True, icon)
    gui = CipherGUI(root)
    root.mainloop()
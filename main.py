from tkinter import *
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

selected_file = ""

def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    file_label.config(text=selected_file)

def encrypt_file():
    global selected_file
    key = key_entry.get().encode()

    if len(key) != 16:
        messagebox.showerror(
            "Error",
            "Key must be 16 characters!"
        )
        return

    with open(selected_file, "rb") as file:
        data = file.read()

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(
        pad(data)
    )

    save_path = filedialog.asksaveasfilename(
        defaultextension=".enc"
    )

    with open(save_path, "wb") as file:
        file.write(encrypted_data)

    messagebox.showinfo(
        "Success",
        "File Encrypted!"
    )

def decrypt_file():
    global selected_file
    key = key_entry.get().encode()

    if len(key) != 16:
        messagebox.showerror(
            "Error",
            "Key must be 16 characters!"
        )
        return

    with open(selected_file, "rb") as file:
        data = file.read()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(data)

    save_path = filedialog.asksaveasfilename()

    with open(save_path, "wb") as file:
        file.write(decrypted_data.rstrip())

    messagebox.showinfo(
        "Success",
        "File Decrypted!"
    )

root = Tk()
root.title("Data Encryption Tool")
root.geometry("500x300")

Label(
    root,
    text="CS-502 Data Encryption Tool",
    font=("Arial",16)
).pack(pady=10)

Button(
    root,
    text="Select File",
    command=select_file
).pack()

file_label = Label(root, text="")
file_label.pack()

Label(root, text="Enter 16 Character Key").pack()

key_entry = Entry(root, width=30)
key_entry.pack()

Button(
    root,
    text="Encrypt",
    command=encrypt_file
).pack(pady=10)

Button(
    root,
    text="Decrypt",
    command=decrypt_file
).pack()

root.mainloop()
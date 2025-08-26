import tkinter as tk
from tkinter import messagebox

def validar_senha():
    senha = entry_senha.get()  # pega o texto digitado

    if len(senha) == 8:
        messagebox.showinfo("Validação", "Senha válida!")
    else:
        messagebox.showerror("Validação", "Senha inválida! Deve conter exatamente 8 caracteres.")


root = tk.Tk()
root.title("Validador de Senha")
root.geometry("300x150")


tk.Label(root, text="Digite sua senha:").pack(pady=10)


entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

tk.Button(root, text="Validar", command=validar_senha).pack(pady=10)

root.mainloop()

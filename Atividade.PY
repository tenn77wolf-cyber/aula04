import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    nota_texto = entry_nota.get()  # pega a informação da nota

    if nota_texto.replace(".", "", 1).isdigit():
        nota = float(nota_texto)

        
        if nota == 10:
            resultado = "Parabéns, nota máxima!"
        elif 9 <= nota < 10:
            resultado = "Quase perfeito!"
        elif nota >= 7:
            resultado = "Aprovado!!"
        elif nota >= 5:
            resultado = "Recuperação!!"
        elif 0 <= nota < 5:
            resultado = "Reprovado com baixa nota."
        else:
            resultado = "Nota inválida."  # caso alguém digite negativo

        messagebox.showinfo("Resultado", f"Situação: {resultado}")
    else:
        messagebox.showerror("Erro", "Digite um número válido.")

# Janela principal
root = tk.Tk()
root.title("Verificador de Notas")
root.geometry("300x200")
root.configure(bg="#F0E68C")

tk.Label(root, text="Digite a nota do aluno:", bg="#F0E68C").pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

tk.Button(
    root,
    text="Verificar",
    command=verificar_nota,
    bg="blue",
    fg="white",
    font=("Arial", 11, "bold")
).pack(pady=10)

root.mainloop()

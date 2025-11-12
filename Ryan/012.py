import tkinter as tk
from tkinter import messagebox

def calcular():
    nome_produto = entrada_nome.get()
    try:
        estoque_inicial = int(entrada_estoque_inicial.get())
        vendidas = int(entrada_vendidas.get())

        if vendidas > estoque_inicial:
            messagebox.showerror("Erro", "A quantidade vendida não pode ser maior que o estoque inicial!")
            return

        estoque_atual = estoque_inicial - vendidas
        porcentagem_vendida = (vendidas / estoque_inicial) * 100
        porcentagem_estoque = (estoque_atual / estoque_inicial) * 100

        resultado.set(
            f"Produto: {nome_produto}\n"
            f"Estoque Inicial: {estoque_inicial}\n"
            f"Vendidas: {vendidas}\n"
            f"Estoque Atual: {estoque_atual}\n"
            f"Porcentagem Vendida: {porcentagem_vendida:.2f}%\n"
            f"Porcentagem em Estoque: {porcentagem_estoque:.2f}%"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos para as quantidades!")

janela = tk.Tk()
janela.title("Controle de Estoque")
janela.geometry("400x400")
janela.config(bg="#f0f0f0")

tk.Label(janela, text="Nome do Produto:", bg="#f0f0f0").pack(pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

tk.Label(janela, text="Estoque Inicial:", bg="#f0f0f0").pack(pady=5)
entrada_estoque_inicial = tk.Entry(janela)
entrada_estoque_inicial.pack(pady=5)

tk.Label(janela, text="Vendidas:", bg="#f0f0f0").pack(pady=5)
entrada_vendidas = tk.Entry(janela)
entrada_vendidas.pack(pady=5)

tk.Button(janela, text="Calcular", command=calcular, bg="#4CAF50", fg="white").pack(pady=10)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, bg="#f0f0f0", justify="left", font=("Arial", 10)).pack(pady=10)

janela.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class ControleEstoqueApp:
    def __init__(self, master):
        self.master = master
        self.master.title("💙 Cruzeiro E.C. - Controle de Estoque")
        self.master.attributes('-fullscreen', True)
        self.master.configure(bg="#0D47A1")

        self.master.bind("<Escape>", self.sair_tela_cheia)

        self.produtos = []  # Lista com (nome, estoque_inicial, vendidas, estoque_atual)

        self._criar_estilo()
        self._criar_widgets()

    def sair_tela_cheia(self, event=None):
        self.master.attributes('-fullscreen', False)
        self.master.geometry("1000x700")

    def _criar_estilo(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", background="#0D47A1", foreground="white", font=("Segoe UI", 12, "bold"))
        style.configure("TEntry", fieldbackground="white", foreground="#0D47A1", font=("Segoe UI", 12))
        style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=6, background="#1976D2", foreground="white")
        style.map("TButton", background=[("active", "#1565C0")], foreground=[("active", "white")])
        style.configure("Treeview", font=("Segoe UI", 11), rowheight=28,
                        background="white", foreground="#0D47A1", fieldbackground="white")
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#1565C0", foreground="white")

    def _criar_widgets(self):
        frame_top = tk.Frame(self.master, bg="#0D47A1")
        frame_top.pack(pady=20)

        ttk.Label(frame_top, text="💙 CRUZEIRO ESPORTE CLUBE 💙",
                  font=("Segoe UI", 22, "bold"), background="#0D47A1", foreground="white").pack(pady=5)
        ttk.Label(frame_top, text="⭐ Controle de Estoque Oficial ⭐",
                  font=("Segoe UI", 14, "italic"), background="#0D47A1", foreground="white").pack(pady=(0, 15))

        ttk.Label(self.master, text="Nome do Produto:").pack(pady=(10, 5))
        self.entrada_nome = ttk.Entry(self.master, width=40)
        self.entrada_nome.pack(pady=5)

        ttk.Label(self.master, text="Adicionar ao Estoque (Qtd):").pack(pady=(10, 5))
        self.entrada_estoque_inicial = ttk.Entry(self.master, width=20)
        self.entrada_estoque_inicial.pack(pady=5)

        ttk.Label(self.master, text="Vendidas:").pack(pady=(10, 5))
        self.entrada_vendidas = ttk.Entry(self.master, width=20)
        self.entrada_vendidas.pack(pady=5)

        ttk.Button(self.master, text="📊 Calcular / Atualizar Estoque", command=self.calcular).pack(pady=15)

        ttk.Separator(self.master, orient="horizontal").pack(fill="x", pady=10)

        self.resultado = tk.StringVar()
        ttk.Label(self.master, textvariable=self.resultado, font=("Consolas", 12, "bold"),
                  justify="left", background="#0D47A1", foreground="white").pack(pady=10)

        frame_botoes = ttk.Frame(self.master, style="TFrame", padding=10)
        frame_botoes.pack(pady=10)

        ttk.Button(frame_botoes, text="💰 Realizar Venda", command=self.realizar_venda).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botoes, text="✏️ Editar Estoque", command=self.editar_estoque).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botoes, text="🗑️ Remover Produto", command=self.remover_produto).grid(row=0, column=2, padx=5)
        ttk.Button(frame_botoes, text="🧹 Limpar Campos", command=self.limpar).grid(row=0, column=3, padx=5)
        ttk.Button(frame_botoes, text="❌ Fechar Sistema (Esc)", command=self.sair_tela_cheia).grid(row=0, column=4, padx=5)

        ttk.Separator(self.master, orient="horizontal").pack(fill="x", pady=10)

        ttk.Label(self.master, text="📋 Produtos no Estoque:", font=("Segoe UI", 14, "bold")).pack(pady=(10, 5))
        colunas = ("produto", "estoque_inicial", "vendidas", "estoque_atual")
        self.tree = ttk.Treeview(self.master, columns=colunas, show="headings", height=15)
        for col in colunas:
            self.tree.heading(col, text=col.replace("_", " ").title())
        self.tree.column("produto", width=400)
        self.tree.column("estoque_inicial", width=150, anchor="center")
        self.tree.column("vendidas", width=150, anchor="center")
        self.tree.column("estoque_atual", width=150, anchor="center")
        self.tree.pack(pady=10, expand=True)

        ttk.Label(self.master, text="💙 Cruzeiro Esporte Clube - 5 Estrelas de Minas ⭐⭐⭐⭐⭐",
                  font=("Segoe UI", 11, "italic"), background="#0D47A1", foreground="white").pack(pady=20)

    # ===================== FUNÇÕES PRINCIPAIS =====================

    def calcular(self):
        nome_produto = self.entrada_nome.get().strip()
        entrada_estoque = self.entrada_estoque_inicial.get().strip()
        vendidas = self.entrada_vendidas.get().strip()

        if not nome_produto:
            messagebox.showwarning("Aviso", "Digite o nome do produto.")
            return

        try:
            entrada_estoque = int(entrada_estoque) if entrada_estoque else 0
            vendidas = int(vendidas) if vendidas else 0

            if entrada_estoque < 0 or vendidas < 0:
                messagebox.showerror("Erro", "As quantidades não podem ser negativas.")
                return

            for i, (produto, estoque_inicial, total_vendidas, estoque_atual) in enumerate(self.produtos):
                if produto.lower() == nome_produto.lower():
                    novo_estoque_atual = estoque_atual + entrada_estoque - vendidas
                    if novo_estoque_atual < 0:
                        messagebox.showerror("Erro", f"Estoque insuficiente para vender {vendidas} unidades de '{produto}'.")
                        return
                    self.produtos[i] = (produto, estoque_inicial + entrada_estoque,
                                        total_vendidas + vendidas, novo_estoque_atual)
                    break
            else:
                if entrada_estoque == 0:
                    messagebox.showerror("Erro", "Para novo produto, o estoque inicial deve ser maior que zero.")
                    return
                estoque_atual = entrada_estoque - vendidas
                if estoque_atual < 0:
                    messagebox.showerror("Erro", "Não é possível vender mais do que o estoque inicial.")
                    return
                self.produtos.append((nome_produto, entrada_estoque, vendidas, estoque_atual))

            self._atualizar_tabela()
            self._mostrar_resultado(nome_produto)

        except ValueError:
            messagebox.showerror("Erro", "Digite apenas números válidos!")

    def realizar_venda(self):
        """Abre janela para vender produtos do estoque"""
        if not self.produtos:
            messagebox.showwarning("Aviso", "Nenhum produto cadastrado.")
            return

        janela_venda = tk.Toplevel(self.master)
        janela_venda.title("💰 Realizar Venda")
        janela_venda.geometry("400x300")
        janela_venda.configure(bg="#1565C0")

        ttk.Label(janela_venda, text="Selecione o Produto:", background="#1565C0", foreground="white",
                  font=("Segoe UI", 12, "bold")).pack(pady=10)

        produtos_nomes = [p[0] for p in self.produtos]
        produto_var = tk.StringVar(value=produtos_nomes[0])
        combo = ttk.Combobox(janela_venda, values=produtos_nomes, textvariable=produto_var, state="readonly")
        combo.pack(pady=10)

        ttk.Label(janela_venda, text="Quantidade Vendida:", background="#1565C0", foreground="white",
                  font=("Segoe UI", 12, "bold")).pack(pady=10)
        entrada_qtd = ttk.Entry(janela_venda)
        entrada_qtd.pack(pady=10)

        def confirmar_venda():
            nome = produto_var.get()
            try:
                qtd_vendida = int(entrada_qtd.get())
                if qtd_vendida <= 0:
                    messagebox.showwarning("Aviso", "Quantidade inválida.")
                    return

                for i, (produto, inicial, vendidas, atual) in enumerate(self.produtos):
                    if produto == nome:
                        if qtd_vendida > atual:
                            messagebox.showerror("Erro", f"Estoque insuficiente! Apenas {atual} unidades disponíveis.")
                            return
                        self.produtos[i] = (produto, inicial, vendidas + qtd_vendida, atual - qtd_vendida)
                        messagebox.showinfo("Venda Realizada", f"✅ Venda registrada!\n\nProduto: {nome}\nVendidas: {qtd_vendida}\nEstoque Restante: {atual - qtd_vendida}")
                        self._atualizar_tabela()
                        self._mostrar_resultado(nome)
                        janela_venda.destroy()
                        return
            except ValueError:
                messagebox.showerror("Erro", "Digite um número válido para a quantidade.")

        ttk.Button(janela_venda, text="Confirmar Venda ✅", command=confirmar_venda).pack(pady=20)

    def editar_estoque(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Aviso", "Selecione um produto para editar o estoque.")
            return
        valores = self.tree.item(item, "values")
        nome = valores[0]
        novo_valor = simpledialog.askinteger("Editar Estoque",
                                             f"Digite o novo estoque atual para '{nome}':",
                                             minvalue=0)
        if novo_valor is None:
            return
        for i, (produto, inicial, vendidas, atual) in enumerate(self.produtos):
            if produto == nome:
                diferenca = novo_valor - atual
                self.produtos[i] = (produto, inicial + max(0, diferenca), vendidas, novo_valor)
                self._atualizar_tabela()
                self._mostrar_resultado(nome)
                messagebox.showinfo("Sucesso", f"Estoque de '{nome}' atualizado para {novo_valor} unidades.")
                break

    def _mostrar_resultado(self, produto_nome):
        for p in self.produtos:
            if p[0].lower() == produto_nome.lower():
                nome, inicial, vendidas, atual = p
                porcentagem_vendida = (vendidas / inicial) * 100 if inicial else 0
                porcentagem_estoque = 100 - porcentagem_vendida
                self.resultado.set(
                    f"⭐ Produto: {nome}\n"
                    f"🧾 Total Recebido: {inicial}\n"
                    f"💰 Total Vendidas: {vendidas}\n"
                    f"📦 Estoque Atual: {atual}\n"
                    f"📊 Vendido: {porcentagem_vendida:.2f}%\n"
                    f"📈 Restante: {porcentagem_estoque:.2f}%"
                )
                break

    def _atualizar_tabela(self):
        self.tree.delete(*self.tree.get_children())
        for p in self.produtos:
            self.tree.insert("", tk.END, values=p)

    def limpar(self):
        self.entrada_nome.delete(0, tk.END)
        self.entrada_estoque_inicial.delete(0, tk.END)
        self.entrada_vendidas.delete(0, tk.END)
        self.resultado.set("")

    def remover_produto(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Aviso", "Selecione um produto para remover.")
            return
        valores = self.tree.item(item, "values")
        nome = valores[0]
        if messagebox.askyesno("Confirmação", f"Tem certeza que deseja remover '{nome}' do estoque?"):
            self.produtos = [p for p in self.produtos if p[0] != nome]
            self._atualizar_tabela()
            self.resultado.set("")
            messagebox.showinfo("Removido", f"O produto '{nome}' foi removido com sucesso.")

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = ControleEstoqueApp(root)
    root.mainloop()

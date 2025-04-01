from tkinter import *
import mysql.connector
import sqlite3

class Application:
    def __init__(self, master=None):
        self.layout = master
        self.layout.title("Pharma Storage")
        self.layout.geometry("300x150")

        self.tela = Frame(self.layout)
        self.tela.pack(pady=10)

        self.descricao = Label(self.tela, text="Digite seu Login e sua senha")
        self.descricao.pack()

        self.login_label = Label(self.tela, text="Login:")
        self.login_label.pack()
        self.login_entry = Entry(self.tela)
        self.login_entry.pack()

        self.senha_label = Label(self.tela, text="Senha:")
        self.senha_label.pack()
        self.senha_entry = Entry(self.tela, show="*")
        self.senha_entry.pack()

        self.botao_verificar = Button(self.tela, text="Verificar", command=self.verificar_login)
        self.botao_verificar.pack()

        self.mensagem = Label(self.tela, text="")
        self.mensagem.pack()

    def verificar_login(self):
        login = self.login_entry.get()
        senha = self.senha_entry.get()

        conexao = sqlite3.connect("farmacia.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE login=? AND senha=?", (login, senha))
        resultado = cursor.fetchone()

        if resultado:
            self.mensagem.config(text="Login bem-sucedido!")
            self.abrir_nova_tela() # Chama a função para abrir a nova tela
        else:
            self.mensagem.config(text="Login ou senha incorretos.")

        conexao.close()

    def abrir_nova_tela(self):
        # Destrói a tela de login
        self.tela.destroy()

        # Cria uma nova tela
        self.nova_tela = Frame(self.layout)
        self.nova_tela.pack(pady=10)

        # Adiciona widgets à nova tela
        Label(self.nova_tela, text="Bem-vindo à nova tela!").pack()
        Button(self.nova_tela, text="Sair", command=self.sair).pack()

    def sair(self):
        # Fecha a aplicação
        self.layout.destroy()

root = Tk()
Application(root)
root.mainloop()

class Application:
    def __init__(self, master=None):
        self.layout = master
        self.layout.title("Pharma Storage")
        self.layout.geometry("300x150")

        self.tela = Frame(self.layout)
        self.tela.pack(pady=10)

        self.descricao = Label(self.tela, text="Dados do Banco de Dados")
        self.descricao.pack()

        self.exibir_dados()

    def exibir_dados(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="toor",
                database="controle_estoque"
            )
            cursor = conexao.cursor()

            cursor.execute("SELECT * FROM produtos") # Substitua 'produtos' pelo nome da sua tabela
            resultados = cursor.fetchall()

            for linha in resultados:
                Label(self.tela, text=str(linha)).pack()

            cursor.close()
            conexao.close()
        except mysql.connector.Error as err:
            Label(self.tela, text=f"Erro: {err}").pack() # Mostra o erro na interface caso ocorra

root = Tk()
Application(root)
root.mainloop()
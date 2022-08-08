from tkinter import *
from tkinter import ttk

from aluno import Aluno


class AlunoAppLista:

    # titulo padrão da minha interface
    titulo = 'Lista de Alunos'

    # fonte padrão dos elementos da interface
    font = ('Verdana', 14)

    width = 10

    anchor = W

    def __init__(self, master=None):

        # armazenei em um atributo o container principal
        self.master = master

        self.master.title(AlunoAppLista.titulo)

        # criação do frame central para apresentar em tela os componentes, dentro do container principal
        # frame_master espaço vazio
        self.frame_master = Frame(self.master)
        self.frame_master.pack()

        # apresentar o titulo da interface
        # Segmentando as areas da interfca utiziando o container frame
        # frame do titulo
        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=AlunoAppLista.titulo,
            font=('Verdana', 30, 'bold')
        )

        self.label_titulo.pack()

        # criando o frame para a lista(espaço vazio)

        self.frame_lista = Frame(
            self.frame_master
        )

        self.frame_lista.pack()

        # criando o widget da lista

        self.lista = ttk.Treeview(self.frame_lista)

        self.lista.pack()

        # declarando as colunas

        self.lista['columns'] = (
            'Matricula', 'Nome', 'CPF', 'E-mail', 'Telefone')

        self.lista.column("#0", width=0,  stretch=NO)
        self.lista.column("Matricula", anchor=CENTER, width=80)
        self.lista.column("Nome", anchor=CENTER, width=80)
        self.lista.column("CPF", anchor=CENTER, width=80)
        self.lista.column("E-mail", anchor=CENTER, width=80)
        self.lista.column("Telefone", anchor=CENTER, width=80)

        # Criando o cabeçalho da lista
        self.lista.heading("#0", text="", anchor=CENTER)
        self.lista.heading("Matricula", text="Matricula", anchor=CENTER)
        self.lista.heading("Nome", text="Nome", anchor=CENTER)
        self.lista.heading("CPF", text="CPF", anchor=CENTER)
        self.lista.heading("E-mail", text="E-mail", anchor=CENTER)
        self.lista.heading("Telefone", text="Telefone", anchor=CENTER)

        # usando o metodo de classe listar
        # para listar os alunos

        self.listar()

    def listar(self):

        lista_alunos = Aluno.listar()

        for aluno in lista_alunos:

            # fazendo o loop das linhas da tabela, com os dados vindo do banco de dados

            self.lista.insert(parent='', index='end', text='', values=(
                aluno[0], aluno[1], aluno[2], aluno[3], aluno[4]))


if __name__ == '__main__':

    root = Tk()

    AlunoAppLista(root)

    root.mainloop()

    # print(Aluno.listar())

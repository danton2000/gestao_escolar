# imporatado tkinter que tem o ttk
from tkinter import *
# Treeview é um metodo do ttk
from tkinter.ttk import Treeview

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
        # Frame que ela vai estar, modulo de exibição, as colunas que ela vai ter, como ela vai ser exibida
        self.lista = Treeview(
            self.frame_lista,
            selectmode="browse",
            column=(
                "matricula",
                "nome",
                "cpf",
                "telefone",
                "email"
            ),
            show="headings",
        )

        # declarando as colunas
        # Criando o cabeçalho da lista
        # Stretch = è o arrasta do cabeçalho da tabela
        self.lista.column(
            "matricula",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#1",
            text="Matricula"
        )

        self.lista.column(
            "nome",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#2",
            text="Nome"
        )

        self.lista.column(
            "cpf",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )
        self.lista.heading(
            "#3",
            text="CPF"
        )
        self.lista.column(
            "telefone",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )
        self.lista.heading(
            "#4",
            text="Telefone"
        )

        self.lista.column(
            "email",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#5",
            text="Email"
        )
        

        # 'Apresentar' tabela
        self.lista.pack()

        # usando o metodo de classe listar
        # para listar os alunos

        self.listar()

    def listar(self):

        lista_alunos = Aluno.listar()

        for aluno in lista_alunos:

            # fazendo o loop das linhas da tabela, com os dados vindo do banco de dados

            self.lista.insert(
                "",
                END,
                values=(
                    aluno[0],
                    aluno[1],
                    aluno[2],
                    aluno[3],
                    aluno[4]
                )
            )


if __name__ == '__main__':

    root = Tk()

    AlunoAppLista(root)

    root.mainloop()

    # print(Aluno.listar())

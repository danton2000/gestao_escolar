from tkinter import *

from tkinter.ttk import Treeview

from professor import Professor


class ProfessorAppLista:

    titulo = 'Lista de Professor'

    font = ('Verdana', 14)

    def __init__(self, master=None):

        self.master = master

        self.master.title(ProfessorAppLista.titulo)

        self.frame_master = Frame(self.master)

        self.frame_master.pack()

        self.frame_titulo = Frame(self.frame_master)

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=ProfessorAppLista.titulo,
            font=('Verdana', 30, 'bold')
        )

        self.label_titulo.pack()

        self.frame_lista = Frame(self.frame_master)

        self.frame_lista.pack()

        self.lista = Treeview(
            self.frame_lista,
            selectmode="browse",
            column=(
                "matricula",
                "nome",
                "cpf",
                "telefone",
                "email",
                "ativo",
                "formacao",
                "especialidade"
            ),
            show="headings",
        )

        # Matricula
        self.lista.column(
            "matricula",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#1",
            text="Matricula"
        )

        # Nome
        self.lista.column(
            "nome",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#2",
            text="Nome"
        )

        # CPF
        self.lista.column(
            "cpf",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#3",
            text="CPF"
        )

        # Telefone
        self.lista.column(
            "telefone",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#4",
            text="Telefone"
        )

        # E-mail
        self.lista.column(
            "email",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#5",
            text="Email"
        )

        # Ativo
        self.lista.column(
            "ativo",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#6",
            text="Ativo"
        )

        # Formação
        self.lista.column(
            "formacao",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#7",
            text="Formação"
        )

        # Especialide
        self.lista.column(
            "especialidade",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#8",
            text="Especialide"
        )

        self.lista.pack()

        self.listar()

    def listar(self):

        lista_professores = Professor.listar()

        for professor in lista_professores:
            
            # if professor[5] == 1:

            #     professor_status = 'Ativo'

            # else:

            #     professor_status = 'Inativo'

            professor_status = "Ativo" if professor[5] == 1 else "Inativo"

            self.lista.insert(
                "",
                END,
                values=(
                    professor[0],
                    professor[1],
                    professor[2],
                    professor[3],
                    professor[4],
                    professor_status,
                    professor[6],
                    professor[7]
                )
            )


if __name__ == '__main__':

    root = Tk()

    ProfessorAppLista(root)

    root.mainloop()

from tkinter import *

from tkinter.ttk import Treeview

from curso import Curso


class CursoAppLista:

    titulo = "Lista de Cursos"

    font = ('Verdana', 14)

    def __init__(self, master=None):

        self.master = master

        self.master.title(CursoAppLista.titulo)

        self.frame_master = Frame(self.master)

        self.frame_master.pack()

        self.frame_titulo = Frame(self.frame_master)

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=CursoAppLista.titulo,
            font=('Verdana', 30, 'bold')
        )

        self.label_titulo.pack()

        self.frame_lista = Frame(self.frame_master)

        self.frame_lista.pack()

        self.lista = Treeview(
            self.frame_lista,
            selectmode="browse",
            column=(
                "codigo",
                "nome",
                "classificacao",
                "ativo",
                "descricao"
            ),
            show="headings",
        )

        # Código
        self.lista.column(
            "codigo",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#1",
            text="Código"
        )

        # Nome
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

        # Classifacação
        self.lista.column(
            "classificacao",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#3",
            text="Classificação"
        )

        # ativo
        self.lista.column(
            "ativo",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#4",
            text="Ativo"
        )

        # classificacao
        self.lista.column(
            "classificacao",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#5",
            text="Classificação"
        )

        self.lista.pack()

        self.listar()

    def listar(self):

        lista_cursos = Curso.listar()

        for curso in lista_cursos:

            # if professor[5] == 1:

            #     professor_status = 'Ativo'

            # else:

            #     professor_status = 'Inativo'

            curso_status = "Ativo" if curso[3] == 1 else "Inativo"

            self.lista.insert(
                "",
                END,
                values=(
                    curso[0],
                    curso[1],
                    curso[2],
                    curso_status,
                    curso[4]

                )
            )


if __name__ == '__main__':

    root = Tk()

    CursoAppLista(root)

    root.mainloop()

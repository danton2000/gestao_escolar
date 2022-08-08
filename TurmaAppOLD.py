from tkinter import *
from tkinter import ttk


class TurmaApp:

    # titulo padrão da minha interface
    titulo = 'Formulário de Turma'

    lista = [(1, 'Python'), (2, 'Python')]

    dict = dict(lista)

    # fonte padrão dos elementos da interface
    font = ('Verdana', 14)

    def __init__(self, master=None):

        self.master = master

        self.master.title(TurmaApp.titulo)

        self.frame_master = Frame(self.master)

        self.frame_master.pack()

        self.frame_titulo = Frame(self.frame_master)

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=TurmaApp.titulo,
            font=(
                'Verdana',
                30,
                'bold'
            )
        )

        self.label_titulo.pack()

        # criando um frame, para a area do cursor
        # para selecionar o curso para a turma

        self.frame_curso = Frame(self.frame_master)

        self.frame_curso.pack()

        self.var_person = StringVar()
        self.select_curso = ttk.Combobox(
            self.frame_curso,
            values=list(
                TurmaApp.dict.items[0]
            ),
            textvariable=self.var_person
        )

        self.select_curso.pack()

        self.frame_ferramenta_curso = Frame(self.frame_master)

        self.frame_ferramenta_curso.pack

        self.button_curso = Button(
            root, text='Selecionar', command=self.pegandoCurso)

        self.button_curso.pack()

    def pegandoCurso(self):

        key = self.var_person.get()

        print(key[0])

        try:  # To bypass the error when user chooses nothing
            # get the corresponding value from the given key
            value = TurmaApp.dict[key]
            print(value)  # print it
        except KeyError:
            print('Please choose an option')  # error message


if __name__ == '__main__':

    root = Tk()

    TurmaApp(root)

    root.mainloop()

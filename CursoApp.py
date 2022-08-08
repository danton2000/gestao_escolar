from tkinter import *

from curso import Curso

# wapper é uma classe, os componentes são atributos dela


class CursoApp:
    """
        Classe empacotadora wapper para armazenar todo os componentes da interface de Alunos
    """
    # titulo padrão da minha interface
    titulo = 'Formulário de Aluno'

    # fonte padrão dos elementos da interface
    font = ('Verdana', 14)

    width = 10

    anchor = W

    # passando container princiapal
    def __init__(self, master=None):
        """
            construtor do wapper
            Local para declararmos os componentes da interface
        """
        # armazenei em um atributo o container principal
        self.master = master

        self.master.title(CursoApp.titulo)

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
            text=CursoApp.titulo,
            font=('Verdana', 30, 'bold')
        )
        self.label_titulo.pack()

        # formulário do aluno
        # segmentei a area do formulario

        self.frame_formulario = Frame(
            self.frame_master
        )

        self.frame_formulario.pack()

        # Matricula
        # self.label_matricula = Label(
        #     self.frame_formulario,
        #     text='Matricula:',
        #     font=CursoApp.font,
        #     width=width
        # )

        # self.label_matricula.grid(
        #     row=0,
        #     column=0
        # )

        # self.entry_matricula = Entry(
        #     self.frame_formulario,
        #     font=CursoApp.font,
        # )

        # Nome
        self.label_nome = Label(
            self.frame_formulario,
            text='Nome:',
            font=CursoApp.font,
            width=CursoApp.width,
            anchor=CursoApp.anchor
        )

        self.label_nome.grid(
            row=0,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=CursoApp.font
        )

        self.entry_nome.grid(
            row=0,
            column=1
        )

        # Classificação
        self.label_classificacao = Label(
            self.frame_formulario,
            text='classificacao:',
            font=CursoApp.font,
            width=CursoApp.width,
            anchor=CursoApp.anchor
        )

        self.label_classificacao.grid(
            row=1,
            column=0
        )

        self.entry_classificacao = Entry(
            self.frame_formulario,
            font=CursoApp.font,
        )

        self.entry_classificacao.grid(
            row=1,
            column=1
        )

        # Descrição
        self.label_descricao = Label(
            self.frame_formulario,
            text='Descrição:',
            font=CursoApp.font,
            width=CursoApp.width,
            anchor=CursoApp.anchor
        )

        self.label_descricao.grid(
            row=2,
            column=0
        )

        self.entry_descricao = Entry(
            self.frame_formulario,
            font=CursoApp.font,
        )

        self.entry_descricao.grid(
            row=2,
            column=1
        )

        # Área de ferramentas
        self.frame_ferramentas = Frame(
            self.frame_master
        )

        self.frame_ferramentas.pack(
            fill=X
        )

        # Botão de salvar
        self.button_salvar = Button(
            self.frame_ferramentas,
            text='Salvar',
            font=CursoApp.font,
            background='Blue',
            foreground='White',
            command=self.salvar
        )

        self.button_salvar.pack(
            side=RIGHT
        )

        # Botão de fechar
        self.button_fechar = Button(
            self.frame_ferramentas,
            text='Fechar',
            font=CursoApp.font,
            background='Black',
            foreground='White',
            command=self.master.quit
        )

        self.button_fechar.pack(side=LEFT)

        # Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=CursoApp.font
        )

        self.label_mensagem.pack()

    def salvar(self):
        # remove o valor do entry
        # self.entry_matricula.delete(0, END)

        nome = self.entry_nome.get()

        classificacao = self.entry_classificacao.get()

        descricao = self.entry_descricao.get()

        if nome and classificacao != "":
            try:
                curso = Curso(
                    nome=nome,
                    classificacao=classificacao,
                    descricao=descricao
                )

                # self.entry_matricula.insert(0, aluno.matricula)

                # self.entry_matricula.grid(
                #     row=0,
                #     column=1
                # )
                self.entry_nome.delete(0, END)
                self.entry_nome.focus()
                self.entry_classificacao.delete(0, END)
                self.entry_descricao.delete(0, END)

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f"Aluno {curso.codigo} - {curso.nome} cadastrado !"

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err
        else:
            self.label_mensagem['foreground'] = 'Red'
            self.label_mensagem['text'] = 'Dados incorretos !'


# tecnica de teste
if __name__ == '__main__':

    root = Tk()

    CursoApp(root)

    root.mainloop()

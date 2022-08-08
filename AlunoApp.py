from tkinter import *

from aluno import Aluno

# wapper é uma classe, os componentes são atributos dela
class AlunoApp:
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

        self.master.title(AlunoApp.titulo)

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
            text=AlunoApp.titulo,
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
        #     font=AlunoApp.font,
        #     width=width
        # )

        # self.label_matricula.grid(
        #     row=0,
        #     column=0
        # )

        # self.entry_matricula = Entry(
        #     self.frame_formulario,
        #     font=AlunoApp.font,
        # )

        # Nome
        self.label_nome = Label(
            self.frame_formulario,
            text='Nome:',
            font=AlunoApp.font,
            width=AlunoApp.width,
            anchor=AlunoApp.anchor
        )

        self.label_nome.grid(
            row=0,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=AlunoApp.font
        )

        self.entry_nome.grid(
            row=0,
            column=1
        )

        # CPF
        self.label_cpf = Label(
            self.frame_formulario,
            text='CPF:',
            font=AlunoApp.font,
            width=AlunoApp.width,
            anchor=AlunoApp.anchor
        )

        self.label_cpf.grid(
            row=1,
            column=0
        )

        self.entry_cpf = Entry(
            self.frame_formulario,
            font=AlunoApp.font,
        )

        self.entry_cpf.grid(
            row=1,
            column=1
        )

        # E-mail
        self.label_email = Label(
            self.frame_formulario,
            text='E-mail:',
            font=AlunoApp.font,
            width=AlunoApp.width,
            anchor=AlunoApp.anchor
        )

        self.label_email.grid(
            row=2,
            column=0
        )

        self.entry_email = Entry(
            self.frame_formulario,
            font=AlunoApp.font,
        )

        self.entry_email.grid(
            row=2,
            column=1
        )

        # Telefone
        self.label_telefone = Label(
            self.frame_formulario,
            text='Telefone:',
            font=AlunoApp.font,
            width=AlunoApp.width,
            anchor=AlunoApp.anchor
        )

        self.label_telefone.grid(
            row=3,
            column=0
        )

        self.entry_telefone = Entry(
            self.frame_formulario,
            font=AlunoApp.font,
        )

        self.entry_telefone.grid(
            row=3,
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
            font=AlunoApp.font,
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
            font=AlunoApp.font,
            background='Black',
            foreground='White',
            command=self.master.quit
        )

        self.button_fechar.pack(side=LEFT)

        # Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=AlunoApp.font
        )

        self.label_mensagem.pack()

    def salvar(self):
        # remove o valor do entry
        # self.entry_matricula.delete(0, END)

        nome = self.entry_nome.get()

        cpf = self.entry_cpf.get()

        email = self.entry_email.get()

        telefone = self.entry_telefone.get()

        if nome and cpf and email and telefone != "":
            try:
                aluno = Aluno(
                    nome=nome,
                    cpf=cpf,
                    email=email,
                    telefone=telefone
                )

                # self.entry_matricula.insert(0, aluno.matricula)

                # self.entry_matricula.grid(
                #     row=0,
                #     column=1
                # )
                self.entry_nome.delete(0, END)
                self.entry_nome.focus()

                self.entry_cpf.delete(0, END)
                self.entry_email.delete(0, END)
                self.entry_telefone.delete(0, END)

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f"Aluno {aluno.matricula} - {aluno.nome} cadastrado !"

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err
        else:
            self.label_mensagem['foreground'] = 'Red'
            self.label_mensagem['text'] = 'Dados incorretos !'


# tecnica de teste
if __name__ == '__main__':

    root = Tk()

    AlunoApp(root)

    root.mainloop()

from tkinter import *

from professor import Professor

class ProfessorApp:

    # titulo padrão da minha interface
    titulo = 'Formulário de Professor'

    # fonte padrão dos elementos da interface
    font = ('Verdana', 14)

    # largura padrão
    width = 12

    #ancora padrão 
    anchor = W

    def __init__(self, master=None):
        """
            construtor do wapper
            Local para declararmos os componentes da interface
        """
        # armazenei em um atributo o container principal
        self.master = master

        self.master.title(ProfessorApp.titulo)

        # criação do frame central para apresentar em tela os componentes, dentro do container principal
        self.frame_master = Frame(self.master)
        self.frame_master.pack()

        # frame do titulo
        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=ProfessorApp.titulo,
            font=('Verdana', 30, 'bold')
        )
        self.label_titulo.pack()

        # Frame Formulário
        self.frame_formulario = Frame(
            self.frame_master
        )

        self.frame_formulario.pack()

        # Nome
        self.label_nome = Label(
            self.frame_formulario,
            text='Nome:',
            font=ProfessorApp.font,
            width=ProfessorApp.width,
            anchor=ProfessorApp.anchor
        )

        self.label_nome.grid(
            row=0,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_nome.grid(
            row=0,
            column=1
        )

        # CPF
        self.label_cpf = Label(
            self.frame_formulario,
            text='CPF:',
            font=ProfessorApp.font,
            width=ProfessorApp.width,
            anchor=ProfessorApp.anchor
        )

        self.label_cpf.grid(
            row=1,
            column=0
        )

        self.entry_cpf = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_cpf.grid(
            row=1,
            column=1
        )

        # E-mail
        self.label_email = Label(
            self.frame_formulario,
            text='E-mail:',
            font=ProfessorApp.font,
            width=ProfessorApp.width,
            anchor=ProfessorApp.anchor
        )

        self.label_email.grid(
            row=2,
            column=0
        )

        self.entry_email = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_email.grid(
            row=2,
            column=1
        )

        # Telefone
        self.label_telefone = Label(
            self.frame_formulario,
            text='Telefone:',
            font=ProfessorApp.font,
            width=ProfessorApp.width,
            anchor=ProfessorApp.anchor
        )

        self.label_telefone.grid(
            row=3,
            column=0
        )

        self.entry_telefone = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_telefone.grid(
            row=3,
            column=1
        )

        # Formação
        self.label_formacao = Label(
            self.frame_formulario,
            text='Formação:',
            font=ProfessorApp.font,
            width=ProfessorApp.width,
            anchor=ProfessorApp.anchor
        )

        self.label_formacao.grid(
            row=4,
            column=0
        )

        self.entry_formacao = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_formacao.grid(
            row=4,
            column=1
        )

        # Especialidade
        self.label_especialidade = Label(
            self.frame_formulario,
            text='Especialidade:',
            font=ProfessorApp.font,
            width=ProfessorApp.width,
            anchor=ProfessorApp.anchor
        )

        self.label_especialidade.grid(
            row=5,
            column=0
        )

        self.entry_especialidade = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_especialidade.grid(
            row=5,
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
            font=ProfessorApp.font,
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
            font=ProfessorApp.font,
            background='Black',
            foreground='White',
            command=self.master.quit
        )

        self.button_fechar.pack(side=LEFT)

        # Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=ProfessorApp.font
        )

        self.label_mensagem.pack()

    def salvar(self):

        nome = self.entry_nome.get()

        cpf = self.entry_cpf.get()

        email = self.entry_email.get()

        telefone = self.entry_telefone.get()

        formacao = self.entry_formacao.get()

        especialidade = self.entry_especialidade.get()

        if nome and cpf != "":
            try:
                professor = Professor(

                    nome=nome,
                    cpf=cpf,
                    email=email,
                    telefone=telefone,
                    formacao=formacao,
                    especialidade=especialidade
                )

                # remove o valor do entry
                self.entry_nome.delete(0, END)
                
                # foca um entry
                self.entry_nome.focus()

                self.entry_cpf.delete(0, END)
                self.entry_email.delete(0, END)
                self.entry_telefone.delete(0, END)
                self.entry_formacao.delete(0, END)
                self.entry_especialidade.delete(0, END)

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f"Professor {professor.matricula} - {professor.nome} cadastrado !"

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err
        else:
            self.label_mensagem['foreground'] = 'Red'
            self.label_mensagem['text'] = 'Dados incorretos !'


if __name__ == '__main__':

    root = Tk()

    ProfessorApp(root)

    root.mainloop()

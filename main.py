#PEGANDO AS CLASSES
from turma import Turma
from aluno import Aluno

#turma precisa dos alunos
python_caldeira = Turma('Noite', '2022-07-01', '2022-07-31')

print(python_caldeira)

joao = Aluno(nome = 'João', cpf = 1, email = 'joao@')

maria = Aluno(nome = 'Maria', cpf = 2, email = 'maria@')

python_caldeira.adicionar_aluno(joao)

python_caldeira.adicionar_aluno(maria)

for aluno in python_caldeira.retorna_alunos():

    print(aluno)
SELECT Alunos.matricula, Alunos.nome AS Alunos_Nome , Turmas_Alunos.codigo_turma, Turmas.periodo, Cursos.nome AS Cursos_Nome
FROM Alunos
INNER JOIN Turmas_Alunos ON Alunos.matricula = Turmas_Alunos.matricula_aluno
INNER JOIN Turmas ON Turmas_Alunos.codigo_turma = Turmas.codigo
INNER JOIN Cursos ON Turmas.codigo_curso = Cursos.codigo

WHERE Alunos.nome = 'João'
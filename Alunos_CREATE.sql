CREATE TABLE IF NOT EXISTS Alunos (
    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR (255) NOT NULL,
    cpf CHAR (11) NOT NULL,
    telefone CHAR (11),
    email VARCHAR (255) NOT NULL
);

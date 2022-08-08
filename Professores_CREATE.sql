CREATE TABLE IF NOT EXISTS Professores (

    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    
    nome VARCHAR(255) NOT NULL,
    
    cpf CHAR(11) NOT NULL,
    
    telefone CHAR(11),
    
    email VARCHAR(255),
    
    ativo BOOLEAN,
    
    formacao VARCHAR(255),
    
    especialidade VARCHAR(255) 

)
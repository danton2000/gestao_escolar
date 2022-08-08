CREATE TABLE IF NOT EXISTS Cursos(

    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    
    nome VARCHAR(255) NOT NULL,
    
    classificacao VARCHAR(255) NOT NULL,
    
    ativo BOOLEAN NOT NULL,
    
    descricao VARCHAR(255)

)
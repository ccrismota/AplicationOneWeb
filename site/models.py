import sqlite3 as sql

conn = sql.connect('database.db')
print("Banco aberto com sucesso!")

conn.execute("""CREATE TABLE dados_usuario ( 
    nome_completo TEXT NOT NULL,  
    email TEXT NOT NULL,
    pais TEXT NOT NULL,
    estado TEXT NOT NULL,
    municipio TEXT NOT NULL,
    cep TEXT NOT NULL,
    rua TEXT NOT NULL,
    numero TEXT NOT NULL,
    complemento TEXT NOT NULL,
    cpf TEXT NOT NULL,
    pis TEXT NOT NULL,
    senha TEXT NOT NULL
)""");

print('Tabela criada com sucesso!!!')

conn.close()
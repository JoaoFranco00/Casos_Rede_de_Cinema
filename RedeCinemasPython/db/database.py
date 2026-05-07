import sqlite3

DB_PATH = "cinema.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    _criar_tabelas(conn)
    return conn

def _criar_tabelas(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS cinemas (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            nome     TEXT NOT NULL,
            endereco TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS generos (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS diretores (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            nome         TEXT NOT NULL,
            nacionalidade TEXT
        );

        CREATE TABLE IF NOT EXISTS atores (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            nome         TEXT NOT NULL,
            nacionalidade TEXT
        );

        CREATE TABLE IF NOT EXISTS filmes (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo      TEXT NOT NULL,
            duracao_min INTEGER NOT NULL,
            sinopse     TEXT
        );

        CREATE TABLE IF NOT EXISTS filme_genero (
            filme_id  INTEGER REFERENCES filmes(id),
            genero_id INTEGER REFERENCES generos(id),
            PRIMARY KEY (filme_id, genero_id)
        );

        CREATE TABLE IF NOT EXISTS filme_diretor (
            filme_id   INTEGER REFERENCES filmes(id),
            diretor_id INTEGER REFERENCES diretores(id),
            PRIMARY KEY (filme_id, diretor_id)
        );

        CREATE TABLE IF NOT EXISTS filme_ator (
            filme_id INTEGER REFERENCES filmes(id),
            ator_id  INTEGER REFERENCES atores(id),
            PRIMARY KEY (filme_id, ator_id)
        );

        CREATE TABLE IF NOT EXISTS sessoes (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            cinema_id  INTEGER NOT NULL REFERENCES cinemas(id),
            filme_id   INTEGER NOT NULL REFERENCES filmes(id),
            data_hora  TEXT NOT NULL,
            sala       TEXT NOT NULL,
            publico    INTEGER DEFAULT 0
        );
    """)
    conn.commit()

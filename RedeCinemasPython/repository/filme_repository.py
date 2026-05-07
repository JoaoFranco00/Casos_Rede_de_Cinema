from db.database import get_connection
from model.filme import Filme
from model.pessoas import Genero, Diretor, Ator


class FilmeRepository:

    def salvar(self, filme: Filme):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO filmes (titulo, duracao_min, sinopse) VALUES (?, ?, ?)",
            (filme.titulo, filme.duracao_min, filme.sinopse)
        )
        filme_id = cursor.lastrowid

        for genero in filme.generos:
            # insere genero se não existir
            cursor.execute(
                "INSERT OR IGNORE INTO generos (nome) VALUES (?)", (genero,)
            )
            cursor.execute("SELECT id FROM generos WHERE nome = ?", (genero,))
            gid = cursor.fetchone()[0]
            cursor.execute(
                "INSERT OR IGNORE INTO filme_genero (filme_id, genero_id) VALUES (?, ?)",
                (filme_id, gid)
            )

        for diretor in filme.diretores:
            cursor.execute(
                "INSERT INTO diretores (nome) VALUES (?)", (diretor,)
            )
            did = cursor.lastrowid
            cursor.execute(
                "INSERT INTO filme_diretor (filme_id, diretor_id) VALUES (?, ?)",
                (filme_id, did)
            )

        for ator in filme.atores:
            cursor.execute(
                "INSERT INTO atores (nome) VALUES (?)", (ator,)
            )
            aid = cursor.lastrowid
            cursor.execute(
                "INSERT INTO filme_ator (filme_id, ator_id) VALUES (?, ?)",
                (filme_id, aid)
            )

        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, duracao_min, sinopse FROM filmes")
        rows = cursor.fetchall()
        filmes = []
        for row in rows:
            filme = Filme(row[1], row[2], row[3], row[0])
            filme.generos = self._buscar_generos(conn, row[0])
            filme.diretores = self._buscar_diretores(conn, row[0])
            filme.atores = self._buscar_atores(conn, row[0])
            filmes.append(filme)
        conn.close()
        return filmes

    def buscar_por_id(self, filme_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, titulo, duracao_min, sinopse FROM filmes WHERE id = ?",
            (filme_id,)
        )
        row = cursor.fetchone()
        if not row:
            conn.close()
            return None
        filme = Filme(row[1], row[2], row[3], row[0])
        filme.generos = self._buscar_generos(conn, row[0])
        filme.diretores = self._buscar_diretores(conn, row[0])
        filme.atores = self._buscar_atores(conn, row[0])
        conn.close()
        return filme

    def _buscar_generos(self, conn, filme_id):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT g.nome FROM generos g
            JOIN filme_genero fg ON fg.genero_id = g.id
            WHERE fg.filme_id = ?
        """, (filme_id,))
        return [r[0] for r in cursor.fetchall()]

    def _buscar_diretores(self, conn, filme_id):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.nome FROM diretores d
            JOIN filme_diretor fd ON fd.diretor_id = d.id
            WHERE fd.filme_id = ?
        """, (filme_id,))
        return [r[0] for r in cursor.fetchall()]

    def _buscar_atores(self, conn, filme_id):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.nome FROM atores a
            JOIN filme_ator fa ON fa.ator_id = a.id
            WHERE fa.filme_id = ?
        """, (filme_id,))
        return [r[0] for r in cursor.fetchall()]

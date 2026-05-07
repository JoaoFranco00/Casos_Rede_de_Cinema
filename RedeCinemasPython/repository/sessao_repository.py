from db.database import get_connection
from model.sessao import Sessao


class SessaoRepository:

    def salvar(self, sessao: Sessao):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO sessoes (cinema_id, filme_id, data_hora, sala, publico)
               VALUES (?, ?, ?, ?, ?)""",
            (sessao.cinema_id, sessao.filme_id,
             sessao.data_hora, sessao.sala, sessao.publico)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, s.cinema_id, s.filme_id, s.data_hora, s.sala, s.publico,
                   c.nome AS cinema_nome, f.titulo AS filme_titulo
            FROM sessoes s
            JOIN cinemas c ON c.id = s.cinema_id
            JOIN filmes f ON f.id = s.filme_id
            ORDER BY s.data_hora
        """)
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_sessao(r) for r in rows]

    def buscar_por_id(self, sessao_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, s.cinema_id, s.filme_id, s.data_hora, s.sala, s.publico,
                   c.nome AS cinema_nome, f.titulo AS filme_titulo
            FROM sessoes s
            JOIN cinemas c ON c.id = s.cinema_id
            JOIN filmes f ON f.id = s.filme_id
            WHERE s.id = ?
        """, (sessao_id,))
        row = cursor.fetchone()
        conn.close()
        return self._row_to_sessao(row) if row else None

    def atualizar_publico(self, sessao_id: int, publico: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE sessoes SET publico = ? WHERE id = ?",
            (publico, sessao_id)
        )
        conn.commit()
        conn.close()

    def total_publico_por_filme(self, filme_id: int) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COALESCE(SUM(publico), 0) FROM sessoes WHERE filme_id = ?",
            (filme_id,)
        )
        total = cursor.fetchone()[0]
        conn.close()
        return total

    def total_publico_por_cinema(self, cinema_id: int) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COALESCE(SUM(publico), 0) FROM sessoes WHERE cinema_id = ?",
            (cinema_id,)
        )
        total = cursor.fetchone()[0]
        conn.close()
        return total

    def sessoes_por_cinema(self, cinema_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, s.cinema_id, s.filme_id, s.data_hora, s.sala, s.publico,
                   c.nome, f.titulo
            FROM sessoes s
            JOIN cinemas c ON c.id = s.cinema_id
            JOIN filmes f ON f.id = s.filme_id
            WHERE s.cinema_id = ?
            ORDER BY s.data_hora
        """, (cinema_id,))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_sessao(r) for r in rows]

    def _row_to_sessao(self, row):
        return Sessao(
            cinema_id=row[1], filme_id=row[2],
            data_hora=row[3], sala=row[4], publico=row[5],
            id=row[0], cinema_nome=row[6], filme_titulo=row[7]
        )

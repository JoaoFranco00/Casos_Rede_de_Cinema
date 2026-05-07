from flask import Flask, request, render_template, redirect, url_for
from controller.cinema_controller import CinemaController
from controller.filme_controller import FilmeController
from controller.sessao_controller import SessaoController


class SessaoViewWeb:

    def __init__(self):
        self.app = Flask(__name__, template_folder="../templates")
        self.cinema_ctrl = CinemaController()
        self.filme_ctrl = FilmeController()
        self.sessao_ctrl = SessaoController()
        self._registrar_rotas()

    def _registrar_rotas(self):

        # ── Página principal ─────────────────────────────────────────────────
        @self.app.route("/")
        def index():
            sessoes = self.sessao_ctrl.listar_sessoes()
            cinemas = self.sessao_ctrl.listar_cinemas()
            filmes  = self.sessao_ctrl.listar_filmes()
            return render_template("sessoes.html", sessoes=sessoes,
                                   cinemas=cinemas, filmes=filmes)

        # ── Cinemas ──────────────────────────────────────────────────────────
        @self.app.route("/cinemas")
        def cinemas():
            lista = self.cinema_ctrl.listar_cinemas()
            sessoes = self.sessao_ctrl.listar_sessoes()
            totais = {}
            for c in lista:
                totais[c.id] = self.sessao_ctrl.total_por_cinema(c.id)
            return render_template("cinemas.html", cinemas=lista, totais=totais)

        @self.app.route("/cinemas/novo", methods=["POST"])
        def criar_cinema():
            mensagem, erro = None, None
            try:
                self.cinema_ctrl.criar_cinema(
                    request.form["nome"],
                    request.form["endereco"],
                    request.form["capacidade"]
                )
                mensagem = "Cinema cadastrado com sucesso!"
            except (ValueError, Exception) as e:
                erro = str(e)
            lista = self.cinema_ctrl.listar_cinemas()
            totais = {c.id: self.sessao_ctrl.total_por_cinema(c.id) for c in lista}
            return render_template("cinemas.html", cinemas=lista,
                                   totais=totais, mensagem=mensagem, erro=erro)

        # ── Filmes ───────────────────────────────────────────────────────────
        @self.app.route("/filmes")
        def filmes():
            lista = self.filme_ctrl.listar_filmes()
            totais = {f.id: self.sessao_ctrl.total_por_filme(f.id) for f in lista}
            return render_template("filmes.html", filmes=lista, totais=totais)

        @self.app.route("/filmes/novo", methods=["POST"])
        def criar_filme():
            mensagem, erro = None, None
            try:
                self.filme_ctrl.criar_filme(
                    request.form["titulo"],
                    request.form["duracao_min"],
                    request.form.get("sinopse", ""),
                    request.form["generos"],
                    request.form["diretores"],
                    request.form["atores"]
                )
                mensagem = "Filme cadastrado com sucesso!"
            except (ValueError, Exception) as e:
                erro = str(e)
            lista = self.filme_ctrl.listar_filmes()
            totais = {f.id: self.sessao_ctrl.total_por_filme(f.id) for f in lista}
            return render_template("filmes.html", filmes=lista, totais=totais,
                                   mensagem=mensagem, erro=erro)

        # ── Sessões ──────────────────────────────────────────────────────────
        @self.app.route("/sessoes/nova", methods=["POST"])
        def criar_sessao():
            mensagem, erro = None, None
            try:
                self.sessao_ctrl.criar_sessao(
                    request.form["cinema_id"],
                    request.form["filme_id"],
                    request.form["data_hora"],
                    request.form["sala"]
                )
                mensagem = "Sessão cadastrada com sucesso!"
            except (ValueError, Exception) as e:
                erro = str(e)
            sessoes = self.sessao_ctrl.listar_sessoes()
            cinemas = self.sessao_ctrl.listar_cinemas()
            filmes = self.sessao_ctrl.listar_filmes()
            return render_template("sessoes.html", sessoes=sessoes,
                                   cinemas=cinemas, filmes=filmes,
                                   mensagem=mensagem, erro=erro)

        # ── Registrar público ────────────────────────────────────────────────
        @self.app.route("/sessoes/publico", methods=["POST"])
        def registrar_publico():
            mensagem, erro = None, None
            try:
                self.sessao_ctrl.registrar_publico(
                    request.form["sessao_id"],
                    request.form["publico"]
                )
                mensagem = "Público registrado com sucesso!"
            except (ValueError, Exception) as e:
                erro = str(e)
            sessoes = self.sessao_ctrl.listar_sessoes()
            cinemas = self.sessao_ctrl.listar_cinemas()
            filmes = self.sessao_ctrl.listar_filmes()
            return render_template("sessoes.html", sessoes=sessoes,
                                   cinemas=cinemas, filmes=filmes,
                                   mensagem=mensagem, erro=erro)

    def run(self):
        self.app.run(debug=True)
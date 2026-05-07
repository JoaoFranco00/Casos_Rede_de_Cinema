from controller.cinema_controller import CinemaController
from controller.filme_controller import FilmeController
from controller.sessao_controller import SessaoController


def menu_principal():
    cinema_ctrl = CinemaController()
    filme_ctrl  = FilmeController()
    sessao_ctrl = SessaoController()

    while True:
        print("\n===== REDE DE CINEMAS =====")
        print("1 - Cadastrar Cinema")
        print("2 - Listar Cinemas")
        print("3 - Cadastrar Filme")
        print("4 - Listar Filmes")
        print("5 - Cadastrar Sessão")
        print("6 - Listar Sessões")
        print("7 - Registrar Público de Sessão")
        print("0 - Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            nome = input("Nome do cinema: ")
            endereco = input("Endereço: ")
            capacidade = input("Capacidade: ")
            try:
                cinema_ctrl.criar_cinema(nome, endereco, capacidade)
                print("✅ Cinema cadastrado!")
            except ValueError as e:
                print(f"❌ {e}")

        elif opcao == "2":
            cinemas = cinema_ctrl.listar_cinemas()
            if not cinemas:
                print("Nenhum cinema cadastrado.")
            for c in cinemas:
                total = sessao_ctrl.total_por_cinema(c.id)
                print(f"[{c.id}] {c.nome} | {c.endereco} | Cap: {c.capacidade} | Público total: {total}")

        elif opcao == "3":
            titulo = input("Título: ")
            duracao = input("Duração (min): ")
            sinopse = input("Sinopse: ")
            generos = input("Gêneros (separados por vírgula): ")
            diretores = input("Diretores (separados por vírgula): ")
            atores = input("Atores (separados por vírgula): ")
            try:
                filme_ctrl.criar_filme(titulo, duracao, sinopse, generos, diretores, atores)
                print("✅ Filme cadastrado!")
            except ValueError as e:
                print(f"❌ {e}")

        elif opcao == "4":
            filmes = filme_ctrl.listar_filmes()
            if not filmes:
                print("Nenhum filme cadastrado.")
            for f in filmes:
                total = sessao_ctrl.total_por_filme(f.id)
                print(f"[{f.id}] {f.titulo} | {f.duracao_min}min | "
                      f"Gêneros: {', '.join(f.generos)} | "
                      f"Diretores: {', '.join(f.diretores)} | "
                      f"Elenco: {', '.join(f.atores)} | Público total: {total}")

        elif opcao == "5":
            cinemas = cinema_ctrl.listar_cinemas()
            for c in cinemas:
                print(f"  [{c.id}] {c.nome}")
            cinema_id = input("ID do Cinema: ")
            filmes = filme_ctrl.listar_filmes()
            for f in filmes:
                print(f"  [{f.id}] {f.titulo}")
            filme_id = input("ID do Filme: ")
            data_hora = input("Data e Hora (YYYY-MM-DDTHH:MM): ")
            sala = input("Sala: ")
            try:
                sessao_ctrl.criar_sessao(cinema_id, filme_id, data_hora, sala)
                print("✅ Sessão cadastrada!")
            except ValueError as e:
                print(f"❌ {e}")

        elif opcao == "6":
            sessoes = sessao_ctrl.listar_sessoes()
            if not sessoes:
                print("Nenhuma sessão cadastrada.")
            for s in sessoes:
                print(f"[{s.id}] {s.filme_titulo} | {s.cinema_nome} | "
                      f"{s.data_hora} | Sala: {s.sala} | Público: {s.publico}")

        elif opcao == "7":
            sessoes = sessao_ctrl.listar_sessoes()
            for s in sessoes:
                print(f"  [{s.id}] {s.filme_titulo} – {s.cinema_nome} – {s.data_hora}")
            sessao_id = input("ID da Sessão: ")
            publico = input("Quantidade de público: ")
            try:
                sessao_ctrl.registrar_publico(sessao_id, publico)
                print("✅ Público registrado!")
            except ValueError as e:
                print(f"❌ {e}")

        elif opcao == "0":
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()

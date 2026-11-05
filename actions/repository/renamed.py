from actions.push.commits import notification


def executar(dados):
    nome_antigo = dados["changes"]["repository"]["name"]["from"]
    nome_novo = dados["repository"]["name"]
    autor = dados["sender"]["login"]

    mensagem = f"✏️ Repositório **{nome_antigo}** foi renomeado para **{nome_novo}** por **{autor}**!"
    notification(mensagem)
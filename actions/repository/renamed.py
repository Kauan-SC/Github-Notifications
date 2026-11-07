from helpers import notification


def executar(dados):
    nome_antigo = dados["changes"]["repository"]["name"]["from"]
    nome_novo = dados["repository"]["name"]
    autor = dados["sender"]["login"]

    message_data = {
    "flags": 32768,
    "components": [
        {
        "type": 17,
        "components": [
            {
            "type": 10,
            "content": f"✏️ Repositório **{nome_antigo}** foi renomeado para **{nome_novo}** por **{autor}**!"
            }
        ]
        }
    ]
    }


    notification(message_data)
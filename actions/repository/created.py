from actions.push.commits import notification


def executar(dados):
    repo = dados["repository"]["full_name"]
    autor = dados["sender"]["login"]

    message_data = {
    "flags": 32768,
    "components": [
        {
        "type": 17,
        "components": [
            {
            "type": 10,
            "content": f"📦 Repositório **{repo}** foi criado por **{autor}**!"
            }
        ]
        }
    ]
    }


    notification(message_data)
from actions.push.commits import notification


def executar(dados):
    repo = dados["repository"]["full_name"]
    autor = dados["pusher"]["name"]
    commit = dados["head_commit"]
    mensagem_commit = commit["message"]
    commit_id = commit["id"][:7]

    message_data = {
    "flags": 32768,
    "components": [
        {
        "type": 17,
        "components": [
            {
            "type": 10,
            "content": f"📝 Novo commit em **{repo}** por **{autor}**."
            },
            {
            "type": 14,
            "spacing": 1,
            "divider": True
            },
            {
            "type": 10,
            "content": f"ID do commit: {commit_id}"
            },
            {
            "type": 14,
            "spacing": 1,
            "divider": True
            },
            {
            "type": 10,
            "content": f"Mensagem de Commit: {mensagem_commit}"
            }
        ]
        }
    ]
    }


    notification(message_data)

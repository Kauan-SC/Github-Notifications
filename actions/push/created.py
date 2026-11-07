from helpers import notification


def executar(dados):
    repo = dados["repository"]["full_name"]
    ref = dados["ref"]
    autor = dados["pusher"]["name"]

    message_data = {
    "flags": 32768,
    "components": [
        {
        "type": 17,
        "components": [
            {
            "type": 10,
            "content": f"🌱 Nova branch **{ref}** criada em **{repo}** por **{autor}**!"
            }
        ]
        }
    ]
    }


    notification(message_data)
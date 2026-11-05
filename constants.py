import os

from dotenv import load_dotenv

load_dotenv()

# Webhooks:
Bot_webhook = os.environ["INFO_BOT_WEBHOOK"]

# Category IDs
class Categorys:
    INFORMAÇÕES = int(os.environ["CATEGORY_INFORMACOES"])
    BATE_PAPO = int(os.environ["CATEGORY_BATE_PAPO"])
    ASSETS = int(os.environ["CATEGORY_ASSETS"])
    PROJETOS_LOGS = int(os.environ["CATEGORY_PROJETOS_LOGS"])

# ------------------------------------------------------------------------------------------

class Channels:
    # Channels IDS / INFORMAÇÕES
    BEM_VINDO = int(os.environ["CHANNEL_BEM_VINDO"])
    REGRAS = int(os.environ["CHANNEL_REGRAS"])

    # Channels IDS / BATE_PAPO
    INFOS = int(os.environ["CHANNEL_INFOS"])
    ERRORS = int(os.environ["CHANNEL_ERRORS"])
    EQUIPE_INTERNA = int(os.environ["CHANNEL_EQUIPE_INTERNA"])
    SALA_DE_REUNIÕES = int(os.environ["CHANNEL_SALA_DE_REUNIOES"])

    # Channels IDS / ASSETS (nova categoria)
    FILES = int(os.environ["CHANNEL_FILES"])
    SKILLS = int(os.environ["CHANNEL_SKILLS"])

    # Channels IDS / PROJETOS_LOGS
    ARENA_44 = int(os.environ["CHANNEL_ARENA_44"])
    MARCELO_SUARTZ = int(os.environ["CHANNEL_MARCELO_SUARTZ"])
    IMPREGRAF = int(os.environ["CHANNEL_IMPREGRAF"])
    SPA_THERAPY_LAURA = int(os.environ["CHANNEL_SPA_THERAPY_LAURA"])
    RAUL_ECON_CONSTRUTORA = int(os.environ["CHANNEL_RAUL_ECON_CONSTRUTORA"])
    IAN_VILELA_IMOVEIS = int(os.environ["CHANNEL_IAN_VILELA_IMOVEIS"])


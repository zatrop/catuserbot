import sys
from telethon.sessions import StringSession

from ..Config import Config
from .client import CatUserBotClient

__version__ = "2.10.6"

loop = None

if Config.STRING_SESSION:
    session = StringSession(str(Config.STRING_SESSION))
else:
    session = "catuserbot"

try:
    catub = CatUserBotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        # loop=loop,
        app_version=__version__,
#         connection=ConnectionTcpAbridged,
        auto_reconnect=True,
#         connect_retries=None,
    ).start()
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()


catub.tgbot = tgbot = CatUserBotClient(
    session="TgCatUB",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    # loop=loop,
    app_version=__version__,
#     connection=ConnectionTcpAbridged,
    auto_reconnect=True,
#     connect_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)

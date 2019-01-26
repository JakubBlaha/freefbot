import sys
from discord import Game
from discord.ext.commands import Bot

from logger import Logger
import commands
from config import Config


class FreefClient(Bot):
    def __init__(self, *args, **kw):
        Logger.info('Client: Initializing client')
        super().__init__(*args, **kw)
        self.load_extension('commands')

    async def on_ready(self):
        Logger.info(f'Client: Logged on as {self.user}')
        presence = Game('⚠ Under construction ⚠')


# Logger
sys.stderr = Logger
sys.stdout = Logger

# Client
client = FreefClient(command_prefix='!')
client.run(Config.token)
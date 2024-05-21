import discord

from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError

TOKEN = "TOKEN"
PREFIX = "*"
BOTID = "ID"
STAGENAME = "test"
MODROLE = "LEFYBOT"
VOLUME = 0.2
GUILDIDS = []
SPOTIPY_CLIENT_ID = 'test'
SPOTIPY_CLIENT_SECRET = 'test'
SPOTIPY_REDIRECT_URI = 'test'
SPOTIPY_SCOPE = 'user-read-private user-read-email user-library-read playlist-read-private user-top-read'

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(PREFIX),
    intents=discord.Intents.all(),
)

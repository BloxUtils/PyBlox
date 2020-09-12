import logging

import PyBlox2

from secret import ROBLOSECURITY

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
    )
client = PyBlox2.BloxClient(prefix="!")


@client.event
async def ready(payload):
    assert payload == "I'm ready"
    print("xx---xx")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("xx---xx")

@client.command
async def ping(ctx, text):
    print('pong ', text)

@client.event
async def error(ctx, error):
    print(ctx.user, " caused an error <unhappy face>")

@client.event
async def start_listening(guild):
    await guild.fetch("name")
    print("Listening to guild", guild)

client.run(ROBLOSECURITY, group_id=3891491)


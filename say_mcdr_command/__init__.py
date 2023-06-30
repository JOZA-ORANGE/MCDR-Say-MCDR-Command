import re

from mcdreforged.api.all import *


def on_info(server: ServerInterface, info: Info):
    if info.player is not None or info.is_user is True:
        return

    if info.content.startswith("[Not Secure]"):
        info.content = info.content.replace("[Not Secure] ", "")
    re_match = re.match(r"^\[(\w+?)]", info.content)
    if re_match is None or re_match.start() != 0:
        return
    info.player = re_match.group(1)
    info.content = info.content.replace("[" + info.player + "] ", "")
    if info.content.startswith("!!!!") is True:
        command = info.content.replace("!!!!", "!!")
        server.execute_command(command=command, source=info.get_command_source())

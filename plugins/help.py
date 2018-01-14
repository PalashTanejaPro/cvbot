import re

from errbot import BotPlugin, re_botcmd


class help(BotPlugin):
    """
    List the bot rules
    """

    @re_botcmd(pattern=r'commands',
               re_cmd_name_help='commands',
               flags=re.IGNORECASE,
               template='help.jinja2')
    def help(self, msg, args):
        """
        Show the bot rules.
        """
        return {'rules': True}
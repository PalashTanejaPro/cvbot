import re

from errbot import BotPlugin, re_botcmd


class List_commands(BotPlugin):
    """
    List the bot rules
    """

    @re_botcmd(pattern=r'list\s+commands',
               re_cmd_name_help='list commands',
               flags=re.IGNORECASE,
               template='list.jinja2')
        
    def list_commands(self, msg, args):
        """
        Show the bot rules.
        """
        return {'rules': True}

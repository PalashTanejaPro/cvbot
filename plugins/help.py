import re

from errbot import BotPlugin, re_botcmd


class help(BotPlugin):
    """
    List the bot rules
    """

    @re_botcmd(pattern=r'help.*',
               re_cmd_name_help='help',
               flags=re.IGNORECASE,
               template='help.jinja2')
    def the_rules(self, msg, args):
        """
        Show the bot rules.
        """
        return {'rules': True}
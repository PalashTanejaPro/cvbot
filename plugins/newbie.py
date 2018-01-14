import re

from errbot import BotPlugin, re_botcmd


class Newbie(BotPlugin):
    """
    List the bot rules
    """

    @re_botcmd(pattern=r'newbie',
               re_cmd_name_help='newbiw',
               flags=re.IGNORECASE,
               template='newbie.jinja2')
        
    def newbie(self, msg, args):
        """
        Show the bot rules.
        """
        return {'rules': True}

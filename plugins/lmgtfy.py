from errbot import BotPlugin, re_botcmd
from google import search

class Lmgtfy(BotPlugin):
    """
    For all those people who find it more convenient to bother you with their
    question rather than search it for themselves.
    """

    @re_botcmd(pattern=r'lmgtfy\s+(.+)',
               re_cmd_name_help='lmgtfy <search-string>',
               template='lmgtfy.jinja2')
    def lmgtfy(self, msg, match):
        """I'm lazy, please google for me."""  # Ignore QuotesBear
        res = []
        for url in search(match.group(1), tld="com", lang="en", stop=5):
            res.append(url)
        return {'results': res}

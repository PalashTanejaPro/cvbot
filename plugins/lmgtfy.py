from errbot import BotPlugin, re_botcmd
from googlesearch import search

class Lmgtfy(BotPlugin):
    """
    For all those people who find it more convenient to bother you with their
    question rather than search it for themselves.
    """

    @re_botcmd(pattern=r'lmgtfy\s+(.+)',
               re_cmd_name_help='lmgtfy <search-string>')
    def lmgtfy(self, msg, match):
        """I'm lazy, please google for me."""  # Ignore QuotesBear
        searches = search(match.group(1), tld="com", lang="en", stop=1)
        return ('There ya go! this can be solved using a simple Google Search:\n- ' +
        '\n- '.join([url for url in searches]) )

import json
import os
from urllib.parse import quote_plus, urljoin

from errbot import BotPlugin, botcmd
import requests


class Answer(BotPlugin):

    # Ignore LineLengthBear, PyCodestyleBear
    SURVEY_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSeD8lqMWAwJx0Mewlpc5Sbeo3MH5Yi9fSfXA6jnk07-aIURSA/viewform?usp=pp_url&entry.1236347280={question}&entry.1734934116={response}&entry.75323266={message_link}'
    MESSAGE_LINK = 'https://gitter.im/{uri}?at={idd}'

    @staticmethod
    def construct_link(text):
        if 'cloudcv/docs/' in text:
            text = text.split('cloudcv/docs/')[-1]
            return 'https://api.cloudcv.io/en/latest/' + text
        elif 'documentation/' in text:
            text = text.split('documentation/')[-1]
            return 'https://docs.cloudcv.io/en/latest/' + text

    @botcmd
    def answer(self, msg, arg):
        try:
            answers = requests.get(urljoin(os.environ['ANSWER_END'], 'answer'),
                                   params={'question': arg}).json()
        except json.JSONDecodeError:  # pragma: no cover # for logging
            self.log.exception('something went wrong while fetching answer for'
                               'question: {}'.format(arg))
            yield 'Something went wrong, please check logs'.format()
        if answers:
            reply = 'Please checkout the following links: \n- '
            reply += '- '.join(map(lambda x:
                                   type(self).construct_link(
                                        x[0].splitlines()[-1]) + '\n',
                                   answers))
            try:
                reply += ('\n\nPlease fill in [this]({}) form to rate the '
                          'answer'.format(self.SURVEY_LINK.format(
                                    question=quote_plus(arg),
                                    response=quote_plus(reply),
                                    message_link=self.MESSAGE_LINK.format(
                                        uri=msg.frm.room.uri,
                                        idd=msg.extras['id'])
                                )
                            )
                          )
            except AttributeError:  # pragma: no cover
                # Test backend doesn't have room attribute
                pass
            yield reply
        else:
            yield 'Dunno'

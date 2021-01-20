# -*- coding: utf-8 -*-
import zmq
from telegram.ext import (CommandHandler, ConversationHandler, Filters, Job,
                          MessageHandler, Updater)

from .logger import get_logger

logger = get_logger(__name__)


class TKLBot(object):

    def __init__(self,
                 client,
                 bot_key):
        self._client = client
        self._updater = Updater(bot_key, use_context=True)
        self._dp = self._updater.dispatcher

        self._dp.add_handler(CommandHandler(
            "start",
            self._start,
            pass_user_data=True))
        self._dp.add_handler(MessageHandler(
            Filters.text,
            self._start,
            pass_user_data=True))
        self._dp.add_error_handler(self._error)

    def _start(self, update, context):
        logger.info("Mensaje recibido: ChatId=%s", update.message.chat.id)
        try:
            msg = str(self._client)
        except ValueError:
            msg = "La formadora está apagada."
        except zmq.ZMQError as ex:
            msg = "Error: {}".format(ex)
        finally:
            update.message.reply_text(msg)

    def _error(self, update, context):
        logger.warn('Update "%s" caused error "%s"' % (update, context.error))

    def run(self):
        logger.info("Iniciando servidor")
        self._updater.start_polling()
        self._updater.idle()




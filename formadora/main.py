import argparse
import sys

from . import __version__
from .client import TKL688
from .config import load_config
from .telegram_bot import TKLBot


HELP_EPILOG = "Herramienta de monitoreo para formadora de baterias"


def go():
    parser = argparse.ArgumentParser(prog='formadora', epilog=HELP_EPILOG)
    parser.add_argument(
        '--config-file', default='config.ini')
    parser.add_argument(
        '--run-bot',
        action="store_true",
        default=False,
        help="Run Telegram bot")
    parser.add_argument(
        '--version',
        action="store_true",
        default=False,
        help="Print version and exit")
    args = parser.parse_args()
    config = load_config(args.config_file)

    if args.version:
        sys.stdout.write(f"Formadora {__version__}")
        return 0

    client = TKL688(ip=config['DEFAULT']['RaspiIp'])
    if args.run_bot:
        bot = TKLBot(
            client=client,
            bot_key=config['DEFAULT']['TelegramToken'],
        )
        bot.run()

    print(client)

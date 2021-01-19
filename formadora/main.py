import sys
import argparse
from .client import TKL688
from .config import get_config
from . import __version__


def go():
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
    config = get_config(args.config_file)

    if args.version:
        sys.stdout.write(f"Formadora {__version__}")
        return 0

    client = TKL688(config['RASPI']['ip'])
    

    print(client)

import asyncio
import logging
import config

from logging.handlers import RotatingFileHandler
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats
from handlers import register_routes

logger = logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def setup_bot_dispatcher() -> Dispatcher:
    logger.info('Start prepare dispatcher')
    dispatcher = Dispatcher()
    register_routes(dispatcher)
    logger.info('Dispatcher was prepared')
    return dispatcher

async def set_default_commands():
    commands = [
        BotCommand(command='/start', description='Начать работу с ботом'),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeAllPrivateChats())

async def main():
    dispatcher = await setup_bot_dispatcher()
    await set_default_commands()
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())
    finally:
        await bot.session.close()
        logger.info('Bot session closed')

if __name__ == '__main__':
    from os import path
    logg_filename = path.join('scr', '_logs', 'log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)-15s:%(lineno)4d %(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
        handlers=[
            RotatingFileHandler(filename=logg_filename, maxBytes=2048000, backupCount=10),
            logging.StreamHandler(),
        ],
    )
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('stoped by KeyboardInterrupt')

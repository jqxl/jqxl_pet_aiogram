from aiogram import Dispatcher

from .common import common_router

def register_routes(dp: Dispatcher):
    dp.include_router(common_router)

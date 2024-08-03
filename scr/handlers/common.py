from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery

import kb
import messages
from enums import Callbacks, Commands


common_router = Router()

@common_router.message(Command(Commands.START))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(messages.greet.format(name=message.from_user.full_name), reply_markup=kb.yes_no_kb)

@common_router.message(F.data == Callbacks.YES, F.data == Callbacks.NO)
async def callback_handler(callback: CallbackQuery):
    await callback.message.answer(messages.you_press.format(callback=callback))

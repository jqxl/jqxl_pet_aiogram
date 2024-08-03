from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery

import kb
import messages
from enums import Callbacks, Commands


common_router = Router()

@common_router.message(F.text, Command(Commands.start))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(messages.greet.format(name=message.from_user.full_name), reply_markup=kb.remove_keyboard)

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

import captions
from enums import Callbacks

remove_keyboard = ReplyKeyboardRemove()

start_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=captions.start)]],
    resize_keyboard=True,
    one_time_keyboard=True,
)

ask_for_a_phone_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=captions.send_phone_number, request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True,
)

yes_no_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=captions.yes, callback_data=Callbacks.yes),
            InlineKeyboardButton(text=captions.no, callback_data=Callbacks.no),
        ]
    ]
)

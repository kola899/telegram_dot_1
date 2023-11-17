from aiogram import types
from aiogram.filters import Command,Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import router
from keys.key import kb_random
from random import randint
@router.message(Command('random'))
async def get_random(message: types.Message):
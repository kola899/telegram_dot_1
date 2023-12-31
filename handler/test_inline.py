from aiogram import types
from aiogram.filters import Command,Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import router
from keys.key import kb_random
from random import randint
kb_random = [types.InlineKeyboardButton(text='Нажми меня!',
                                        callback_data='random_num')]
@router.message(Command('random'))
async def get_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    for button in kb_random:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text=f'Получить рандомное число от 1 до 10?',
                         reply_markup=builder.as_markup(resize_keyboard=True))

@router.message(Text('random_num'))
async def choice(callback: types.CallbackQuery):
    num = randint(1, 10)
    await callback.message.answer(f'Твоё число: {num}')
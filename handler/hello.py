from aiogram import types
from aiogram.filters import Text
from loader import router
@router.message(Text(contains="привет"))
async def hallo(message: types.Message):
    await message.answer(text='hello')
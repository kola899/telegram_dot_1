import asyncio
from aiogram.filters import Text, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Text
from aiogram.types import FSInputFile
TOKEN = '6735716649:AAG-vPyVvlu3QZRE8np6b4E2FYSKgpLW_TE'
router = Router()
@router.message(Text(startswith="Привет"))
async def hallo(message: types.Message):
    await message.answer(text='Привет')
kb = [
    types.KeyboardButton(text='Кнопочка 1'),
    types.KeyboardButton(text='Кнопочка 2'),
]
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for button in kb:
        builder.add(button)
    builder.adjust(2)
    await message.answer(text='Сделай выбор',
                         reply_markup=builder.as_markup(resize_keyboard=True))
@router.message(Text('Кнопочка 1'))
async def hello(message: types.Message):
    await message.answer(text='Ты выбрал Кнопку 1')

@router.message(Command('привет'))
async def send_image_file(message: types.Message):
    url = f'data/kek.png'
    task_image = FSInputFile(url)
    await message.answer_photo(
        photo=task_image,
        caption='Не обязательная подпись к картинке'
    )

async def main():
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode='HTML')
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
if __name__ == '__main__':
    asyncio.run(main())

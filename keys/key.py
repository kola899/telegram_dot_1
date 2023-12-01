from aiogram import types
kb_random = [
    types.InlineKeyboardButton(text='Нажми на меня!', callback_data='random_num')
]
kb_menu = [
    types.KeyboardButton(text='Список задач'),
    types.KeyboardButton(text='Добавить задачу'),
    types.KeyboardButton(text='Удалить задачу')
]
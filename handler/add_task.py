from aiogram import types
from aiogram.filters import Text, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import *
from keys.key import kb_menu
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
class Task_from(StatesGroup):
    task = State()
@router.message(Command('cantel'))
async def cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Действие отменено')

@router.message(Text('Добавить задачу '))
async def cancel(message: types.Message, state: FSMContext):
    id_user = message.chat.id
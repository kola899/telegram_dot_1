from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loader import router
class Reg_from(StatesGroup):
    name = State()
    age = State()
    gander = State()
@router.message(Command('reg'))
async def start_reg(message: types.Message, state: FSMContext):
    await state.set_state(Reg_from.name)
    await message.answer('Проивет. Напиши и отправь своё имя')
@router.message(Reg_from.name)
async def get_name(message: types.Message, state: FSMContext):
    await  state.update_data(name=message.text)
    await state.set_state(Reg_from.age)
    await message.answer('А сейчас напиши и отправь свой возраст')
@router.message(Reg_from.name)
async def get_name(message: types.Message, state: FSMContext):
    await  state.update_data(age=message.text)
    await state.set_state(Reg_from.gender)
    await message.answer('Укажи свой пол')
@router.message(Reg_from.name)
async def get_name(message: types.Message, state: FSMContext):
    await  state.update_data(gender=message.text)
    data = await state.get_data()
    name = data['name']
    age = data['age']
    gender = data['gender']
    await state.clear()
    await message.answer(('Регистрация завершина\n'
                          f'Имя {name}\n'
                          f'Возраст {age}\n'
                          f'Пол {gender}'))
@router.message(Command('cancel'))
async def restart(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Регистрация отменена')
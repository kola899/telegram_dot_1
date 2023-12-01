from aiogram import Bot, Dispatcher, Router
import sqlite3
TOKEN = '6735716649:AAH6lrxTpmTFMv5H43VOYJEpSm3QMx3hIcY'
router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN, parse_mode='HTML')
con = sqlite3.connect('data/data.db')
cursor = con.cursor()

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import token
import asyncio
import random
from aiogram import F

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer('''Добро пожаловать в игру"камень, ножницы, бумага"
Выберите камень, ножницы или бумага и мы скажем кто выиграл Я или ВЫ!!!''')

choices = ['камень', 'ножницы', 'бумага']

def play_game(user_choice):
    bot_choice = random.choice(choices)

    if user_choice == bot_choice:
        return(f"Я выбрал {bot_choice}. НИЧЬЯ!!!")
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
         (user_choice == 'ножницы' and bot_choice == 'бумага') or \
         (user_choice == 'бумага' and bot_choice == 'камень'):
        return (f"Я выбрал {bot_choice}. ВЫ ВЫИГРАЛИ!!!")
    else:
        return (f"Я выбрал {bot_choice}. ВЫ ПРОИГРАЛИ!!!")
    
@dp.message(F.text)
async def echo(message: types.Message):
    user_choice = message.text.lower()

    if user_choice not in choices:
        await message.answer("Пожалуйста, выберите один из вариантов: камень, ножницы или бумага.")
        return
    
    result = play_game(user_choice)
    await message.answer(result)

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer('Добро пожаловать в игру"камень, ножницы, бумага" /n Выберите камень, ножницы или бумага и мы скажем кто выиграл Я или ВЫ')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
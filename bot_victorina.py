import asyncio
import gspread
from config import bot_token
from aiogram import*
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, CallbackQuery, Message, InlineKeyboardMarkup
from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(bot_token)
dp = Dispatcher()
router = Router()

gs = gspread.service_account(filename=r'/home/unotuno/Рабочий стол/newpro-426508-c47665635951.json')
sht = gs.open_by_url('https://docs.google.com/spreadsheets/d/1Mt28TQ_f71Jzc4jBpE8KV_UQwQ3Cr0LUsXZ8KOeTypE/edit?gid=0#gid=0')
work_sheet = sht.get_worksheet(2)
list_of_values = work_sheet.get_all_values()

def creating_msg(n,ch_id):
    msg = []
    for i,j in enumerate(list_of_values[int(n)]):
        l = list_of_values[int(n)]
        if (i == 1) and not (j.endswith('?')): msg.append(bot.send_message(ch_id,j))
        if l[i].endswith(('jpg','png','JPG','PNG')):
            if ';' in l[i]:
                for a in l[i].split(';'):
                    photo = types.FSInputFile(f'media/{a}')
                    msg.append(bot.send_photo(ch_id,photo))
            else:
                photo = types.FSInputFile(f'media/{j}')
                msg.append(bot.send_photo(ch_id, photo))
        if l[i].startswith('https'): msg.append(bot.send_message(ch_id,f'{j}'))
        if l[i].endswith('mp3'):
            audio = types.FSInputFile(f'media/{j}')
            msg.append(bot.send_audio(ch_id,audio))
    return msg
@router.message(Command('start'))
async def start(message: types.Message):
    n = 1
    for i in creating_msg(n,message.chat.id):
        await i
    one_btn = InlineKeyboardBuilder()
    one_btn.add(InlineKeyboardButton(text='*', callback_data=f'{n + 1}'))
    await bot.send_message(message.chat.id, text=f'{list_of_values[n][12]}', reply_markup=one_btn.as_markup())
@router.callback_query()
async def message_callback(call: CallbackQuery):
    data = call.data
    one_btn = InlineKeyboardBuilder()
    if data[-1] == 'T':
        one_btn.add(InlineKeyboardButton(text='*', callback_data=f'{int(data[:-1]) + 1}'))
        await bot.send_message(call.message.chat.id, text=f'{list_of_values[int(data[:-1])][8]}')
        await bot.send_message(call.message.chat.id, text=f'{list_of_values[int(data[:-1])][12]}',
                               reply_markup=one_btn.as_markup())
    elif data[-1] == 'F':
        one_btn.add(InlineKeyboardButton(text='*', callback_data=f'{int(data[:-1]) + 1}'))
        await bot.send_message(call.message.chat.id, text=f'{list_of_values[int(data[:-1])][9]}')
        await bot.send_message(call.message.chat.id, text=f'{list_of_values[int(data[:-1])][12]}',
                               reply_markup=one_btn.as_markup())
    elif int(data) in (5,7,10,31,44):
        keyb = InlineKeyboardBuilder()
        for i in creating_msg(call.data, call.message.chat.id):
            await i
        for i in list_of_values[int(data)][6].split(','):
            if i == list_of_values[int(data)][7]: keyb.add(InlineKeyboardButton(text=f'{i}', callback_data=f"{data}T"))
            else: keyb.add(InlineKeyboardButton(text=f'{i}', callback_data=f"{data}F"))
        keyb.adjust(1)
        await bot.send_message(call.message.chat.id, text=f'{list_of_values[int(data)][1]}',
                               reply_markup=keyb.as_markup())
    elif int(data) not in (5,7,10,31,44):
        for i in creating_msg(call.data, call.message.chat.id):
            await i
        one_btn.add(InlineKeyboardButton(text='*', callback_data=f'{int(data) + 1}'))
        await bot.send_message(call.message.chat.id, text=f'{list_of_values[int(data)][12]}',
                               reply_markup=one_btn.as_markup())
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Ой')

# # import gspread
bot_token = '6328630786:AAFxh0fPW0-NyxK2mvC-ZwPKvqAEuEAIyE8'
#
#
#
# import asyncio
# import gspread
# from config import bot_token
# from aiogram import*
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import InlineKeyboardButton, CallbackQuery, Message, InlineKeyboardMarkup
# from aiogram import Router
# from aiogram.utils.keyboard import InlineKeyboardBuilder
#
# class Answer(StatesGroup):
#     wait_btn = State()
#
# bot = Bot(bot_token)
# dp = Dispatcher()
# router = Router()
#
# gs = gspread.service_account(filename=r'/home/unotuno/Рабочий стол/newpro-426508-c47665635951.json')
# sht = gs.open_by_url('https://docs.google.com/spreadsheets/d/1Mt28TQ_f71Jzc4jBpE8KV_UQwQ3Cr0LUsXZ8KOeTypE/edit?gid=0#gid=0')
# work_sheet = sht.get_worksheet(2)
# list_of_values = work_sheet.get_all_values()
#
# def creating_msg(n,ch_id):
#
#     msg = []
#     for i,j in enumerate(list_of_values[int(n)]):
#         l = list_of_values[int(n)]
#         if (i == 1) and not (j.endswith('?')): msg.append(bot.send_message(ch_id,j))
#         if l[i].endswith(('jpg','png','JPG','PNG')):
#             if ';' in l[i]:
#                 for a in l[i].split(';'):
#                     photo = types.FSInputFile(f'media/{a}')
#                     msg.append(bot.send_photo(ch_id,photo))
#             else:
#                 photo = types.FSInputFile(f'media/{j}')
#                 msg.append(bot.send_photo(ch_id, photo))
#         if l[i].startswith('https'): msg.append(bot.send_message(ch_id,f'{j}'))
#         if l[i].endswith('mp3'):
#             audio = types.FSInputFile(f'media/{j}')
#             msg.append(bot.send_audio(ch_id,audio))
#         if i == 6 and j!='':
#             Answer.wait_btn.set()
#             keyb = InlineKeyboardBuilder()
#             for i in j.split(','):
#                 print(i)
#                 keyb.add(InlineKeyboardButton(text=f'{i}',callback_data=f'{i}'))
#             keyb.adjust(1)
#             msg.append(bot.send_message(chat_id=ch_id ,text = f'{l[1]}', reply_markup=keyb.as_markup()))
#
#         if i == 12:
#             one_btn = InlineKeyboardBuilder()
#             one_btn.add(InlineKeyboardButton(text='*', callback_data=f'{int(n)+1}'))
#             msg.append(bot.send_message(ch_id, text = f'{j}', reply_markup=one_btn.as_markup()))
#
#     return msg
# @router.message(Command('start'))
# async def start(message: types.Message):
#     for i in creating_msg(1,message.chat.id):
#         await i
# @router.callback_query()
# async def message_callback(call: CallbackQuery):
#     for i in creating_msg(call.data, call.message.chat.id):
#         await i
#
# async def main():
#     dp.include_router(router)
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print('Ой')
#

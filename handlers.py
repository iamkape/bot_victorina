# from aiogram import*
#
#
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from config import*
# step = 0
# router = Router()
# #------------------------положить в другой фалй
# async def question(list):
#     keyboard = InlineKeyboardBuilder()
#     for i in list:
#         keyboard.add(InlineKeyboardButton(text=f'{i}',callback_data=f'{step}'))
#     return keyboard.adjust(1).as_markup()
# async def step_by_step():
#     one_keyb = InlineKeyboardBuilder()
#     one_keyb.add(InlineKeyboardButton(text='*', callback_data=f'{step}'))
#     return one_keyb.adjust(1).as_markup()
# #--------------------------------------------
#
# @router.message(Command('start'))
# async def start(message: types.Message):
#     global step
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(text='*',callback_data='*'))
#     await message.answer("hi")
#     await message.answer(f"{message_list[step][step]}")
#     await message.answer(f'{message_list[step][-1]}',reply_markup=builder.as_markup())
#     step+=1
# @router.callback_query()
# async def message_callback(call: CallbackQuery):
#     global step
#     print(message_list[step][0][-1])
#     if message_list[step][0][-1]!= '?' and message_list[step][0][-2:-1]!='ч?':
#         await call.answer('')
#         await call.message.answer(text = f"{message_list[step][0]}")
#         await call.message.answer(f'{message_list[step][-1]}', reply_markup=await step_by_step())
#     else:
#         que = questions[step][0].split(',')
#         await call.answer('')
#         await call.message.answer(f'{message_list[step][0]}', reply_markup=await question(que))
#         await call.message.answer(f'{message_list[step][-1]}', reply_markup=await step_by_step())
#     if step < len(message_list): step+=1

from aiogram.types import Message ,ReplyKeyboardRemove
from keyboards import some_buttons

async def some_answer(message: Message):
    await message.answer("Some answer", reply_markup=some_buttons)

async def cancel_markup(message: Message):
    await message.answer("Markup tozalandi!", reply_markup=ReplyKeyboardRemove())
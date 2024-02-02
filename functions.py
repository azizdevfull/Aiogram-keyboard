from aiogram.types import Message
from keyboards import some_buttons
async def some_answer(message: Message):
    await message.answer("Some answer", reply_markup=some_buttons)
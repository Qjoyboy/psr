from aiogram import Router
from aiogram.types import Message
from lexicon import lexicon
other_router = Router()

other_router.message()
async def send_answer(message: Message):
    await message.answer(text=lexicon.LEXICON_RU["other_answer"])
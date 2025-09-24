from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU

# ------- Создаём клавиатуру через ReplyKeyboardBuilder -------
btn_yes = KeyboardButton(text=LEXICON_RU["yes_button"])
btn_no = KeyboardButton(text=LEXICON_RU["no_button"])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(btn_yes, btn_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)

# ------- Создаём игровую клавиатуру без использования билдера -------

btn_1 = KeyboardButton(text=LEXICON_RU["rock"])
btn_2 = KeyboardButton(text=LEXICON_RU["paper"])
btn_3 = KeyboardButton(text=LEXICON_RU["scissors"])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[btn_1], [btn_2], [btn_3]], resize_keyboard=True
)
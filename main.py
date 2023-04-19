from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup

from constant import Text

bot_token = "6271069393:AAFseHKvFh4VxSqgYWDDE7Ronr09imDon4g"

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

map_keyboard = ReplyKeyboardMarkup(keyboard=[
    ["Цільова аудиторія 🤖"], ["Проблеми які вирішує бот 🦾"], ["Команда 🐼"], ["Технології 🛸"]
], resize_keyboard=True)


@dp.message_handler(commands=["start"])
async def sendStartMessage(message: types.Message):
    photo = open("./resources/start_img.png", "rb")
    await message.answer_photo(photo=photo, caption=Text.start_text, reply_markup=map_keyboard)


@dp.message_handler()
async def handle_message(message: types.Message):
    await reactionForText(message)


async def reactionForText(message: types.Message):
    if message.text == "Цільова аудиторія 🤖":
        await sendUserProfile(message)
    elif message.text == "Команда 🐼":
        await sendAllTeam(message)
    elif message.text == "Проблеми які вирішує бот 🦾":
        await sendSolution(message)
    elif message.text == "Технології 🛸":
        await sendTechnologies(message)
    elif message.text == "end":
        await sendTheEnd(message)


async def sendUserProfile(message: types.Message):
    photo = open("./resources/user_img.png", "rb")
    await message.answer_photo(photo=photo, caption=Text.user_profile)


async def sendAllTeam(message: types.Message):
    photo = open("./resources/team_img.png", "rb")
    team_keyboard = types.InlineKeyboardMarkup()
    daniil_deinekin = types.InlineKeyboardButton("👽 Даніїл Дейнекін 👽", callback_data="DEINEKIN_DANIIL")
    sofia = types.InlineKeyboardButton("🥰 Софія Засименко 🥰", callback_data="SOFIA")
    yroslava = types.InlineKeyboardButton("👻 Ярослава Храброва 👻", callback_data="YAROSLAVA")
    andrew = types.InlineKeyboardButton("🦁 Андрій Прудник 🦁", callback_data="ANDREW")
    volodimir = types.InlineKeyboardButton("🤖 Семенов Володимир 🤖", callback_data="VOLODIMIR")
    team_keyboard.add(daniil_deinekin)
    team_keyboard.add(sofia)
    team_keyboard.add(yroslava)
    team_keyboard.add(andrew)
    team_keyboard.add(volodimir)
    await message.answer_photo(photo=photo, caption=Text.team_text, reply_markup=team_keyboard)


async def sendSolution(message: types.Message):
    photo = open("./resources/solutions_img.png", "rb")
    await message.answer_photo(photo=photo, caption=Text.solution_text)


async def sendTechnologies(message: types.Message):
    photo = open("./resources/tech_img.png", "rb")
    await message.answer_photo(photo=photo, caption=Text.tech_text)


async def sendTheEnd(message: types.Message):
    gif = open("resources/the-end.gif", "rb")
    await bot.send_animation(message.chat.id, animation=gif)


@dp.callback_query_handler(lambda c: c.data == 'DEINEKIN_DANIIL')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("./resources/team/daniil_img.png", "rb")
    await bot.send_photo(callback_query.from_user.id, photo=photo, caption=Text.daniil_text,
                         parse_mode=types.ParseMode.MARKDOWN)


@dp.callback_query_handler(lambda c: c.data == 'SOFIA')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("./resources/team/sofia.png", "rb")
    await bot.send_photo(callback_query.from_user.id, photo=photo, caption=Text.sofia_text,
                         parse_mode=types.ParseMode.MARKDOWN)


@dp.callback_query_handler(lambda c: c.data == 'YAROSLAVA')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("./resources/team/yaroslava_img.png", "rb")
    await bot.send_photo(callback_query.from_user.id, photo=photo, caption=Text.yaroslava_text,
                         parse_mode=types.ParseMode.MARKDOWN)


@dp.callback_query_handler(lambda c: c.data == 'ANDREW')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("./resources/team/andrew.png", "rb")
    await bot.send_photo(callback_query.from_user.id, photo=photo, caption=Text.andrew_text,
                         parse_mode=types.ParseMode.MARKDOWN)


@dp.callback_query_handler(lambda c: c.data == 'VOLODIMIR')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("./resources/team/volodimir_img.png", "rb")
    await bot.send_photo(callback_query.from_user.id, photo=photo, caption=Text.volodimir_text,
                         parse_mode=types.ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)

import os
import dotenv

from vkbottle.bot import Bot, Message

from src import blueprints
from db_init import engine
from src.keyboards import (
    DO_YOU_LIKE_MEME,
    GENERAL_STATISTICS_KEYBOARD)
from src.memes_logic import (
    create_user_if_does_not_exist,
    select_random_meme,
    create_memes,
    get_meme_grades)
from src.state_dispensers import MemeState, UploadState

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

for blueprint in blueprints:
    blueprint.load(bot)


@bot.on.message(text=['Привет', 'привет'])
async def handler(message: Message) -> str:
    ans = "Привет вездекодерам! Хочешь пройти небольшой квиз?"\
        + "Тогда напиши /квиз. Ещё я умею кидать мемы! Напиши \"Мем\""
    print(message.attachments)
    return ans


# legacy get_meme view i left it there in case something goes wrong
# @bot.on.message(text=['Мем', "Скинь ещё"])
# async def get_meme(message: Message):
#     user = await bot.api.users.get(user_ids=[message.from_id])
#     user = user[0]
#     full_name = f'{user.first_name} {user.last_name}'
#     user = await create_user_if_does_not_exist(engine, message.from_id, full_name)
#     # meme_path = await select_random_meme(engine, message.from_id)
#     meme_path = 'vezdekod_memes/atL_c3yflRw.jpg'
#     meme = await PhotoMessageUploader(bot.api).upload(
#         meme_path, peer_id=message.peer_id
#     )
#     print(meme)
#     print(type(meme))
#     await bot.state_dispenser.set(message.peer_id, MemeState.MEME_SENT, meme=meme_path)
#     await message.answer(attachment=meme, keyboard=DO_YOU_LIKE_MEME)


@bot.on.message(text=['Мем', "Скинь ещё", 'мем', 'Скинь мем'])
async def get_meme(message: Message):
    user = await bot.api.users.get(user_ids=[message.from_id])
    user = user[0]
    full_name = f'{user.first_name} {user.last_name}'
    user = await create_user_if_does_not_exist(engine, message.from_id, full_name)
    meme_path, meme_id = await select_random_meme(engine, message.from_id)
    grades = await get_meme_grades(meme_id)
    dislikes, likes = 0, 0
    if grades != [] and grades is not None:
        _, dislikes, _, likes, _ = grades

    formatted_grading = f'Лайков: {dislikes} дизлайков: {likes}'
    await bot.state_dispenser.set(message.peer_id, MemeState.MEME_SENT, meme=meme_path)
    await message.answer(
        message=formatted_grading,
        attachment=meme_path,
        keyboard=DO_YOU_LIKE_MEME)


@bot.on.message(text=['Загрузи'])
async def notice_upload(message: Message):
    await bot.state_dispenser.set(message.peer_id, UploadState.UPLOADING_STATE)
    await message.answer("Скинь сюда картинки")


@bot.on.message(state=UploadState.UPLOADING_STATE)
async def upload_meme(message: Message):
    pictures = message.get_photo_attachments()
    response = await bot.api.messages.get_by_id(message_ids=[message.id])
    response = response.items[0]
    pictures = response.attachments

    picture_ids = []
    for attachment in pictures:
        picture = attachment.photo
        pic_id = f'photo{picture.owner_id}_{picture.id}'
        if picture.access_key is not None:
            pic_id += f'_{picture.access_key}'
        picture_ids.append(pic_id)
    await create_memes(picture_ids)
    await message.answer(
        f"Загружено {len(picture_ids)} файлов", keyboard=GENERAL_STATISTICS_KEYBOARD)
    await bot.state_dispenser.set(message.peer_id, UploadState.NO_UPLOAD_STATE)


bot.run_forever()

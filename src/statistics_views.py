from vkbottle.bot import Message
from vkbottle.bot import Blueprint
from sqlalchemy.exc import IntegrityError

from src.keyboards import (
    ONTO_ANOTHER_PAGE,
    GENERAL_STATISTICS_KEYBOARD)
from src.memes_logic import grade_meme

from src.statistics_logic import (
    get_formatted_general_statistics,
    get_statistics,
    get_top_nine_memes
    )
from src.state_dispensers import MemeState, PagingState


bl = Blueprint()

IS_LIKE_MAPPING = {
    'Лайк': True,
    'Дизлайк': False
}

PAGE_OFFSET_MAPPING = {
    'Следующая страница': 1,
    'Предыдущая страница': -1
}


@bl.on.message(state=MemeState.MEME_SENT, text=['Лайк', 'Дизлайк'])
async def grade_meme_handler(message: Message):
    state_data = await bl.state_dispenser.get(message.peer_id)
    meme = state_data.payload.get('meme')

    is_like = IS_LIKE_MAPPING[message.text]
    try:
        await grade_meme(message.from_id, meme, is_like)
    except IntegrityError:
        return "Прости, но ты уже оценил этот мем"
    await message.answer(f"{message.text} поставлен")


@bl.on.message(text=['Посмотреть статистику'])
async def statistics_handler(message: Message):
    statistics_for_user = await get_statistics(message.from_id)
    dislikes, likes = statistics_for_user
    formatted_statistics = f'Количество ваших лайков {likes}, количество' +\
    f' ваших дизлайков {dislikes}'
    await message.answer(
        formatted_statistics, keyboard=GENERAL_STATISTICS_KEYBOARD)


@bl.on.message(text=['Посмотреть общую статистику'])
async def general_statistics_handler(message: Message):
    formatted_table = await get_formatted_general_statistics()
    formatted_table = f'Страница 1\n{formatted_table}'
    await bl.state_dispenser.set(
        message.peer_id, PagingState.PAGINATION_STATE, curpage=1)
    await message.answer(formatted_table, keyboard=ONTO_ANOTHER_PAGE)
    top_nine_memes = await get_top_nine_memes()
    memes = []
    grades = []
    for likes, file, _ in top_nine_memes:
        memes.append(file)
        grades.append(likes)
    print(memes)
    formatted_top = ""
    for idx, grade in enumerate(grades):
        formatted_top += f"{idx + 1} место {grade} лайков\n"
    await message.answer(
        message=formatted_top,
        attachment=memes,
        keyboard=GENERAL_STATISTICS_KEYBOARD)


@bl.on.message(
    text=['Следующая страница', 'Предыдущая страница'],
    state=PagingState.PAGINATION_STATE)
async def view_another_page(message: Message):
    previous_page = await bl.state_dispenser.get(message.peer_id)
    previous_page = previous_page.payload.get('curpage')

    offset = PAGE_OFFSET_MAPPING[message.text]
    curpage = previous_page + offset
    if curpage < 1:
        return "Это первая страница. Предыдущие страницы кончились"
    formatted_statistics = await get_formatted_general_statistics(
        page_number=curpage)

    if formatted_statistics is None or formatted_statistics == '':
        return "Это последняя страница. Дальше никого нет."
    formatted_statistics = f'Страница {curpage}\n{formatted_statistics}'
    await bl.state_dispenser.set(
        message.peer_id, PagingState.PAGINATION_STATE, curpage=curpage)
    print(formatted_statistics)

    await message.answer(formatted_statistics, keyboard=ONTO_ANOTHER_PAGE)

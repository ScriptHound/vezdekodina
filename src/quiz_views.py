from vkbottle.bot import Blueprint
from vkbottle.bot import Message

from src.state_dispensers import QuizStates
from src.keyboards import (
    WHICH_COLOR_DO_YOU_LIKE_MORE,
    DO_YOU_LIKE_VEZDEKOD,
    HOW_LONG_DO_YOU_CODE,
    WHICH_DIGIT_DO_YOU_LIKE_MORE,
    WHICH_IS_YOUR_EDUCATION,
    WHICH_IS_YOUR_SPECIALITY,
    WHICH_WEATHER_DO_YOU_LIKE_MORE,
    WHICH_WORK_TYPE_DO_YOU_LIKE,
    AFTER_QUIZ_KEYBOARD)


bl = Blueprint()


@bl.on.message(text="/квиз")
async def do_you_like_vezdekod_handler(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.QUESTION_ONE)
    await message.answer(
        "Нравится ли тебе вездекод?",
        keyboard=DO_YOU_LIKE_VEZDEKOD)


@bl.on.message(state=QuizStates.QUESTION_ONE)
async def how_long_do_you_code(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.QUESTION_TWO)
    await message.answer(
        "Как долго ты пишешь код?",
        keyboard=HOW_LONG_DO_YOU_CODE
    )


@bl.on.message(state=QuizStates.QUESTION_TWO)
async def which_is_your_speciality(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.QUESTION_THREE)
    await message.answer(
        "Какова твоя специализация",
        keyboard=WHICH_IS_YOUR_SPECIALITY
    )


@bl.on.message(state=QuizStates.QUESTION_THREE)
async def which_is_your_education(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.QUESTION_FOUR)
    await message.answer(
        "Расскажи о своём образовании",
        keyboard=WHICH_IS_YOUR_EDUCATION
    )


@bl.on.message(state=QuizStates.QUESTION_FOUR)
async def which_color_do_you_like(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.QUESTION_FIVE)
    await message.answer(
        "Выбери какой цвет тебе нравится больше",
        keyboard=WHICH_COLOR_DO_YOU_LIKE_MORE
    )



@bl.on.message(state=QuizStates.QUESTION_FIVE)
async def which_digit_do_you_like_more(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.QUESTION_SIX)
    await message.answer(
        "Какая цифра тебе нравится больше?",
        keyboard=WHICH_DIGIT_DO_YOU_LIKE_MORE
    )


@bl.on.message(state=QuizStates.QUESTION_SIX)
async def which_weather_do_you_like_more(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.QUESTION_SEVEN)
    await message.answer(
        "Какая погода тебе нравится больше?",
        keyboard=WHICH_WEATHER_DO_YOU_LIKE_MORE
    )


@bl.on.message(state=QuizStates.QUESTION_SEVEN)
async def which_work_type_do_you_like(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.GREETING_STATE)
    await message.answer(
        "Поздравляю, последний вопрос. Какой вид трудоустройства тебе нравится больше?",
        keyboard=WHICH_WORK_TYPE_DO_YOU_LIKE
    )


@bl.on.message(state=QuizStates.GREETING_STATE)
async def final_quiz_question(message: Message):
    await bl.state_dispenser.set(message.peer_id, QuizStates.QUIZ_COMPLETED)
    await message.answer(
        "Спасибо, что ответили на все вопросы!", keyboard=AFTER_QUIZ_KEYBOARD)

from vkbottle import Keyboard
from vkbottle import Keyboard, KeyboardButtonColor, Text

DO_YOU_LIKE_VEZDEKOD = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Да"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Нет"))
    .get_json()
)

HOW_LONG_DO_YOU_CODE = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Меньше года"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("От года до трёх лет"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("Больше трёх лет"), color=KeyboardButtonColor.PRIMARY)
    .get_json()
)

WHICH_IS_YOUR_SPECIALITY = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Backend"), color=KeyboardButtonColor.PRIMARY)
    .row()
    .add(Text("Frontend"), color=KeyboardButtonColor.PRIMARY)
    .row()
    .add(Text("Data Science"), color=KeyboardButtonColor.PRIMARY)\
    .row()
    .add(Text("DevOps"), color=KeyboardButtonColor.PRIMARY)
    .get_json()
)

WHICH_IS_YOUR_EDUCATION = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Университет"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Колледж"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("Школа"), color=KeyboardButtonColor.SECONDARY)\
    .add(Text("Самоучка"), color=KeyboardButtonColor.SECONDARY)
    .get_json()
)


WHICH_COLOR_DO_YOU_LIKE_MORE = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Зелёный"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Красный"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
)


WHICH_DIGIT_DO_YOU_LIKE_MORE = (
    Keyboard(one_time=True, inline=False)
    .add(Text("1"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("2"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("3"), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text("4"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("5"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("6"), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text("7"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("8"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("9"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
)


WHICH_DIGIT_DO_YOU_LIKE_MORE = (
    Keyboard(one_time=True, inline=False)
    .add(Text("1"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("2"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("3"), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text("4"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("5"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("6"), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text("7"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("8"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("9"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
)


WHICH_WEATHER_DO_YOU_LIKE_MORE = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Солнечная"), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text("Облачная"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("Дождь"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("Снег"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
)

WHICH_WORK_TYPE_DO_YOU_LIKE = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Фриланс"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("По ТК"), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text("Как самозанятый"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Как ИП"), color=KeyboardButtonColor.POSITIVE)
    .get_json()
)

DO_YOU_LIKE_MEME = (
    Keyboard(one_time=False, inline=True)
    .add(Text("Лайк"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Дизлайк"), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text("Скинь ещё"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Загрузи"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("Посмотреть статистику"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("Посмотреть общую статистику"), color=KeyboardButtonColor.SECONDARY)
    .get_json()
)


ONTO_ANOTHER_PAGE = (
    Keyboard(one_time=False, inline=True)
    .add(Text("Предыдущая страница"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Следующая страница"), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text("Скинь ещё"), color=KeyboardButtonColor.SECONDARY)
    .get_json()
)

GENERAL_STATISTICS_KEYBOARD = (
    Keyboard(one_time=False, inline=True)
    .add(Text("Скинь ещё"), color=KeyboardButtonColor.SECONDARY)
    .get_json()
)

AFTER_QUIZ_KEYBOARD = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Скинь мем"), color=KeyboardButtonColor.SECONDARY)
    .get_json()
)

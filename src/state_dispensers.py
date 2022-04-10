from vkbottle import BaseStateGroup


class MemeState(BaseStateGroup):
    MEME_SENT = 0
    MEME_GRADED = 1


class PagingState(BaseStateGroup):
    NO_PAGINATION_STATE = 0
    PAGINATION_STATE = 1

class UploadState(BaseStateGroup):
    NO_UPLOAD_STATE = 0
    UPLOADING_STATE = 1


class QuizStates(BaseStateGroup):
    GREETING_STATE = 0
    QUESTION_ONE = 1
    QUESTION_TWO = 2
    QUESTION_THREE = 3
    QUESTION_FOUR = 4
    QUESTION_FIVE = 5
    QUESTION_SIX = 6
    QUESTION_SEVEN = 7
    QUESTION_EIGHT = 8
    QUIZ_COMPLETED = 9

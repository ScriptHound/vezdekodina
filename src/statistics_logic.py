from string import Template

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from general_statistics_query import (
    GENERAL_STATISTICS_QUERY, TOP_NINE_MEMES)
from models import Likes
from db_init import engine


async def get_statistics(user_vk_id):
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        query = select(func.count(), Likes.is_liked)\
            .where(Likes.user_vk_id==user_vk_id).group_by(Likes.is_liked)
        result = await session.execute(query)
        result = {grade: count for count, grade in result.all()}
        dislikes = result.get(False, 0)
        likes = result.get(True, 0)
        return dislikes, likes


async def get_general_statistics(page_number: int = 1):
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        query = Template(GENERAL_STATISTICS_QUERY)
        query = query.substitute({
            'page': page_number,
            'page_size': 5
        })
        result = await session.execute(query)
        # the result comes in shape (true_count, false_count, vk_id)
        return result


async def get_formatted_general_statistics(page_number: int = 1):
    general_statistics = await get_general_statistics(page_number=page_number)
    general_statistics = [item for item in general_statistics]
    accumulating_string = ''
    for likes, dislikes, vk_id, full_name in general_statistics:
        if likes is None:
            likes = 0
        if dislikes is None:
            dislikes = 0
        accumulating_string += f"Лайки: {likes}, Дизлайки: {dislikes}"\
            + f", Имя: [id{vk_id}|{full_name}]\n"
    return accumulating_string


async def get_top_nine_memes():
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        result = await session.execute(TOP_NINE_MEMES)
        result = [item for item in result]
        return result

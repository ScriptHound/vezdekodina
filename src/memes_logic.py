from string import Template

from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from general_statistics_query import GRADES_OF_MEMES

from models import Meme, User, Likes
from db_init import engine


async def create_user_if_does_not_exist(engine, user_id, user_fullname):
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        query = select(User).where(User.vk_id==user_id)
        result = await session.execute(query)
        user = result.first()

        if user is not None:
            return

        user = User(full_name=user_fullname, vk_id=user_id)
        session.add(user)
        await session.commit()

        return user


async def select_random_meme(engine, user_vk_id):
    async_session = sessionmaker(
         engine, expire_on_commit=False, class_=AsyncSession
     )
    async with async_session() as session:
        query = text(
            "select memes.filepath, memes.id from memes "
            "where memes.id not in "
            "(select memes.id from memes "
            "inner join likes on likes.meme_id = memes.id "
            f"where user_vk_id = {user_vk_id}) order by random();")
        result = await session.execute(query)
        result = [item for item in result.all()][0]
        return result


async def grade_meme(user_vk_id, picture_name: str, is_like: bool):
    async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
    async with async_session() as session:
        query = select(Meme.id, User.id)\
            .where(
                Meme.filepath==picture_name,
                User.vk_id==user_vk_id)
        result = await session.execute(query)
        meme_id, _ = result.one()

        like = Likes(meme_id, user_vk_id, is_like)
        session.add(like)
        await session.commit()
        return like


async def create_memes(meme_ids):
    async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
    async with async_session() as session:
        for meme_id in meme_ids:
            meme = Meme(meme_id)
            session.add(meme)
        await session.commit()


async def get_meme_grades(meme_db_id):
    async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
    async with async_session() as session:
        query = Template(GRADES_OF_MEMES)
        query = query.substitute({
            'meme_db_id': meme_db_id
        })
        result = await session.execute(query)
        result = result.first()
        return result

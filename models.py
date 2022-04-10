from typing import List, Dict

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String)
    vk_id = Column(Integer, unique=True)

    def __init__(self, full_name: str, vk_id: int) -> None:
        self.full_name = full_name
        self.vk_id = vk_id


class Meme(Base):
    __tablename__ = 'memes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filepath = Column(String, unique=True)

    def __init__(self, filepath) -> None:
        self.filepath = filepath
    
    @classmethod
    def bulk_create(self, session, memes: List[Dict[str, str]]):
        """cards should be a list of dictionaries"""
        cards = [Meme(**meme) for meme in memes]
        session.bulk_save_objects(cards)


# a m2m table between Meme and User tables
class Likes(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    meme_id = Column(Integer)
    user_vk_id = Column(Integer)
    is_liked = Column(Boolean)
    __table_args__ = (
        UniqueConstraint('meme_id', 'user_vk_id', name='_meme_user_vk_id_uc'),
                     )
    
    def __init__(self, meme_id: int, user_vk_id: int, is_liked: bool) -> None:
        self.meme_id = meme_id
        self.user_vk_id = user_vk_id
        self.is_liked = is_liked

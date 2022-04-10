import os
from inspect import getfullargspec
from sqlalchemy.orm import session, sessionmaker

from db_init import sync_engine
from models import Meme

Session = sessionmaker(bind=sync_engine)
INIT_ARGS = 0


def get_filenames(dirpath: str):
    filenames = os.listdir(dirpath)
    filenames = [f'{dirpath}/{filename}' for filename in filenames]
    return filenames


if __name__ == '__main__':
    memes_list = []
    file_init_argument_name = getfullargspec(Meme.__init__)[INIT_ARGS][1]
    filenames = get_filenames('vezdekod_memes')
    filenames = [{file_init_argument_name: filename} for filename in filenames]

    conn = sync_engine.connect()
    session = Session(bind=conn)

    try:
        Meme.bulk_create(session, filenames)

        session.commit()
        print("Import complete")
    except Exception as e:
        session.rollback()
        print(f"Something gone wrong: {e}")
    finally:
        session.close()




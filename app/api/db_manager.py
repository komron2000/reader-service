from app.api.models import ReaderIn, ReaderOut
from app.api.db import readers, database


async def add_reader(payload: ReaderIn):
    query = readers.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_reader():
    query = readers.select()
    return await database.fetch_all(query=query)


async def get_reader(id):
    query = readers.select().where(readers.c.id == id)
    return await database.fetch_one(query=query)


async def delete_reader(id: int):
    query = readers.delete().where(readers.c.id == id)
    return await database.execute(query=query)


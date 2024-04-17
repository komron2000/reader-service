from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import ReaderOut, ReaderIn
from app.api import db_manager

readers = APIRouter()

@readers.post('/', response_model=ReaderOut, status_code=201)
async def create_reader(payload: ReaderIn):
    reader_id = await db_manager.add_reader(payload)

    response = {
        'id':reader_id,
        **payload.dict()
    }

    return response


@readers.get('/', response_model=List[ReaderOut])
async def get_readers():
    return await db_manager.get_all_reader()


@readers.get('/{id}/', response_model=ReaderOut)
async def get_reader(id: int):
    reader = await db_manager.get_reader(id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return reader


@readers.delete('/{id}/', response_model=None)
async def delete_reader(id: int):
    reader = await db_manager.get_reader(id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return await db_manager.delete_reader(id)
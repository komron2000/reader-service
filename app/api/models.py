from pydantic import BaseModel
from typing import List, Optional

class ReaderIn(BaseModel):
    name: str
    phone: str
    city: str
    age: int

class ReaderOut(ReaderIn):
    id: int

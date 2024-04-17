import pytest
from app.api.models import ReaderIn, ReaderOut


reader = ReaderIn(
    name='Pavel Durov',
    phone='+791234567',
    city='Moscow',
    age= 20
)


def test_create_reader(reader: ReaderIn = reader):
    assert dict(reader) == {'name': reader.name,
                              'phone': reader.phone,
                              'city': reader.city,
                              'age': reader.age
                              }


def test_update_reader_age(reader: ReaderIn = reader):
    reader_upd = ReaderOut(
        name='Pavel Durov',
        phone='+791234567',
        city='Moscow',
        age=20,
        id=1
    )
    assert dict(reader_upd) == {'name': reader.name,
                              'phone': reader.phone,
                              'city': reader.city,
                              'age': reader.age,
                              'id': reader_upd.id
                              }


def test_update_reader_city(reader: ReaderIn = reader):
    reader_upd = ReaderOut(
        name= reader.name,
        phone=reader.phone,
        city=reader.city,
        age=reader.age,
        id=1
    )
    assert dict(reader_upd) == {'name': reader.name,
                              'phone': reader.phone,
                              'city': reader.city,
                              'age': reader.age,
                              'id': reader_upd.id
                              }

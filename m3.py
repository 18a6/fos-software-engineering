from sqlalchemy import select
from sqlalchemy.orm import Session

from m1 import engine

session = Session(engine)

stmt = select(Book).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)
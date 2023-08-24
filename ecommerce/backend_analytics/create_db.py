from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import analytics_models
import os
import sys
print(os.environ)
# Option 1, using manual transaction
# engine = create_engine(f"postgresql://{username}:{password}@{host}/{database_name}")

# engine = create_engine(analytics_db_url)  # Using f"postgresql://{username}:{password}@{host}"
engine = create_engine(f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}/{os.environ['POSTGRES_DB']}")
# Session = sessionmaker(bind=engine)
conn = engine.connect()
# tables = [
#     analytics_models.Analytics,
#     analytics_models.Pages,
#     analytics_models.Clicks,
#     analytics_models.OS,
#     analytics_models.Browsers,
#     analytics_models.RawRequest
# ]
analytics_models.Base.metadata.create_all(engine)

# engine = create_engine(f"postgresql://{username}:{password}@{host}")

# conn = engine.connect()
# conn.execute("commit")
# conn.execute("create database analytics_db")
conn.close()



# Option 2, using automatic transaction
# with create_engine(
#     analytics_db_url,
#     isolation_level='AUTOCOMMIT'
# ).connect() as connection:
#     connection.execute('CREATE DATABASE analytics_db')









































# """
# from sqlalchemy.orm import sessionmaker
# database_url = 'postgresql://username:password@host/database_name'
# engine = create_engine(database_url)
# """

# engine = create_engine("postgres://postgres@/postgres")
# # engine = create_engine(f"postgresql://username:password@host/database_name")





# analytics_models.Base.metadata.create_all(engine)


# # Create
# from sqlalchemy.orm import Session
# with Session(engine) as session:
#     spongebob = User(
#         name="spongebob",
#         fullname="Spongebob Squarepants",
#         addresses=[Address(email_address="spongebob@sqlalchemy.org")],
#     )
#     sandy = User(
#         name="sandy",
#         fullname="Sandy Cheeks",
#         addresses=[
#             Address(email_address="sandy@sqlalchemy.org"),
#             Address(email_address="sandy@squirrelpower.org"),
#         ],
#     )
#     patrick = User(name="patrick", fullname="Patrick Star")
#     session.add_all([spongebob, sandy, patrick])
#     session.commit()

# # Select
# from sqlalchemy import select
# session = Session(engine)
# stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
# for user in session.scalars(stmt):
#     print(user)

# # Select with join
# stmt = (
#     select(Address)
#     .join(Address.user)
#     .where(User.name == "sandy")
#     .where(Address.email_address == "sandy@sqlalchemy.org")
# )
# sandy_address = session.scalars(stmt).one()

# # Update
# stmt = select(User).where(User.name == "patrick")
# patrick = session.scalars(stmt).one()
# patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
# sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"
# session.commit()

# # Delete
# sandy = session.get(User, 2)
# sandy.addresses.remove(sandy_address)
# session.flush()

# session.delete(patrick)
# session.commit()

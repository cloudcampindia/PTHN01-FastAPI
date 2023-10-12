from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# r -> RAW String
SQLALCHEMY_DATABASE_URI = r"sqlite:///C:\Users\akula\Desktop\cloudcamp\dbs"
engine = create_engine(url=SQLALCHEMY_DATABASE_URI)

# Every database has a Session associated with it inorder to perform transactions
# autocommit=False, indicates SQLAlchemy to perform transactions as a group
# If any of the transactions fails, the whole group will not be executed
session = sessionmaker(engine=engine, autoflush=False, autocommit=False)

# Using this parent class, we can extend it further to create our own classes
# for creating/modifying tables inside a database
Base = declarative_base()
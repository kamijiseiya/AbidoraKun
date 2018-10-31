from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
ENGINE = create_engine(
    'sqlite:///cash_cow.sqlite',
    encoding="UTF-8",
    echo=False
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = Session().query()


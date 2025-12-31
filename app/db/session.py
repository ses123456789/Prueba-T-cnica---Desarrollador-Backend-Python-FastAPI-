# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.core.config import settings

# DATABASE_URL = (
#     f"postgresql+psycopg2://{settings.DB_USER}:"
#     f"{settings.DB_PASSWORD}@{settings.DB_HOST}:"
#     f"{settings.DB_PORT}/{settings.DB_NAME}"
# )

# #engine = create_engine(DATABASE_URL, echo=True)
# engine = create_engine(
#     DATABASE_URL,
#     echo=True,
#     pool_pre_ping=True,
#     connect_args={"connect_timeout": 5},
# )
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


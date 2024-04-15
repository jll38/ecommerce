from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE as db_info
from colorama import Fore

DATABASE_URL = f"postgresql://{db_info['username']}:{db_info['password']}@{db_info['host']}:{db_info['port']}/{db_info['database']}"

Base = declarative_base()

def get_db_engine():
    try:
        engine = create_engine(DATABASE_URL, echo=True)
        return engine
    except Exception as e:
        print(f"{Fore.RED}Error creating database engine: {e}{Fore.WHITE}")
        return None

def get_db_session():
    engine = get_db_engine()
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    return Session()

def create_tables():
    engine = get_db_engine()
    Base.metadata.create_all(bind=engine)

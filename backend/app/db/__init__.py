from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE as db_info
from colorama import Fore

DATABASE_URL = f"postgresql://{db_info['username']}:{db_info['password']}@{db_info['host']}:{db_info['port']}/{db_info['database']}"

Base = declarative_base()

def get_db_engine():
    try:
        engine = create_engine(DATABASE_URL)
    except:
        print(f"{Fore.ERROR}Error creating database engine. {Fore.WHITE}")
    return engine

def get_db_session():
    engine = get_db_engine()
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session


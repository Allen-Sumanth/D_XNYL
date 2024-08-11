from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://root:welcome123@localhost:3306/d-xnyl'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()
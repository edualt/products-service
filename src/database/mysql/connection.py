from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("DB_URL"))

Base = declarative_base()

engine = create_engine(os.getenv("DB_URL"))
Base.metadata.create_all(bind=engine)
session_local = sessionmaker(bind=engine)




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from srk.main.api.configs.config import Config

engine = create_engine(Config.fetch('dataBaseURL'),echo=False)
SessionLocal = sessionmaker(bind=engine)

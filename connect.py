from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

url_to_db = "postgresql://postgres:pythonweb6@0.0.0.0:5432/postgres"
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
session = Session()

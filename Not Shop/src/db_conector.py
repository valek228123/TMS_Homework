from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqldb://root:кщще@localhost/general",pool_size= 1)
session_maker = sessionmaker(bind=engine)
session = session_maker()
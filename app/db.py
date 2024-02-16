from settings import settings
import urllib
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


driver = '{ODBC Driver 17 for SQL Server}'

params = urllib.parse.quote_plus(
    'Driver=%s;' % driver +
    'Server=tcp:%s,1433;' % settings.database_hostname +
    'Database=%s;' % settings.database_name +
    'Uid=%s;' % settings.database_username +
    'Pwd={%s};' % settings.database_password +
    'Encrypt=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=30;')

conn_str = 'mssql+pyodbc:///?odbc_connect=' + params

engine = create_engine(
    conn_str, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Model
class Productos(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    descripcion = Column(String)
    precio = Column(Float, default=True)
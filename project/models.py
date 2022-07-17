from sqlalchemy import Column, Integer, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects.postgresql import JSONB
import psycopg2

conn = psycopg2.connect(database="ar", user="ar",
    password="artur", host="localhost", port=5432)
cur = conn.cursor()


DATABASE_URL = "postgresql://ar:artur@localhost:5432/ar"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)


class Records(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    structure_id = Column(Integer)
    data = Column(JSONB, unique=True)
    created = Column(Integer)
    created_by = Column(Integer)
    updated = Column(Integer)
    updated_by = Column(Integer)


class Structures(Base):
    __tablename__ = 'structures'
    id = Column(Integer, primary_key=True)
    data = Column(JSONB, unique=True)
    created = Column(Integer)
    created_by = Column(Integer)
    updated = Column(Integer)
    updated_by = Column(Integer)


def add_to_db(data):
    # cur.execute("INSERT INTO {} {} VALUES (%s, %s, %s, %s, %s);".format(name,features),data)
    # cur.commit()
    s.add(data)
    s.commit()


def select_all(data):
   return s.query(data).all()


def select_needed(data,id):
    stmt = s.query(data).get(id)
    return stmt


def select_needed_records(data,id):
    stmt = s.query(data).filter(data.structure_id == id).all()
    return stmt


def update(data,id,val,name):
    s.query(data).filter(data.id == id).update({name: val})
    s.commit()


def delete_elem(data,id):
    s.query(data).filter(data.id == id).delete()
    s.commit()
    

Session = sessionmaker(bind=engine)
s = Session()

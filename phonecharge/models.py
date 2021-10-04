from sqlalchemy import Column, Integer, ForeignKey, String, DECIMAL, TIMESTAMP
import sqlalchemy as sqla
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects.postgresql import UUID
import uuid

from decouple import config

engine = create_engine(config("SQLALCHEMY_DATABASE_URI"))

conn = engine.connect()

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Company(Base):
    id = Column(String(50), primary_key=True)
    name = Column(String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.company_name}"

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Product(Base):
    id = Column(String(50), primary_key=True)
    public_id = Column(String(80), unique=True, nullable=False)
    value = Column(DECIMAL, nullable=False)
    comany_id = Column(
        ForeignKey("company.id"),
    )

    def __repr__(self):
        return f"{self.public_id}"


class Recharge(Base):
    id = Column(String(50), primary_key=True)
    public_id = Column(
        UUID(as_uuid=True, default=uuid.uuid4), unique=True, nullable=False
    )
    value = Column(DECIMAL, nullable=False)
    created_at = Column(TIMESTAMP)
    phone_number = Column(String(13))
    comany_id = Column(
        ForeignKey(Company, ondelete="RESTRICT"),
    )
    product_id = Column(
        ForeignKey(Product, ondelete="RESTRICT"),
    )

    def __repr__(self):
        return f"{self.public_id}"


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(300), nullable=False)

    def __repr__(self):
        return f"{self.public_id}"


def save(model_data):
    db_session.add(model_data)
    db_session.commit()


def delete(model_data):
    db_session.delete(model_data)
    db_session.commit()

from datetime import datetime
from decouple import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, create_engine, Column, String, ForeignKey, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, TIMESTAMP
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine(config('SQLALCHEMY_DATABASE_URI'))

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    public_id = Column(String(80), nullable=False, index=True)
    name = Column(String(80), nullable=False)
    product = relationship('Product', backref='company')

    def __repr__(self):
        return f'{self.public_id}'

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        try:
            company = session.query(Company).get(self.public_id)
            session.delete(company)
            session.commit()
        except Exception:
            pass


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    public_id = Column(String(80), nullable=False, index=True)
    value = Column(DOUBLE_PRECISION)
    company_id = Column(Integer, ForeignKey('companies.id'))
    recharge = relationship('Recharge', backref='product')

    def __repr__(self):
        return f'{self.public_id}'

    def save(self):
        company = session.query(Company.id).where(Company.public_id == self.company_id).first()
        print(f'company {company}')
        product = Product(public_id=self.public_id, company_id=company[0], value=self.value)
        session.add(product)
        session.commit()

    def delete(self):
        try:
            product = session.query(Product).get(self.public_id)
            session.delete(product)
            session.commit()
        except Exception:
            pass


class Recharge(Base):
    __tablename__ = 'recharges'
    id = Column(Integer, primary_key=True)
    public_id = Column(String(80), nullable=False, index=True)
    created_at = Column(TIMESTAMP, default=datetime.isoformat(datetime.now()))
    phone_number = Column(String(15))
    value = Column(DOUBLE_PRECISION)
    product_id = Column(Integer, ForeignKey('products.id'))

    def __repr__(self):
        return f'{self.public_id}'

    def save(self):
        product = session.query(Product.id).where(Product.public_id == self.product_id).first()
        print(f'product {product}')
        recharge = Recharge(public_id=self.public_id, product_id=product[0], value=self.value, phone_number=self.phone_number)
        session.add(recharge)
        session.commit()

    def delete(self):
        try:
            recharge = session.query(Recharge).get(self.public_id)
            session.delete(recharge)
            session.commit()
        except Exception:
            pass

def get_products():
    pass




def create_all():
    Base.metadata.create_all(bind=engine)




if __name__ == "__main__":
    create_all()

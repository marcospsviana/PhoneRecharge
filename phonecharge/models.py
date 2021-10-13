from datetime import datetime
from decouple import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, create_engine, Column, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, DECIMAL
from sqlalchemy.orm import sessionmaker, relationship
from passlib.context import CryptContext

engine = create_engine(config("SQLALCHEMY_DATABASE_URI"))

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.query = session.query()





class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    public_id = Column(String(80), nullable=False, index=True)
    name = Column(String(80), nullable=False)
    product = relationship("Product", backref="company")

    def __repr__(self):
        return f"{self.public_id}"

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        try:
            company = session.query(Company).get(self.product_id)
            session.delete(company)
            session.commit()
        except Exception:
            pass


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    public_id = Column(String(80), nullable=False, index=True)
    value = Column(DECIMAL)
    company_id = Column(Integer, ForeignKey("companies.id"))
    recharge = relationship("Recharge", backref="product")

    def __repr__(self):
        return f"{self.public_id}"

    def save(self):
        company = (
            session.query(Company.id)
            .where(Company.public_id == self.company_id)
            .first()
        )
        print(f"company {company}")
        product = Product(
            public_id=self.public_id, company_id=company[0], value=self.value
        )
        session.add(product)
        session.commit()
        return f"deleted {self.public_id}"

    def delete(self):
        try:
            product = session.query(Product).get(self.product_id)
            session.delete(product[0])
            session.commit()
        except Exception:
            pass


class Recharge(Base):
    __tablename__ = "recharges"
    id = Column(Integer, primary_key=True)
    public_id = Column(String(80), nullable=False, index=True)
    created_at = Column(TIMESTAMP, default=datetime.isoformat(datetime.now()))
    phone_number = Column(String(15))
    value = Column(DECIMAL)
    product_id = Column(Integer, ForeignKey("products.id"))

    def __repr__(self):
        return f"{self.public_id}"

    def save(self):
        recharge = Recharge(
            public_id=self.public_id,
            product_id=session.query(Product.id).filter(
                Product.public_id == self.product_id
            )[0][0],
            value=self.value,
            phone_number=self.phone_number,
        )
        try:
            session.add(recharge)
            session.commit()
            return True
        except Exception as err:
            return err

    def delete(self):
        try:
            recharge = session.query(Recharge).get(self.product_id)

            session.delete(recharge[0])
            session.commit()
        except Exception:
            pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(300), nullable=False, index=True)
    created_at = Column(TIMESTAMP, default=datetime.isoformat(datetime.now()))
    password = Column(String(500), nullable=False)

    def __repr__(self):
        return self.email

    def save(self):
        crypt_context = CryptContext(schemes=["sha256_crypt"])
        password = crypt_context.hash(self.password)
        user = User(email=self.email, password=password)
        session.add(user)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()


def get_products(id=None):
    if id is not None:
        products = (
            session.query(Company, Product.public_id, Product.value)
            .join(Company)
            .filter(Company.public_id == id)
            .all()
        )
        return {
            "company_id": f"{id}",
            "products": [
                {"id": product.public_id, "value": float(product.value)}
                for product in products
            ],
        }
    else:
        products_all = session.query(Product).all()
        company_all = session.query(Company).all()

        list_all = [
            {
                "company_id": f"{company.public_id}",
                "products": [
                    {"id": product.public_id, "value": float(product.value)}
                    for product in products_all
                    if product.company_id == company.id
                ],
            }
            for company in company_all
        ]

        return list_all


def create_all():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_all()

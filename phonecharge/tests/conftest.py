import uuid

import pytest

from phonecharge.base import create_app
from decouple import config

# from phonecharge.db.db_operations import save, delete
from phonecharge.models import Company, Product, Recharge
import factory

# from factory.alchemy import SESSION_PERSISTENCE_COMMIT as session
from sqlalchemy import orm, create_engine

engine = create_engine(config("SQLALCHEMY_DATABASE_URI"))
Session = orm.scoped_session(orm.sessionmaker(bind=engine))
from pytest_factoryboy import register


@register
class CompanyFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: n)
    public_id = factory.Sequence(lambda n: u"%s" % n)
    name = factory.Sequence(lambda n: u"%s" % n)

    class Meta:
        model = Company
        sqlalchemy_session = Session()


@register
class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
        # sqlalchemy_session = Session()
        # sqlalchemy_get_or_create = ("public_id", "value")

    id = factory.Sequence(lambda n: n)
    public_id = factory.Sequence(lambda n: u"%s" % n)
    value = factory.Sequence(lambda n: u"%d" % n)
    company_id = factory.SubFactory(CompanyFactory)

    class Meta:
        model = Product
        sqlalchemy_session = Session()


@register
class RechargeFactory(factory.alchemy.SQLAlchemyModelFactory):
        # sqlalchemy_session = Session()
        # sqlalchemy_get_or_create = (
        #     "public_id",
        #     "created_at",
        #     "phone_number",
        #     "value",
        # )

    id = factory.Sequence(lambda n: n)
    public_id = factory.Sequence(lambda n: u"%s" % n)
    phone_number = factory.Sequence(lambda n: u"%s" % n)
    value = factory.Sequence(lambda n: u"%d" % n)
    product_id = factory.RelatedFactoryList(ProductFactory)

    class Meta:
        model = Recharge
        sqlalchemy_session = Session()


@pytest.fixture(scope="session")
def app():
    return create_app()


# @pytest.fixture(scope="session")
# def db():
#     company = CompanyFactory()
#     product = ProductFactory()
#     recharge = RechargeFactory()

import pytest
from pytest_factoryboy import register
from phonecharge.base import create_app
from decouple import config


from phonecharge.models import Company, Product, Recharge, User
import factory

from sqlalchemy import orm, create_engine

engine = create_engine(config("SQLALCHEMY_DATABASE_URI"))
Session = orm.scoped_session(orm.sessionmaker(bind=engine))


@register
class CompanyFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Company
        sqlalchemy_session = Session()

    public_id = "claro_11"
    name = "claro"


@register
class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = Session()
        # sqlalchemy_session_persistence = "commit"

    public_id = "claro_10"  # factory.Sequence(lambda n: u"%s" % n)
    value = 10.0  # factory.Sequence(lambda n: u"%d" % n)
    company_id = 1  # factory.SubFactory(CompanyFactory)


@register
class RechargeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Recharge
        sqlalchemy_session = Session()
        # sqlalchemy_session_persistence = "commit"

    public_id = "284206977373282501394198671064916751422"  # factory.Sequence(lambda n: u"%s" % n)
    created_at = "2021-10-11T21:23:16.220005"
    phone_number = "5511969999999"  # factory.Sequence(lambda n: u"%s" % n)
    value = 20.0  # factory.Sequence(lambda n: u"%d" % n)
    product_id = "claro_20"  # factory.RelatedFactoryList(ProductFactory)


@register
class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = Session()
        # sqlalchemy_session_persistence = "commit"

    email = "marcospaulo.silvaviana@gmail.com"
    created_at = "2021-10-12T18:23:16.220005"
    password = "laylaebel"


@pytest.fixture(scope="session")
def app():
    return create_app()

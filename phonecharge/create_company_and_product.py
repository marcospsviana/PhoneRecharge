from models import Company, Product, User


def create():
    company = Company(public_id="claro_11", name="claro")
    company.save()
    company = Company(public_id="tim_11", name="tim")
    company.save()

    product = Product(public_id="claro_10", value=10.0, company_id="claro_11")
    product.save()

    product = Product(public_id="claro_20", value=20.0, company_id="claro_11")
    product.save()

    product = Product(public_id="tim_20", value=20.0, company_id="tim_11")
    product.save()

    product = Product(public_id="tim_10", value=10.0, company_id="tim_11")
    product.save()

    user = User(email="marcospaulo.silvaviana@gmail.com", password="laylaebel")
    user.save()


if __name__ == "__main__":
    create()

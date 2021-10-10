from phonecharge.models import Product, Recharge, session


def product(id=None):
    if id is not None:
        products = session.query(Company, Product.public_id, Product.value).join(Company).filter(Company.public_id == id).all()
        return {
        'company_id': f'{id}',
        'products': [{"id": product.public_id, "value": product.value} for product in products]
    }
    else:
        products_all = session.query(Product).all()
        company_all = session.query(Company).all()
        
        list_all = [{
            'company_id': f'{company.public_id}',
            'products': [
                {"id": product.public_id, "value": product.value} for product in products_all if product.company_id == company.id
                
            ]
        } for company in company_all ]
       
        return list_all


def recharge(phone_number=None):
    if phone_number is not None:
        products = session.query(Company.public_id, Product.public_id, Recharge).join(Company).filter(Company.public_id == id).all()
        return {
        'company_id': f'{id}',
        'products': [{"id": product.public_id, "value": product.value} for product in products]
    }
    else:
        products_all = session.query(Product).all()
        company_all = session.query(Company).all()
        
        list_all = [{
            'company_id': f'{company.public_id}',
            'products': [
                {"id": product.public_id, "value": product.value} for product in products_all if product.company_id == company.id
                
            ]
        } for company in company_all ]
       
        return list_all
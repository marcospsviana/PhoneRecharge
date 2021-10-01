from phonecharge.base import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'{self.username}'

class Company(db.Model):
    id_company = db.Column(db.String(50), primary_key=True)
    company_name = db.Column(db.String(80), unique=True, nullable=False)
    product_company = db.Column(db.Forei, unique=True, nullable=False)

    def __repr__(self):
        return f'{self.company_name}'
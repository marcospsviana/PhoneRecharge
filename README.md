## PHONE RECHARGE

[![codecov](https://codecov.io/gh/marcospsviana/PhoneRecharge/branch/main/graph/badge.svg?token=ptQEaccEnM)](https://codecov.io/gh/marcospsviana/PhoneRecharge)
[![Phone Recharge API](https://github.com/marcospsviana/PhoneRecharge/actions/workflows/phonecharge-app.yml/badge.svg)](https://github.com/marcospsviana/PhoneRecharge/actions/workflows/phonecharge-app.yml)


### **criação da estrutura inicial do projeto**

- criar o ambiente virtual

```
python3 -m venv .venv

```

- ativar o ambiente

```
source .venv/bin/activate
```

- instalar gerenciador de dependencias

```
pip install pip-tools
```

- criar o arquivos para compilação das dependencias

```
touch requirements.in requirements-dev.in
echo 'flask' > requirements.in
echo '-r requirements.in' > requirements-dev.in
```

- incluir dependencias de desenvolvimento em requirements-dev.in

```
-r requirements.in
pytest
coverage
black
flake8
pytest-flask
pytest-cov
codecov

```


- compilar as dependencias

```
pip-compile requirements.in --generate-hashes
pip-compile requirements-dev.in --generate-hashes
```

- instalar dependencias

```
pip install -r requirements-dev.txt
```

Populate database tables Company, Product 
~~~python
from phonecharge.models import Company, Product

def create():
    company = Company(public_id='claro_11', name='claro')
    company.save()
    company = Company(public_id='tim_11', name='tim')
    company.save()

    product = Product(public_id='claro_10', value=10.0, company_id='claro_11')
    product.save()

    product = Product(public_id='claro_20', value=20.0, company_id='claro_11')
    product.save()

    product = Product(public_id='tim_20', value=20.0, company_id='tim_11')
    product.save()

    product = Product(public_id='tim_10', value=10.0, company_id='tim_11')
    product.save()



if __name__ == '__main__':
    create()
~~~
**execute**
```
python phonecharge/operations/create_company_and_product.py
```

## API endpoints

Get all products

```
GET /CompanyProducts
```
headers 
~~~python
headers ={ 'Authorization': 'Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs' }
~~~
**Response**
~~~json
[
    {
        "company_id": "claro_11",
        "products": [
            {
                "id": "claro_10",
                "value": 10.0
            },
            {
                "id": "claro_20",
                "value": 20.0
            }
        ]
    },
    {
        "company_id": "tim_11",
        "products": [
            {
                "id": "tim_10",
                "value": 10.0
            },
            {
                "id": "tim_20",
                "value": 20.0
            }
        ]
    }
]
~~~



Get all recharges

```
GET /PhoneRecharges

```
headers 
~~~python
headers ={ 'Authorization': 'Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs' }
~~~
**Response**

~~~json
[
    {
        "id": "107802416839818990217276955951447063658",
        "created_at": "2021-10-08T08:25:16.518757",
        "company_id": "claro_11",
        "product_id": "tim_10",
        "phone_number": "5511999999999",
        "value": 10.0
    },
    {
        "id": "112631079329131080778876532853319043477",
        "created_at": "2021-10-11T08:03:27.277829",
        "company_id": "claro_11",
        "product_id": "claro_20",
        "phone_number": "5511999556699",
        "value": 20.0
    }
]

~~~

Get recharges by phone number
```
GET /PhoneRecharges?phone_number=5511969999999
```
headers 
~~~python
headers ={ 'Authorization': 'Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs' }
~~~
**Response**

~~~json
{
    "id": "284206977373282501394198671064916751422",
    "created_at": "2021-10-08T08:25:16.518757",
    "company_id": "claro_11",
    "product_id": "claro_20",
    "phone_number": "5511969999999",
    "value": 20.0
}
~~~

Get recharges by id recharge
```
GET /PhoneRecharges?id=112631079329131080778876532853319043477
```
headers 
~~~python
headers ={ 'Authorization': 'Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs' }
~~~
**Response**
~~~json
{
    "id": "112631079329131080778876532853319043477",
    "created_at": "2021-10-11T08:03:27.277829",
    "company_id": "claro_11",
    "product_id": "claro_20",
    "phone_number": "5511999556699",
    "value": 20.0
}
~~~



Create a new recharge

```
POST /PhoneRecharges
```

**Parameters**
headers 
~~~python
headers ={ 'Authorization': 'Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs' }
~~~

~~~json
{
"product_id": "claro_20",
"phone_number": "5511999556691",
"value": 20.0
}
~~~
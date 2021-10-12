## PHONE RECHARGE

[![codecov](https://codecov.io/gh/marcospsviana/PhoneRecharge/branch/main/graph/badge.svg?token=ptQEaccEnM)](https://codecov.io/gh/marcospsviana/PhoneRecharge)
[![Phone Recharge API](https://github.com/marcospsviana/PhoneRecharge/actions/workflows/phonecharge-app.yml/badge.svg)](https://github.com/marcospsviana/PhoneRecharge/actions/workflows/phonecharge-app.yml)

**Objetivo**
Problema: Recarga de telefônica Implementar uma API para permitir a compra de créditos telefônicos onde o usuário, após
informar o número à ser recarregado a compra será efetuada. Pesquisa por produtos O primeiro recurso que deve ser
implementado é o que irá permitir a manutenção (CRUD)
e busca por produtos compatíveis para serem utilizados na recarga. O mesmo deverá, em seu método GET, também receber um
parâmetro "company_id" e retornar um json com os produtos daquela companhia informada. Como no exemplo abaixo:
Exemplo 1.1: GET /CompanyProducts?company_id=claro_11




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

## API endpoints

Get all products

```
GET /CompanyProducts
```
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

~~~json
{
"product_id": "claro_20",
"phone_number": "5511999556691",
"value": 20.0
}
~~~
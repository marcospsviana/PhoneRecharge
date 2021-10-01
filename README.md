## PHONE RECHARGE

**Objetivo**
Problema: Recarga de telefônica Implementar uma API para permitir a compra de créditos telefônicos onde o usuário, após
informar o número à ser recarregado a compra será efetuada. Pesquisa por produtos O primeiro recurso que deve ser
implementado é o que irá permitir a manutenção (CRUD)
e busca por produtos compatíveis para serem utilizados na recarga. O mesmo deverá, em seu método GET, também receber um
parâmetro "company_id" e retornar um json com os produtos daquela companhia informada. Como no exemplo abaixo:
Exemplo 1.1: GET /CompanyProducts?company_id=claro_11

~~~json
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
}
~~~
Exemplo 1.2: GET /CompanyProducts

~~~json
[
{
  "company_id": "claro_11",
"products":[
{"id": "claro_10", "value": 10.0},
{"id": "claro_20", "value": 20.0}
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

Obs.: Os demais métodos, deverão seguir a mesma estrutura do payload indicado no exemplo 1.1. Efetivação da recarga O
segundo recurso deverá efetivar a recarga telefônica propriamente dita. Permitirá uma requisição POST com os dados
necessários para a recarga, bem como requisições GET para busca de dados, como nos exemplos abaixo:
Exemplo 2.1: POST /PhoneRecharges

~~~json
{
  "company_id": "claro_11",
  "product_id": "claro_10",
  "phone_number": "5511999999999",
  "value": 10.00
}
~~~

Exemplo 2.2: GET /PhoneRecharges?id=id_da_recarga

~~~json
{
  "id": "id_da_recarga",
  "created_at": "2019-02-01T13:00:00.000Z",
  "company_id": "claro_11",
  "product_id": "claro_10",
  "phone_number": "5511999999999",
  "value": 10.00
}
~~~

Exemplo 2.3: GET /PhoneRecharges?phone_number=5511999999999

~~~json
[
  {
    "id": "id_da_recarga",
    "created_at": "2019-02-01T13:00:00.000Z",
    "company_id": "claro_11",
    "product_id": "claro_10",
    "phone_number": "5511999999999",
    "value": 10.00
  },
  {
    "id": "id_da_recarga",
    "created_at": "2019-03-14T13:00:00.000Z",
    "company_id": "claro_11",
    "product_id": "claro_10",
    "phone_number": "5511999999999",
    "value": 10.00
  }
]


~~~
Obs.: Os demais métodos não deverão ser permitidos para este recurso.


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
pytest
flake8
black
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
**Estrutura do projeto**
```
/phonecharge
    base.py
    models.py
    /blueprints
        products.py
```
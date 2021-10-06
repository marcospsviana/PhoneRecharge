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
**Estrutura do projeto**
```
/phonecharge
    base.py
    models.py
    /blueprints
        products.py
    /tests
        conftest.py
        test_app.py
```


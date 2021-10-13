from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config  # config environment
from flask_migrate import Migrate
from flask_restful import Api
from phonecharge.api import CompanyProducts, Recharge


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_envvar(
        config("SECRET_KEY"),
        config("SQLALCHEMY_DATABASE_URI"),
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    api = Api(app)
    api.add_resource(
        CompanyProducts, "/CompanyProducts", provide_automatic_options=True
    )
    api.add_resource(Recharge, "/PhoneRecharges")

    migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app)

    return app


if __name__ == "__main__":
    create_app().run(debug=config("DEBUG", default=False, cast=bool))

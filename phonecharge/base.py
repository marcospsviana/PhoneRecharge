from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config  # config environment
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_envvar(
        config("SECRET_KEY"),
        config("SQLALCHEMY_DATABASE_URI"),
    )
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app)

    return app


if __name__ == "__main__":
    create_app().run(debug=config("DEBUG", default=False, cast=bool))

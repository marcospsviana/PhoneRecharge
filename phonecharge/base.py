from flask import Flask
from decouple import config


def create_app():
    app = Flask(__name__)
    app.config.from_envvar(SECRET_KEY=config("SECRET_KEY"), DATABASE=config('DATABASE'))

    return app


if __name__ == '__main__':
    create_app().run(debug=config('DEBUG', default=False, cast=bool))
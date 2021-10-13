from phonecharge.base import create_app
from decouple import config


if __name__ == "__main__":
    DEBUG = config("DEBUG", default=False, cast=bool)
    create_app.run(debug=DEBUG)

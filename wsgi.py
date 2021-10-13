from phonecharge.base import create_app


if __name__ == "__main__":
    DEBUG = config("DEBUG", default=False, cast=bool)
    create_app.run(debug=DEBUG)

import os
import requests

from flask import Flask, render_template


def read_access_key_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()  # .strip() removes any leading/trailing whitespace


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def home():
        return "Nada por aqui"

    @app.route("/products")
    def get_products():
        access_key = read_access_key_from_file("config.txt")
        headers = {"x-access-key": access_key}
        response = requests.get(
            "https://api.jsonbin.io/v3/b/65b3d105dc746540189b910d", headers=headers
        ).json()
        products = response["record"]["products"]
        print(products)
        return render_template("index.html", products=products)

    @app.route("/products/<id>")
    def get_product_by_id(id):
        return render_template("product_detail.html", id=id)

    return app

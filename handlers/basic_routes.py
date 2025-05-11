from flask import Flask
import os

def setup_basic_routes(app):
    @app.route("/")
    def hello_world():
        return "Hello, World!"

    @app.route("/testing")
    def testing():
        if os.environ.get('Testing_KEY') == "55645":
            return "key founded!"
        return "key not found!"
import app


def test_flask_imports():
    assert "Flask" in dir(app) and "render_template" in dir(app), \
        "The necessary flask utilities have not been imported into app.py, " \
        "please import with 'from flask import Flask, render_template'"

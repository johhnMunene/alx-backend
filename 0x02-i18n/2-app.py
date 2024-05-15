#!/usr/bin/env python3
"""Basic Flask app with Babel extension."""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    request.accept_languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def get_locale():
    """
    hello world
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)

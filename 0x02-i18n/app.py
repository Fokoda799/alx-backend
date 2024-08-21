#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
import datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user(login_as: int = None) -> dict:
    """ Returns: user dictionary or None if ID cannot be found """
    if login_as and int(login_as) in users:
        return users.get(int(login_as))


@babel.localeselector
def get_locale() -> str:
    """ get locale from request and return best match"""
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    if request.headers.get('locale') in app.config['LANGUAGES']:
        return request.headers.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ get timezone from request and return best match"""
    time = request.args.get('timezone')
    if time:
        try:
            return pytz.timezone(time)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            return pytz.timezone(g.user['timezone'])
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    """ find a user if any, and set it as a global on `g.user"""
    g.user = get_user(request.args.get('login_as'))


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Returns: 7-index.html """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == '__main__':
    """ Main Function"""
    app.run()

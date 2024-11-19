"""Initializes the Flask application."""

import contextlib
from pathlib import Path

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from tippyreloaded.config import CONF_FLASK, QUOTES


def create_app() -> Flask:
    """Create and configure the tippyreloaded app."""
    app = Flask(__name__, instance_relative_config=True)

    # load the test config if passed in
    app.config.from_object(CONF_FLASK)

    # ensure the instance folder exists
    with contextlib.suppress(OSError):
        Path(app.instance_path).mkdir(parents=True)

    # add rate limiting to the app
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["6 per minute"],
        storage_uri="memory://",
    )
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

"""Application's Module."""


from flask import Flask


def create_app():
    """Application Factory."""
    app = Flask(__name__)
    _register_configurations(app=app)
    _register_extensions(app=app)
    _register_modules(app=app)

    return app


def _register_configurations(app: Flask):
    from src.config import get_config_from_environment_variable

    app.config.from_object(get_config_from_environment_variable())


def _register_extensions(app: Flask):
    from src.extensions import __all__ as extensions

    for extension in extensions:
        extension.init_app(app=app)


def _register_modules(app: Flask):
    from src.modules import __all__ as modules

    for module in modules:
        app.register_blueprint(module)

"""Application's configuration."""

import os
from dotenv import load_dotenv

load_dotenv()


class Base:
    """Base Configuration Object."""

    pass


class Development:
    """Development Configuration Object."""

    pass


class Testing:
    """Testing Configuration Object."""

    pass


class Production:
    """Production Configuration Object."""

    pass


def get_config_from_environment_variable():
    """Get configuration object name from `CONF` env var and get lookup configuration object with the name."""
    config_name = os.getenv("CONF", "base")
    return {
        "base": Base,
        "dev": Development,
        "testing": Testing,
        "prod": Production,
    }.get(config_name.lower(), Base)

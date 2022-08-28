from pydantic import BaseSettings


ENV_PREFIX = 'TEST_'


class Settings(BaseSettings):
    # pylint: disable=too-few-public-methods
    HOST = "0.0.0.0"
    PORT = 8000
    ENABLE_AUTORELOAD = True
    WORKERS = 1

    class Config:
        # pylint: disable=too-few-public-methods
        env_prefix = ENV_PREFIX


settings = Settings()

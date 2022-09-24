from pydantic import BaseSettings

from pogo_api.version import __version__


class PogoSettings(BaseSettings):
    title: str
    docs_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class PogoConfig:
    def __init__(self) -> None:
        self.version = __version__
        self.settings = PogoSettings()

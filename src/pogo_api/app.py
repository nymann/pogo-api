from fastapi import FastAPI

from pogo_api.core.config import PogoConfig
from pogo_api.core.endpoint import Endpoint
from pogo_api.endpoints.upload import Upload


class PogoApi:
    def __init__(self, config: PogoConfig) -> None:
        self.config = config
        self.api = FastAPI(
            version=config.version,
            title=config.settings.title,
            docs_url=config.settings.docs_url,
        )
        self.add_endpoints()

    @property
    def endpoints(self) -> list[Endpoint]:
        return [Upload(config=self.config)]

    def add_endpoints(self) -> None:
        for endpoint in self.endpoints:
            endpoint.route.add_to_router(self.api)

from abc import ABC
from abc import abstractmethod
from collections.abc import Coroutine

from pogo_api.core.config import PogoConfig
from pogo_api.core.http import Method
from pogo_api.core.route import Route


class Endpoint(ABC):
    method = Method.GET

    def __init__(self, config: PogoConfig) -> None:
        self._name = self.__class__.__name__
        self.config = config
        self.settings = config.settings

    @property
    def path(self) -> str:
        name = self._name.lower()
        return f"/{name}"

    @abstractmethod
    async def endpoint(self) -> Coroutine:
        raise NotImplementedError()

    @property
    def route(self) -> Route:
        return Route(
            path=self.path,
            method=self.method,
            endpoint=self.endpoint,
            tag=self._name,
        )


class DeleteEndpoint(Endpoint):
    method = Method.DELETE


class GetEndpoint(Endpoint):
    method = Method.GET


class PatchEndpoint(Endpoint):
    method = Method.PATCH


class PostEndpoint(Endpoint):
    method = Method.POST


class PutEndpoint(Endpoint):
    method = Method.PUT


class UpdateEndpoint(Endpoint):
    method = Method.UPDATE

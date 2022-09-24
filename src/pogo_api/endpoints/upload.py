from pogo_api.core.endpoint import PostEndpoint


class Upload(PostEndpoint):
    async def endpoint(self, message: str) -> str:
        sender = self.settings.title
        return f"{sender} says: '{message}'."

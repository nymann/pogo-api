from pogo_api.app import PogoApi
from pogo_api.core.config import PogoConfig

app = PogoApi(config=PogoConfig()).api

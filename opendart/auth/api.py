from opendart.utils.singleton import Singleton

class DartAPI(metaclass=Singleton):

    def __init__(self) -> None:
        self._api_key = None

    @property
    def api_key(self) -> str:
        if self._api_key:
            return self._api_key
        else:
            raise ValueError('')

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        # TODO api_key validation
        self._api_key = api_key
    
    def __str__(self) -> str:
        return self.api_key
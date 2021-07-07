import requests
from zipfile import ZipFile
from io import BytesIO
from opendart.config import CORP_CODE_XML, CORP_CODE_LOCATION
from opendart.auth.api import DartAPI
from opendart.objects.corpcode import CorpCode
from opendart.utils.url import make_url


def get_corp_code_list() -> CorpCode:
    url = make_url(
        api_code=CORP_CODE_XML,
        crtfc_key=DartAPI().api_key
    )
    response = requests.get(url)
    response.raise_for_status()

    zf = ZipFile(BytesIO(response.content))
    path = zf.extract(zf.infolist()[0].filename, 'temp/')

    return CorpCode(path)


def load_corp_code_list(path: str = CORP_CODE_LOCATION) -> CorpCode:
    return CorpCode(path)
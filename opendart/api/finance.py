import requests
from opendart.config import SINGLE_FS_XML, QUATER_REPORT_KEYS, FS_DIV_KEYS
from opendart.auth.api import DartAPI
from opendart.objects.fs import FinancialStatement
from opendart.utils.url import make_url


def get_fs(corp: str, year: int, quater: int, div: int = 1) -> FinancialStatement:
    """
    Make API request of financial statement
    """

    url = make_url(
        api_code=SINGLE_FS_XML,
        crtfc_key=DartAPI().api_key,
        corp_code=corp,
        bsns_year=year,
        reprt_code=QUATER_REPORT_KEYS[quater],
        fs_div=FS_DIV_KEYS[div]
    )
    response = requests.get(url)
    response.raise_for_status()

    return FinancialStatement(response.text, corp, year, quater, div)
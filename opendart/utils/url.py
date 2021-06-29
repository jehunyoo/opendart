from opendart.config import BASE_URL


def make_url(api_code, base=BASE_URL, **kwargs) -> str:
    url = base + api_code + '?'
    for key, value in kwargs.items():
        url += f"{key}={value}&"
    return url
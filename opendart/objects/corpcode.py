from lxml.etree import parse
from opendart.utils.singleton import Singleton


class CorpCode(metaclass=Singleton):

    def __init__(self, path: str) -> None:
        self.path = path
        self.root = parse(self.path)

    def __len__(self):
        return len(self.root.findall('list'))

    def __str__(self) -> str:
        return self.path

    def find_code_by_name(self, name: str, kind: str = "corp") -> str or tuple(str, str):
        corp_code = self.root.xpath(f".//list[corp_name='{name}'][not(stock_code=' ')]/corp_code")[0].text
        stock_code = self.root.xpath(f".//list[corp_name='{name}'][not(stock_code=' ')]/stock_code")[0].text

        if kind == "corp":
            return corp_code
        elif kind == "stock":
            return stock_code
        else:
            return corp_code, stock_code

    def find_name_by_code(self, code: str) -> str:
        if len(code) == 8:
            corp_name = self.root.xpath(f".//list[corp_code='{code}'][not(stock_code=' ')]/corp_name")[0].text
        elif len(code) == 6:
            corp_name = self.root.xpath(f".//list[stock_code='{code}']/corp_name")[0].text
        else:
            raise ValueError("Invalid code.")
        
        return corp_name
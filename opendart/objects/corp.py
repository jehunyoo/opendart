from os.path import isfile
from opendart.config import CORP_CODE_LOCATION
from opendart.objects.fs import FinancialStatement
from opendart.api.finance import get_fs
from opendart.api.corp import get_corp_code_list, load_corp_code_list

class Corporation:

    def __init__(self, name: str = None, code: str = None) -> None: # TODO use stock code
        if name is None and code is None:
            raise ValueError
        elif name and code:
            self.name = name
            self.code = code
        else:
            if isfile(CORP_CODE_LOCATION):
                corp_list = load_corp_code_list()
            else:
                corp_list = get_corp_code_list()
            
            if name is None:
                self.name = corp_list.find_name_by_code(code)
                self.code = code
            elif code is None:
                self.code = corp_list.find_code_by_name(name)
                self.name = name

        self.fs = {}
    
    def __str__(self) -> str:
        return f"{self.name}: {self.code}"  

    def get_fs(self, year: int, quater: int, div: int = 1) -> FinancialStatement:
        return get_fs(self.code, year, quater, div)

    def load_fs(self, year: int, quater: int, div: int = 1, request: bool = True) -> None:
        if request:
            if div == 1:
                self.fs[f"{year}+{quater}"] = get_fs(self.code, year, quater, div)
            elif div == 0:
                self.fs[f"{year}-{quater}"] = get_fs(self.code, year, quater, div)
        else: #TODO load fs from local storage
            if div == 1:
                pass
            elif div == 0:
                pass
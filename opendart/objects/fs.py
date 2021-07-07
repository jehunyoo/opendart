from typing import List
from xml.etree.ElementTree import fromstring
from opendart.config import ITEM_ID, TERM_KEYS, STATEMENT_KEYS, INVERSE_STATEMENT_KEYS
from opendart.objects.item import Item
from opendart.utils.xml import check_status


class FinancialStatement:

    def __init__(self, fs: str, corp: str, year: int, quater: int, div: int) -> None:
        self.fs = fs
        self.corp = corp
        self.year = year
        self.quater = quater
        self.div = div

        check_status(self.fs)
        self.root = fromstring(self.fs)

    def __str__(self) -> str:
        if self.div == 1:
            return f"Consolidated Financial Statement of {self.corp}@{self.year}-{self.quater}"
        elif self.div == 0:
            return f"Separate Financial Statement of {self.corp}@{self.year}-{self.quater}"

    def find(self, item: str, term: int = 0, by: str = 'id') -> Item:
        if term not in [0, 1, 2]:
            raise ValueError("Invalid term.")

        if by == 'id':
            item_id = ITEM_ID[item]
            return Item(
                self.root.findtext(f".//list[account_id='{item_id}']/{TERM_KEYS[term]}"),
                STATEMENT_KEYS[self.root.findtext(f".//list[account_id='{item_id}']/sj_div")] + ':' + item,
                item_id
            )
        elif by == 'name':
            try:
                div, item = item.split(':')
                div = INVERSE_STATEMENT_KEYS[div]
            except:
                div = None
            
            try:
                item_id = ITEM_ID[item]
            except:
                item_id = None

            if div:
                return Item(
                    self.root.findtext(f".//list[account_nm='{item}'][sj_div='{div}']/{TERM_KEYS[term]}"),
                    div + ':' + item,
                    item_id
                )
            else:
                return Item(
                    self.root.findtext(f".//list[account_nm='{item}']/{TERM_KEYS[term]}"),
                    STATEMENT_KEYS[self.root.findtext(f".//list[account_nm='{item}']/sj_div")] + ':' + item,
                    item_id
                )
    
    def findall(self, items: list, term: int = 0) -> List[Item]:
        item_list = []
        for item in items:
            item_list.append(self.find(item, term))
        
        return item_list
    
    def search(self, item: str) -> None:
        result = []
        for element in self.root.findall('list'):
            name = element.findtext('account_nm')
            if item in name:
                result.append(STATEMENT_KEYS[element.findtext('sj_div')] + ':' + name)
        print(f"{len(result)} results, {result}")
    
    def get_all_itmes(self):
        return [
            element.findtext('sj_div') + ':' + element.findtext('account_nm')
            for element in self.root.findall('list')
        ]

    def save(self) -> str:
        pass # return path
class Item:

    def __init__(self, value: str, name: str, id_: str) -> None:
        self.n = self.name = name
        self.v = self.value = int(value)
        self.i = self.id_ = id_
    
    def __str__(self) -> str:
        return self.name, self.value
    
    def __add__(self, another) -> int:
        return self.value + another.value
    
    def __sub__(self, another) -> int:
        return self.value - another.value
    

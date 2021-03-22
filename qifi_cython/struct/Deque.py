from collections import deque
import numpy as np
import pandas as pd

class DequeDict():
    def __init__(self, fields: dict):
        self.__fields = fields
        self.__data = {key:deque() for key in self.__fields}
        self.__change = True

    def index(self, key: str, value, start: int = 0, stop: int = -1) -> int:
        return self.__data[key].index(value, start, stop if stop>0 else len(self.__data[key]))

    def count(self, key: str, value) -> int:
        return self.__data[key].count(value)
    
    def append(self, values: dict):
        self.__change = True
        for key in self.__fields.keys():
            self.__data[key].append(values.get(key, np.nan))
        return self
    
    def update(self, index: int, values: dict):
        self.__change = True
        for key, value in values.items():
            if key in self.__data:
                self.__data[key][index] = value
        return self
    
    def get(self, index: int) -> dict:
        return {key:self.__data[key][index] for key in self.__fields.keys()}

    @property
    def values(self) -> np.rec.array :
        if self.__change is True:
            self.__values = np.rec.fromarrays(
                arrayList=np.array(object=list(self.__data.values())), 
                dtype=list(self.__fields.items())
                )
            self.__change = False
        return self.__values

    def to_pandas(self, index: str = '') -> pd.core.frame.DataFrame :
        if index in self.__fields:
            return pd.DataFrame(data=self.values, index=self.__data[index])
        else:
            return pd.DataFrame(data=self.values)

    def to_dict(self, index: str = '') ->dict :
        return self.to_pandas(index).T.to_dict()


class Deque2D(DequeDict):
    def __init__(self, index: str, fields: dict):
        self.__index = index
        super().__init__(fields)

    def index(self, value) -> int:
        return super().index(self.__index, value)

    def count(self, value) -> int:
        return super().value(self.__index, value)
    
    def update(self, index, values: dict):
        return super().update(self.index(index), values)
    
    def get(self, index) -> dict:
        return super().get(self.index(index))

    def to_pandas(self) -> pd.core.frame.DataFrame :
        return super().to_pandas(self.__index)

    def to_dict(self) ->dict :
        return self.to_pandas().T.to_dict()
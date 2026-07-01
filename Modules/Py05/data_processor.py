from abc import ABC, abstractmethod
from typing import Any

type Number = int | float

class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[tuple[int, str]] = []
        self.index: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise Exception("No data to output")
        return self.data.pop(0)

class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                for item in data
            )
        return False
    
    def ingest(self, data: Number | list[Number]) -> None:
        if not self.validate(data):
            raise Exception("Invalid Numeric data")
        
        items: list[Number] = data if isinstance(data, list) else [data]

        for item in items:
            self.data.append((self.index, str(item)))
            self.index += 1

class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        
        if isinstance(data, list):
            return all(
                isinstance(item, str)
                for item in data
            )
        return False
    
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Invalid Text data")
        
        items: list[str] = data if isinstance(data, list) else [data]

        for item in items:
            self.data.append((self.index, item))
            self.index += 1

class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in data.items()
        ):
            return True
        
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items())
                for item in data
            )
        return False
    
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Invalid Log data")
        
        items: list[dict[str, str]] = data if isinstance(data, list) else [data]

        for item in items:
            self.data.append((self.index, str(item)))
            self.index += 1

def main():
    try:
        num1 = NumericProcessor()

        num1.ingest(10)
        num1.ingest([1,23,3,4])
        print(num1.output())
        print(num1.output())
        print(num1.output())
        # num1.ingest([1,23,3,'4'])

        str1 = TextProcessor()

        str1.ingest('hello')
        str1.ingest(['w', 'o', 'r', 'l', 'd'])
        print(str1.output())
        print(str1.output())
        # str1.ingest(1)

        dict1 = LogProcessor()

        dict1.ingest({'k1':'v1'})
        dict1.ingest([{'k2':'v2'}, {'k3':'v3'}, {'k4':'v4'}])
        print(dict1.output())
        print(dict1.output())
        print(dict1.output())
        # dict1.ingest([{'k2':'v2'}, {4:'v3'}, {'k4':'v4'}])

    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()
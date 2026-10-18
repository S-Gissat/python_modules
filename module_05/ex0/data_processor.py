from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]]
        self._rank: int

        self._data = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(i, (int, float)) for i in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for i in data:
                self._data.append((self._rank, str(i)))
                self._rank += 1
        else:
            self._data.append((self._rank, str(data)))
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for i in data:
                self._data.append((self._rank, i))
                self._rank += 1
        else:
            self._data.append((self._rank, data))
            self._rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            if "log_level" not in data or "log_message" not in data:
                return False
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        elif isinstance(data, list):
            for i in data:
                if not isinstance(i, dict):
                    return False
                if "log_level" not in i or "log_message" not in i:
                    return False
                for key, value in i.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        log_str: str

        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for i in data:
                log_str = f"{i['log_level']}: {i['log_message']}"
                self._data.append((self._rank, log_str))
                self._rank += 1
        else:
            log_str = f"{data['log_level']}: {data['log_message']}"
            self._data.append((self._rank, log_str))
            self._rank += 1


def test_validation(processor: DataProcessor, data: typing.Any) -> None:
    result = processor.validate(data)
    print(f"Trying to validate input {data!r}: {result}")

 
if __name__ == "__main__":
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    test_validation(numeric, 42)
    test_validation(numeric, "Hello")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5,])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    test_validation(text, "Hello")
    test_validation(text, 42)
    print("Processing text data...")
    text.ingest(["Hello", "Code", "Nexus"])
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = text.output()
        print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    test_validation(log,
                    {"log_level": "NOTICE",
                     "log_message": "Connection to server"})
    test_validation(log, 42)
    print("Processing log data...")
    log.ingest([
        {"log_level": "NOTICE",
         "log_message": "Connection to server"},
        {"log_level": "ERROR",
         "log_message": "Unauthorized access!!"}
    ])
    print("Extracting log entries...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")

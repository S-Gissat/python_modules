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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [i for rank, i in data]
        csv_str = ",".join(values)
        print("CSV Output:")
        print(csv_str)


def escape_json(value: str) -> str:
    value = value.replace("\\", "\\\\")
    value = value.replace('"', '\\"')
    value = value.replace("\n", "\\n")
    value = value.replace("\r", "\\r")
    value = value.replace("\t", "\\t")
    return value


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        data_parts: list[str]
        json_data: str

        data_parts = []
        for rank, value in data:
            escaped_value = escape_json(value)
            data_parts.append(f'"item_{rank}": "{escaped_value}"')
        json_data = ", ".join(data_parts)
        json_data = "{" + json_data + "}"
        print("JSON Output:")
        print(json_data)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        processed: bool

        for i in stream:
            processed = False
            for j in self._processors:
                if j.validate(i):
                    j.ingest(i)
                    processed = True
                    break
            if not processed:
                print("DataStream error - "
                      f"Can't process element in stream: {i}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for i in self._processors:
            name = type(i).__name__.replace("Processor", " Processor")
            print(f"{name}: total {i._rank} items processed, "
                  f"remaining {len(i._data)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        output_data: list[tuple[int, str]]

        for i in self._processors:
            output_data = []
            for _ in range(min(nb, len(i._data))):
                output_data.append(i.output())
            plugin.process_output(output_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    data = ["Hello world",
            [3.14, -1, 2.71],
            [{"log_level": "WARNING",
              "log_message": "Telnet access! Use ssh instead"},
             {"log_level": "INFO",
              "log_message": "User wil is connected"}],
            42,
            ["Hi", "five"]]
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    data = [21,
            ["I love AI", "LLMs are wonderful", "Stay healthy"],
            [{"log_level": "ERROR",
              "log_message": "500 server crash"},
              {"log_level": "NOTICE",
               "log_message": "Certificate expires in 10 days"}],
               [32, 42, 64, 84, 128, 168],
               "World hello"]
    print(f"Send another batch of data: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()

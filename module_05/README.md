# Python Module 05 — Code Nexus

## Overview

This module focuses on **abstract classes, inheritance, polymorphism, method overriding, protocols, and duck typing**.

The project gradually builds a small data-processing pipeline capable of handling different types of input through a common interface.

The final architecture can:

- validate different types of data,
- route mixed data streams to the appropriate processor,
- store and consume processed values,
- track processing statistics,
- and export processed data through interchangeable CSV and JSON plugins.

The module demonstrates how different classes can participate in the same workflow without the surrounding code needing to know their exact implementation.

---

## Concepts Covered

- Abstract Base Classes (`ABC`)
- Abstract methods
- Inheritance
- Method overriding
- Polymorphism
- Runtime type validation
- Type annotations
- `typing.Any`
- `typing.Protocol`
- Duck typing
- Internal object state
- Data routing
- Processing queues
- Plugin architecture
- CSV formatting
- Manual JSON formatting
- Exception handling

---

## Exercise Progression

| Exercise | File | Main Concept |
|---|---|---|
| 0 | `data_processor.py` | Abstract processors and inheritance |
| 1 | `data_stream.py` | Polymorphic stream processing |
| 2 | `data_pipeline.py` | Protocols, duck typing, and export plugins |

---

# Exercise 0 — Data Processor

The first exercise introduces a common processor architecture using an abstract base class.

The abstract `DataProcessor` class defines the interface shared by all specialized processors.

It contains:

```python
validate(self, data: Any) -> bool
ingest(self, data: Any) -> None
output(self) -> tuple[int, str]
```

`validate()` and `ingest()` are abstract methods and must therefore be implemented by every specialized processor.

`output()` is shared by all processors and returns the oldest stored value.

---

## Processor Types

Three specialized processors inherit from `DataProcessor`.

### NumericProcessor

Accepts:

- `int`
- `float`
- lists containing integers and floats

Example:

```python
[1, 2.5, -3, 4.2]
```

Each numeric value is converted to a string before being stored.

---

### TextProcessor

Accepts:

- `str`
- `list[str]`

Example:

```python
["Hello", "Code", "Nexus"]
```

Each string is stored separately.

---

### LogProcessor

Processes structured log dictionaries.

This implementation expects entries containing:

```python
{
    "log_level": "ERROR",
    "log_message": "Server crash"
}
```

They are converted into strings such as:

```text
ERROR: Server crash
```

Lists containing multiple log dictionaries can also be processed.

---

## Internal Storage

All processors use the same internal structure:

```python
list[tuple[int, str]]
```

Each processed value receives a rank:

```python
[
    (0, "42"),
    (1, "3.14"),
    (2, "100")
]
```

The rank represents the order in which individual values were processed.

Calling:

```python
processor.output()
```

removes and returns the oldest stored item.

---

## Validation and Ingestion

Validation and ingestion are intentionally separated.

Example:

```text
validate()
    ↓
Can this processor handle the data?
    ↓
True / False
```

`ingest()` performs the actual processing.

Each `ingest()` implementation also validates its input internally so that invalid data cannot be silently accepted.

Invalid direct ingestion raises a `ValueError`.

---

# Exercise 1 — Polymorphic Data Stream

The second exercise introduces the `DataStream` class.

Instead of manually choosing a processor, mixed input data can now be routed automatically.

Example stream:

```python
[
    "Hello world",
    [3.14, -1, 2.71],
    [
        {
            "log_level": "WARNING",
            "log_message": "Telnet access! Use ssh instead"
        }
    ],
    42,
    ["Hi", "five"]
]
```

The stream contains several completely different data types.

---

## Registering Processors

Processors are registered using:

```python
register_processor(self, proc: DataProcessor) -> None
```

Internally, `DataStream` stores them in a list:

```python
self._processors: list[DataProcessor]
```

Because every specialized processor inherits from `DataProcessor`, they can all be stored and handled through the same interface.

---

## Stream Processing

The method:

```python
process_stream(self, stream: list[typing.Any]) -> None
```

iterates over every element in the stream.

Each registered processor is asked:

```python
processor.validate(element)
```

The first processor that accepts the element receives it through:

```python
processor.ingest(element)
```

This means `DataStream` does not need to know whether a processor is numeric, textual, or log-based.

It only relies on the shared `DataProcessor` interface.

This is the central example of **polymorphism** in the module.

---

## Processing Statistics

`DataStream` can display statistics for every registered processor.

Example:

```text
Numeric Processor: total 8 items processed, remaining 5 on processor
Text Processor: total 3 items processed, remaining 1 on processor
Log Processor: total 2 items processed, remaining 1 on processor
```

Two different pieces of information are tracked:

### Total processed

The processor rank increases whenever a new item is ingested.

It therefore represents the total number of individual values processed.

### Remaining

The current number of stored values is determined through:

```python
len(processor._data)
```

Calling `output()` decreases the number of remaining items without changing the total number already processed.

---

# Exercise 2 — Data Pipeline

The final exercise extends the input-processing architecture with an output pipeline.

The complete flow becomes:

```text
Mixed Input Data
       ↓
   DataStream
       ↓
Data Processors
       ↓
    output()
       ↓
Output Pipeline
       ↓
Export Plugin
       ↓
 CSV / JSON
```

---

## ExportPlugin Protocol

Instead of using another inheritance hierarchy, export plugins use:

```python
typing.Protocol
```

The protocol defines:

```python
process_output(
    self,
    data: list[tuple[int, str]]
) -> None
```

Any class implementing a compatible `process_output()` method can therefore be used as an export plugin.

Unlike the `DataProcessor` hierarchy, the plugin does not need to explicitly inherit from `ExportPlugin`.

This demonstrates **duck typing**.

---

## CSV Export Plugin

The CSV plugin receives processed tuples such as:

```python
[
    (0, "3.14"),
    (1, "-1"),
    (2, "2.71")
]
```

Only the values are exported.

Result:

```text
CSV Output:
3.14,-1,2.71
```

The processor ranks are intentionally ignored for CSV output.

---

## JSON Export Plugin

The JSON plugin uses both parts of each tuple.

Example:

```python
[
    (3, "42"),
    (4, "21"),
    (5, "32")
]
```

becomes:

```json
{"item_3": "42", "item_4": "21", "item_5": "32"}
```

The JSON string is created manually instead of using a JSON library.

Special characters can be escaped before being inserted into the final JSON string to keep the generated output valid.

---

## Output Pipeline

The final `DataStream` method is:

```python
output_pipeline(
    self,
    nb: int,
    plugin: ExportPlugin
) -> None
```

For every registered processor it:

1. determines how many values can be consumed,
2. calls `output()` repeatedly,
3. stores the resulting tuples,
4. sends them to the selected export plugin.

The number of consumed values is limited using:

```python
min(nb, len(processor._data))
```

This prevents the pipeline from attempting to consume more elements than a processor currently contains.

---

## Duck Typing

The pipeline can use either plugin through the same call:

```python
stream.output_pipeline(3, csv_plugin)
```

or:

```python
stream.output_pipeline(5, json_plugin)
```

`DataStream` does not contain special logic such as:

```python
if plugin is CSV:
    ...
elif plugin is JSON:
    ...
```

Instead it simply calls:

```python
plugin.process_output(data)
```

As long as the object provides the required method, it can participate in the pipeline.

---

## Architecture

```text
                    DataProcessor
                         │
          ┌──────────────┼──────────────┐
          │              │              │
 NumericProcessor  TextProcessor   LogProcessor
          │              │              │
          └──────────────┼──────────────┘
                         │
                     DataStream
                         │
                  output_pipeline()
                         │
                    ExportPlugin
                         │
                 ┌───────┴───────┐
                 │               │
          CSVExportPlugin   JSONExportPlugin
```

---

## Repository Structure

```text
module05/
├── ex0/
│   └── data_processor.py
├── ex1/
│   └── data_stream.py
└── ex2/
    └── data_pipeline.py
```

Each exercise builds on the architecture introduced in the previous one.

---

## Running the Exercises

Exercise 0:

```bash
python3 ex0/data_processor.py
```

Exercise 1:

```bash
python3 ex1/data_stream.py
```

Exercise 2:

```bash
python3 ex2/data_pipeline.py
```

---

## Code Quality

The module uses type annotations throughout the processor and pipeline architecture.

Before submission, the files can be checked with:

```bash
flake8 data_processor.py
mypy data_processor.py
```

```bash
flake8 data_stream.py
mypy data_stream.py
```

```bash
flake8 data_pipeline.py
mypy data_pipeline.py
```

Exercise 0 intentionally contains a direct invalid `ingest()` test that may produce a `mypy` warning because invalid data is deliberately passed to a specialized processor.

---

## Key Takeaways

This module demonstrates the difference between several related object-oriented concepts.

### Inheritance

Specialized processors inherit shared behavior from `DataProcessor`.

### Method overriding

Each processor implements its own version of `validate()` and `ingest()`.

### Polymorphism

`DataStream` can handle every processor through the same `DataProcessor` interface without knowing its concrete class.

### Abstract Base Classes

`DataProcessor` defines behavior that all subclasses are required to implement.

### Protocols

`ExportPlugin` defines the behavior required from export plugins without requiring an explicit inheritance relationship.

### Duck Typing

CSV and JSON plugins are accepted because they provide the expected `process_output()` method.

---

## Final Pipeline

By the end of the module, the program can process mixed data through a common workflow:

```text
Input
  ↓
Validation
  ↓
Automatic Processor Selection
  ↓
Ingestion
  ↓
Internal Ranked Storage
  ↓
Output
  ↓
CSV / JSON Export
```

The result is a small but flexible data-processing architecture where new processors or export plugins can be added without rewriting the entire workflow.
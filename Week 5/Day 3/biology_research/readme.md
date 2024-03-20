# Rabbit Simulation System

The Rabbit Simulation System is a program that simulates the population dynamics of rabbits. It generates records of rabbit births and deaths over time, and manages these records using a data handler. The system is designed to handle errors that may occur during data read/write operations.

## Modules

### `data_handler.py`

#### Classes:
- **DataHandler:** Manages data read/write operations and error handling.
  - **Methods:**
    - `write_to_json(record: Record)`: Writes a record to a JSON file.
    - `read_from_json()`: Reads records from a JSON file.
    - `write_to_file(record: Record, path)`: Writes a record to a specified file path.
    - `read_from_file(path)`: Reads records from a specified file path.
    - `make_replica()`: Creates a replica of a JSON file.
    - `merge_json_files(file1, file2)`: Merges data from two JSON files.
    - `overwrite_file(records)`: Overwrites a file with new records.

### `errors.py`

#### Classes:
- **Errors:** Handles error generation during data read/write operations.
  - **Methods:**
    - `generate_read_error()`: Generates read errors with increasing probability.
    - `generate_write_error()`: Generates write errors with increasing probability.

### `record.py`

#### Classes:
- **Record:** Represents a record of rabbit population data.
  - **Attributes:**
    - `_timestamp`: Timestamp of the record.
    - `_deaths_num`: Number of rabbit deaths.
    - `_births_num`: Number of rabbit births.
  - **Methods:**
    - `get_timestamp()`: Returns the timestamp of the record.
    - `get_deaths()`: Returns the number of rabbit deaths.
    - `get_births()`: Returns the number of rabbit births.

### `simulation.py`

#### Classes:
- **Simulation:** Simulates rabbit population dynamics.
  - **Attributes:**
    - `_rabbits_num`: Current number of rabbits.
    - `_num_of_inserted_records`: Number of inserted records.
    - `_max_num_records`: Maximum number of records.
  - **Methods:**
    - `get_rabbits_num()`: Returns the current number of rabbits.
    - `add_rabbits_num(number)`: Increases the current number of rabbits by the specified amount.
    - `get_inserted()`: Returns the number of inserted records.
    - `increment_inserted()`: Increments the number of inserted records.
    - `simulation()`: Runs the rabbit population simulation.

## Testing

Unit tests are included for the `Record` and `Simulation` classes to ensure their functionality. These tests cover various methods and attributes of the classes.

![biology research diagram drawio](https://github.com/najeebib/Backend-bootcamp-exercises/assets/79699737/f57765f1-aea4-43d0-b188-704d3d73a11a)

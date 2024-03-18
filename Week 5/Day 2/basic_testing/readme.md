# Raffle System

The Raffle System is a simple application that facilitates raffle events. It allows people to buy tickets for the raffle, and then randomly selects a winner from the pool of participants.

## Modules

### `person.py`

#### Classes:
- **Person:** Represents an individual participating in the raffle.
  - **Attributes:**
    - `_num_of_tickets`: Number of tickets owned by the person.
    - `_name`: Name of the person.
  - **Methods:**
    - `get_num_of_tickets()`: Returns the number of tickets owned by the person.
    - `get_name()`: Returns the name of the person.
    - `add_ticket()`: Increases the ticket count by one.

### `raffle.py`

#### Classes:
- **Raffle:** Manages the raffle event.
  - **Attributes:**
    - `_people`: List of participants.
    - `_tickets`: Total number of tickets sold.
    - `_max_people`: Maximum number of participants allowed.
    - `_max_tickets`: Maximum number of tickets available for purchase.
    - `_total_earnings`: Total amount earned from ticket sales.
    - `_ticket_price`: Price of each ticket.
  - **Methods:**
    - `get_people()`: Returns the list of participants.
    - `get_tickets()`: Returns the total number of tickets sold.
    - `get_max_people()`: Returns the maximum number of participants allowed.
    - `get_max_tickets()`: Returns the maximum number of tickets available.
    - `get_total_earnings()`: Returns the total earnings from ticket sales.
    - `get_ticket_price()`: Returns the price of each ticket.
    - `buy_ticket(person: Person)`: Allows a person to buy a ticket for the raffle.
    - `select_winner()`: Randomly selects a winner from the participants.

### `test_person.py`

#### Classes:
- **TestPerson:** Unit tests for the `Person` class.
  - **Methods:**
    - `setup_method()`: Sets up the test environment.
    - `test_person_get_tickets()`: Tests the `get_num_of_tickets()` method.
    - `test_person_tickets_int()`: Tests if the number of tickets returned is an integer.
    - `test_add_ticket()`: Tests the `add_ticket()` method.

### `test_raffle.py`

#### Classes:
- **TestRaffle:** Unit tests for the `Raffle` class.
  - **Methods:**
    - `setup_method()`: Sets up the test environment.
    - Various test methods to validate the functionality of `Raffle` class methods.

## Testing

The application includes unit tests for both the `Person` and `Raffle` classes to ensure the functionality of the system. You can run the tests using the appropriate testing framework.


![Untitled Diagram drawio](https://github.com/najeebib/Backend-bootcamp-exercises/assets/79699737/856b63c4-7eb7-4596-8957-2fa5747b4786)


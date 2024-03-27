# Ticket Selling System

The Ticket Selling System is a Python program that simulates a ticket selling service. It consists of various modules responsible for generating ticket requests, processing these requests, managing ticket inventory, and testing the functionality of the system.

## Modules

### `ticket.py`

Contains the `Ticket` class, which represents a ticket with attributes such as ID, price, event, and sold status. It provides methods to retrieve and update ticket information.

### `request.py`

Defines the `Request` class, representing a ticket purchase request. It includes information such as timestamp, event, and the number of tickets requested.

### `request_stream.py`

Includes the `RequestGenerator` class responsible for generating random ticket purchase requests at specified time intervals.

### `ticket_generator.py`

Generates ticket objects with random attributes for testing purposes.

### `server.py`

Implements the `Server` class, which simulates a server responsible for processing ticket requests, managing ticket inventory, and handling concurrency.

### `load_balancer.py`

Not implemented in this project but could be used to distribute requests across multiple servers for scalability.

### `test_ticket.py` and `test_request.py`

Contain unit tests for the `Ticket` and `Request` classes, respectively, ensuring their functionality.

### Data consistency
In this project I want to use strict consistency, every read operation must return the most recent write operation
every time the server sells a ticket it reads the database and when the ticket is sold the database is updated
this way the databse is up to date all the time
the downside of this approach is that it takes a lot of network traffic to read and write everytime

I implemented it in the server code
with open(self.tickets_file, 'r') as f:
            self.tickets_db = json.load(f)
everytime the server handles a request it gets the most recent databses
![ticket system diagram drawio](https://github.com/najeebib/Backend-bootcamp-exercises/assets/79699737/32100e07-52c2-4599-b185-4704ebb8a3ee)

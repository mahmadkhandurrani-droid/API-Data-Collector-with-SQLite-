# API-Data-Collector-with-SQLite-
A modular Python automation project that fetches data from a REST API, validates responses, handles errors and timeouts, parses JSON data, stores records in a SQLite database, and logs operations. Built using Python, Requests, SQLite, JSON, and object-oriented programming.
API Data Collector with SQLite

Overview

API Data Collector with SQLite is a modular Python automation project that retrieves data from a REST API and stores it in a SQLite database. The project demonstrates how to integrate web APIs with databases using clean, modular, and object-oriented Python code. It also includes configuration management, logging, timeout handling, and exception handling to simulate real-world automation workflows.

Features

- Fetches data from a REST API using GET requests.
- Parses JSON responses into Python objects.
- Stores API data in a SQLite database.
- Creates database tables automatically.
- Uses configuration values from a JSON file.
- Handles API errors and request timeouts.
- Logs important operations and errors.
- Modular architecture for easy maintenance and future expansion.

Project Structure

API_Data_Collector/
│── main.py
│── api_client.py
│── database.py
│── logger.py
│── config.json
│── collector.db
└── README.md

Technologies Used

- Python
- Requests
- SQLite
- JSON
- Logging
- Object-Oriented Programming (OOP)

Workflow

1. Load configuration from "config.json".
2. Connect to the SQLite database.
3. Create the required database table.
4. Send a GET request to the REST API.
5. Validate the response and parse JSON data.
6. Store records in SQLite.
7. Display saved records.
8. Log successful operations and errors.
9. Close the database connection.

Learning Objectives

This project demonstrates practical skills in REST API integration, SQLite database management, JSON processing, exception handling, logging, modular software design, and Python automation.

Future Improvements

- Retry logic with exponential backoff.
- Authentication using API tokens.
- CSV and Excel export.
- Command-line interface using "argparse".
- Unit testing with "pytest".
- Support for multiple API endpoints.
- Automatic scheduling for data collection.

License

This project is licensed under the MIT License.

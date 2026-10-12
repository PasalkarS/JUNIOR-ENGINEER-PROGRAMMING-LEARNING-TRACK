# Inventory Management System

## Overview

A beginner-friendly Python application for managing inventory using SQLite.

## Features

- Add and view product categories.
- Add, view, search, filter, update, and delete products.
- Validate product information.
- Calculate total inventory value.
- Identify low-stock products.
- Generate category reports.
- Store records in a local SQLite database.

## Requirements

- Python 3.10 or newer recommended.
- No external packages required.

## How to Run

From the project root, execute:

```bash
python src/main.py
```

The database is created automatically inside the `data` directory.

## Run Tests

From the project root, run:

```bash
python -m unittest discover -s tests -v
```

## Project Structure

- `data/`: SQLite database.
- `docs/`: Database design and recovery instructions.
- `src/`: Application source code.
- `tests/`: Automated tests.

## Learning Objectives

- SQL CRUD operations.
- Python SQLite connections and parameterized queries.
- Primary keys, foreign keys, constraints, and indexes.
- Input validation and repository design.
- Searching, filtering, and reporting.
- Database testing and recovery.

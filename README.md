# Tasky - A Simple CLI Task Manager

Tasky is a lightweight command-line tool for managing your daily tasks.

## Features
- Add tasks
- List tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage (JSON)

## Usage
`python -m tasky.cli add "Buy groceries"`
`python -m tasky.cli list`
`python -m tasky.cli complete 1`
`python -m tasky.cli delete 1`

## Running Tests
`python -m unittest discover tests`

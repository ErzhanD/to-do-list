CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER DEFAULT 0,
    deadline DATE
    )
"""

INSERT_TASK = """
    INSERT INTO tasks (task, deadline) VALUES (?, ?)
"""

SELECT_TASKS = """SELECT id, task, completed, deadline FROM tasks"""
SELECT_TASKS_completed = "SELECT id, task, completed, deadline FROM tasks WHERE completed = 1"
SELECT_TASKS_uncompleted = "SELECT id, task, completed, deadline FROM tasks WHERE completed = 0"

DELETE_TASK = """
    DELETE FROM tasks WHERE id = ?
"""

UPDATE_TASK = """
    UPDATE tasks SET task = ? WHERE id = ?
"""

UPDATE_DEADLINE = "UPDATE tasks SET deadline = ? WHERE id = ?"
import sqlite3
from db import queries
from config import db_path



def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASKS)
    print('База данных подключена!')
    conn.commit()
    conn.close()



def get_tasks(filter_type='all'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # cursor.execute(queries.SELECT_TASKS)
    if filter_type == 'completed':
        cursor.execute(queries.SELECT_TASKS_completed)
    elif filter_type == 'uncompleted':
        cursor.execute(queries.SELECT_TASKS_uncompleted)
    else:
        cursor.execute(queries.SELECT_TASKS)
    
    print(filter_type)

    tasks = cursor.fetchall()
    conn.close()
    return tasks


def add_task(task, deadline=None):
    if len(task) > 100:
        print("Ошибка: новая задача слишком длинная (больше 100 символов)")
        return None
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_TASK, (task, deadline))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def delete_task(task_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()


def update_task(task_id, new_task=None, completed=None, deadline=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # cursor.execute(queries.UPDATE_TASK, (new_task, task_id))

    if new_task is not None:
        if len(new_task) > 100:
            print("Ошибка: новая задача слишком длинная (больше 100 символов)")
            conn.close()
            return
        cursor.execute(queries.UPDATE_TASK, (new_task, task_id))
    
    if completed is not None:
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))

    if deadline is not None:
        cursor.execute(queries.UPDATE_DEADLINE, (deadline, task_id))
    conn.commit()
    conn.close()
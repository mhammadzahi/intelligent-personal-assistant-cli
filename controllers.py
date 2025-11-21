from typing import List, Optional
from database import get_connection
from models import Task, Note, Reminder
from nlp_utils import summarize_text
from datetime import datetime

class TaskController:
    @staticmethod
    def add_task(title: str, category: str = "general") -> Task:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, category) VALUES (?, ?)", (title, category))
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return Task(id=task_id, title=title, category=category)

    @staticmethod
    def get_all_tasks() -> List[Task]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        conn.close()
        return [Task(**dict(row)) for row in rows]

    @staticmethod
    def delete_task(task_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_status(task_id: int, status: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        conn.commit()
        conn.close()

class NoteController:
    @staticmethod
    def add_note(title: str, content: str) -> Note:
        summary = summarize_text(content)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content, summary) VALUES (?, ?, ?)", (title, content, summary))
        note_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return Note(id=note_id, title=title, content=content, summary=summary)

    @staticmethod
    def get_all_notes() -> List[Note]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        rows = cursor.fetchall()
        conn.close()
        return [Note(**dict(row)) for row in rows]
    
    @staticmethod
    def delete_note(note_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def search_notes(query: str) -> List[Note]:
        conn = get_connection()
        cursor = conn.cursor()
        search_query = f"%{query}%"
        cursor.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?", (search_query, search_query))
        rows = cursor.fetchall()
        conn.close()
        return [Note(**dict(row)) for row in rows]

class ReminderController:
    @staticmethod
    def add_reminder(title: str, due_date: str) -> Reminder:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reminders (title, due_date) VALUES (?, ?)", (title, due_date))
        reminder_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return Reminder(id=reminder_id, title=title, due_date=due_date)

    @staticmethod
    def get_all_reminders() -> List[Reminder]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reminders")
        rows = cursor.fetchall()
        conn.close()
        return [Reminder(**dict(row)) for row in rows]

    @staticmethod
    def delete_reminder(reminder_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_due_reminders() -> List[Reminder]:
        conn = get_connection()
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        cursor.execute("SELECT * FROM reminders WHERE due_date <= ? AND status = 'pending'", (now,))
        rows = cursor.fetchall()
        conn.close()
        return [Reminder(**dict(row)) for row in rows]

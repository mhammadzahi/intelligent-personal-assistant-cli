from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: Optional[int]
    title: str
    category: str
    status: str = 'pending'
    created_at: Optional[str] = None

@dataclass
class Note:
    id: Optional[int]
    title: str
    content: str
    summary: Optional[str] = None
    created_at: Optional[str] = None

@dataclass
class Reminder:
    id: Optional[int]
    title: str
    due_date: str
    status: str = 'pending'
    created_at: Optional[str] = None

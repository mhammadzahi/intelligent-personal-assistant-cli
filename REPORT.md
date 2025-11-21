# Intelligent Personal Assistant (CLI) - Project Report

## 1. Architecture
The project follows a modular **MVC (Model-View-Controller)** architecture to ensure separation of concerns and maintainability.

### Modules
- **`main.py`**: The entry point and **View** layer. It handles user input via `argparse` and renders output using `rich`.
- **`controllers.py`**: The **Controller** layer. It contains business logic for Tasks, Notes, and Reminders, mediating between the database and the view.
- **`models.py`**: The **Model** layer. It defines Python dataclasses (`Task`, `Note`, `Reminder`) representing the data entities.
- **`database.py`**: Handles SQLite database connection and table initialization.
- **`nlp_utils.py`**: Encapsulates the **spaCy** NLP logic for text summarization.
- **`notifications.py`**: Handles checking for due reminders and displaying alerts.
- **`utils.py`**: Helper functions for date parsing and formatting.

## 2. Features Implemented

### Mandatory Features
- **Tasks**: Add, list, delete, mark as done. Categorization (work, personal, etc.) is supported.
- **Data Persistence**: Uses **SQLite** (`assistant.db`) for robust storage.
- **Notes**: Create, list, delete, and search notes.
- **Automatic Summarization**: Uses **spaCy** to generate summaries for notes.

### Advanced/Bonus Features
- **Notifications**: Console alerts for due reminders when the application runs.
- **Task Categories**: Tasks can be assigned categories.
- **Intelligent Search**: Notes can be searched by title or content.
- **Rich CLI**: Uses the `rich` library for beautiful tables, panels, and colored output.

## 3. How the Summarizer Works
The summarization logic is implemented in `nlp_utils.py` using **spaCy**:
1.  **Tokenization**: The text is processed into tokens (words/sentences).
2.  **Frequency Analysis**: Word frequencies are calculated, excluding stop words and punctuation.
3.  **Scoring**: Sentences are scored based on the frequency of significant words they contain.
4.  **Selection**: The top sentences (default 30%) are selected to form the summary.

## 4. How to Run the Program

### Prerequisites
- Python 3.x (Tested with 3.11)
- Dependencies: `rich`, `spacy`, `en_core_web_sm` model.

### Installation
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Usage
**Tasks**
```bash
python main.py task add "Buy milk" --category personal
python main.py task list
python main.py task done <ID>
python main.py task delete <ID>
```

**Notes**
```bash
python main.py note add "Title" "Long content..."
python main.py note list
python main.py note search "keyword"
```

**Reminders**
```bash
python main.py reminder add "Meeting" "2025-11-22 14:00"
python main.py reminder list
```

## 5. How to Extend
- **Email Notifications**: Implement the `smtplib` logic in `notifications.py` to send emails for due reminders.
- **Recurring Reminders**: Add a `recurrence` field to the `reminders` table and update logic in `controllers.py`.
- **Web Interface**: The `controllers.py` and `models.py` can be reused with a web framework like Flask or FastAPI.

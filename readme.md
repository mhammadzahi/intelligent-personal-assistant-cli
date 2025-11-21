## Intelligent Personal Assistant (CLI)

A command-line personal assistant built in Python that manages tasks, reminders, and notes, with automatic summarization and intelligent search.


## Features

### Task Management

* Add tasks
* Edit tasks
* Delete tasks
* Mark tasks as done or undone
* Categorize tasks (work, studies, personal)
* List tasks by category or status

### Reminders

* Create reminders with date and time
* Persistent storage
* Console notifications
* Optional email notifications

### Notes and Summaries

* Create notes
* Edit notes
* Delete notes
* Automatic summarization using NLTK or spaCy
* Intelligent search by keyword, date, or partial match

### Data Persistence

* SQLite3 (recommended) or JSON
* Stores tasks, notes, and reminders


## Project Structure

```
assistant/
│── main.py
│── cli.py
│── database.py
│── models/
│   ├── task.py
│   ├── reminder.py
│   └── note.py
│── controllers/
│   ├── task_controller.py
│   ├── reminder_controller.py
│   └── note_controller.py
│── utils/
│   ├── summarizer.py
│   ├── notifier.py
│   └── helpers.py
│── data/
│   └── assistant.db  (or data.json)
│── docs/
│   └── report.md
```


## Installation

### 1. Clone the project

```
git clone https://github.com/mhammadzahi/intelligent-personal-assistant-cli.git
cd intelligent-personal-assistant-cli
```

### 2. Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### spaCy model (optional)

```
python -m spacy download en_core_web_sm
```

### NLTK data (optional)

```
python -c "import nltk; nltk.download('punkt')"
```


## Usage

Run the assistant:

```
python main.py
```

Example commands:

```
python cli.py add-task "Finish project" --category work
python cli.py list-tasks
python cli.py add-note "This is a long note..."
python cli.py search-notes "meeting"
```

---

## Summarization

The assistant supports:

* spaCy summarization
* NLTK summarization

The summarizer extracts key sentences and keywords to create a short, meaningful summary.


## Notifications

### Console notifications

Reminders are periodically checked and displayed in the console.

### Email notifications (optional)

Configure a `.env` file:

```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```


## Documentation

The full project report is located in:

```
docs/report.md
```



## Extensibility

Possible future improvements:

* Voice input
* GUI version
* FastAPI REST API
* Cloud sync



## Contributing

Pull requests and issue reports are welcome.



## License

MIT License.

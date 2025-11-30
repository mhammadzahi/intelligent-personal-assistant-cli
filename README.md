# Intelligent Personal Assistant CLI

A powerful command-line personal assistant that helps you manage tasks, notes, and reminders with AI-powered text summarization.

## Features

- 📝 **Task Management**: Create, list, complete, and delete tasks with categories
- 📓 **Note Taking**: Add notes with automatic AI-powered summarization using NLP
- ⏰ **Reminders**: Set time-based reminders with console notifications
- 🔍 **Search**: Search through your notes efficiently
- 🎨 **Rich CLI**: Beautiful terminal interface with tables and panels

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mhammadzahi/intelligent-personal-assistant-cli.git
cd intelligent-personal-assistant-cli
```

2. Create and activate a virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the spaCy language model (if not auto-downloaded):
```bash
python -m spacy download en_core_web_sm
```

## Usage

### Task Management

#### Add a Task
```bash
python main.py task add "Buy groceries"
python main.py task add "Complete project report" --category work
```

#### List All Tasks
```bash
python main.py task list
```

#### Mark Task as Done
```bash
python main.py task done 1
```

#### Delete a Task
```bash
python main.py task delete 1
```

### Note Management

#### Add a Note
The assistant will automatically generate a summary using NLP:
```bash
python main.py note add "Meeting Notes" "Today we discussed the Q4 roadmap. Key points include launching the new feature by December, hiring two more developers, and increasing marketing budget. The team agreed on the timeline."
```

#### List All Notes
```bash
python main.py note list
```

#### Search Notes
Search through note titles and content:
```bash
python main.py note search "roadmap"
python main.py note search "meeting"
```

#### Delete a Note
```bash
python main.py note delete 1
```

### Reminder Management

#### Add a Reminder
Reminders use the format `YYYY-MM-DD HH:MM`:
```bash
python main.py reminder add "Doctor appointment" "2025-12-15 10:30"
python main.py reminder add "Call mom" "2025-12-01 18:00"
```

#### List All Reminders
```bash
python main.py reminder list
```

#### Delete a Reminder
```bash
python main.py reminder delete 1
```

#### Reminder Notifications
Reminders are automatically checked when you run the application. If any reminders are due, they will be displayed as console notifications.

## Project Structure

```
intelligent-personal-assistant-cli/
├── main.py              # CLI entry point and command handling
├── controllers.py       # Business logic for tasks, notes, and reminders
├── models.py           # Data models (Task, Note, Reminder)
├── database.py         # SQLite database connection and initialization
├── nlp_utils.py        # NLP text summarization utilities
├── notifications.py    # Reminder notification system
├── utils.py            # Helper functions (date parsing, formatting)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Data Storage

The application uses SQLite for data persistence. The database file (`assistant.db`) is automatically created in the project directory on first run.

### Database Schema

**Tasks Table:**
- `id`: Primary key
- `title`: Task title
- `category`: Task category (default: "general")
- `status`: Task status ("pending" or "done")
- `created_at`: Timestamp

**Notes Table:**
- `id`: Primary key
- `title`: Note title
- `content`: Full note content
- `summary`: AI-generated summary
- `created_at`: Timestamp

**Reminders Table:**
- `id`: Primary key
- `title`: Reminder title
- `due_date`: Due date and time
- `status`: Reminder status ("pending")
- `created_at`: Timestamp

## Examples

### Complete Workflow Example

```bash
# Add some tasks
python main.py task add "Prepare presentation" --category work
python main.py task add "Go to gym" --category personal
python main.py task add "Review pull requests" --category work

# List all tasks
python main.py task list

# Mark a task as done
python main.py task done 1

# Add a detailed note with auto-summarization
python main.py note add "Project Ideas" "We brainstormed several ideas for the next quarter. First, implementing a mobile app version of our platform. Second, adding AI-powered recommendations. Third, improving the onboarding experience with interactive tutorials. The team was most excited about the AI features."

# List notes to see the summary
python main.py note list

# Search for specific notes
python main.py note search "AI"

# Set reminders
python main.py reminder add "Team standup" "2025-12-01 09:00"
python main.py reminder add "Submit timesheet" "2025-12-01 17:00"

# List reminders
python main.py reminder list

# Delete completed items
python main.py task delete 1
python main.py note delete 1
python main.py reminder delete 1
```

## Features in Detail

### AI-Powered Summarization

When you add a note, the application uses spaCy's NLP capabilities to:
1. Analyze the text content
2. Calculate word frequencies (excluding stop words)
3. Score sentences based on important keywords
4. Extract the most relevant sentences
5. Generate a concise summary

This helps you quickly review your notes without reading the entire content.

### Task Categories

Organize your tasks with custom categories:
- `work`: Professional tasks
- `personal`: Personal errands
- `shopping`: Shopping lists
- `general`: Miscellaneous tasks (default)

### Reminder Notifications

The application checks for due reminders every time it's launched. If any reminders have passed their due date, they'll be displayed prominently in a notification panel.

## Dependencies

- **rich**: Beautiful terminal formatting and tables
- **spacy**: Natural language processing for text summarization
- **en_core_web_sm**: English language model for spaCy

## Tips

1. **Use quotes** for multi-word arguments:
   ```bash
   python main.py task add "This is a multi-word task"
   ```

2. **Date format** for reminders must be `YYYY-MM-DD HH:MM`:
   ```bash
   python main.py reminder add "Meeting" "2025-12-25 14:30"
   ```

3. **Search is case-insensitive** and searches both titles and content:
   ```bash
   python main.py note search "project"
   ```

4. **Task IDs** are displayed when listing - use them for done/delete operations

## Troubleshooting

### spaCy Model Not Found
If you get an error about missing spaCy model:
```bash
python -m spacy download en_core_web_sm
```

### Import Errors
Make sure you've activated the virtual environment:
```bash
source env/bin/activate  # On Windows: env\Scripts\activate
```

### Database Errors
If you encounter database issues, you can delete `assistant.db` to start fresh (this will delete all your data).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Mohammad Hammad Zahi (@mhammadzahi)

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

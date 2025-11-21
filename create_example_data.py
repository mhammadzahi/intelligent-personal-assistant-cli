from database import init_db
from controllers import TaskController, NoteController, ReminderController
from datetime import datetime, timedelta

def create_data():
    init_db()
    
    # Tasks
    print("Adding tasks...")
    TaskController.add_task("Buy groceries", "personal")
    TaskController.add_task("Finish project report", "work")
    TaskController.add_task("Call mom", "personal")
    TaskController.add_task("Study for exam", "studies")
    
    # Notes
    print("Adding notes...")
    long_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans.
    Leading AI textbooks define the field as the study of "intelligent agents": any system that perceives its environment and takes actions that maximize its chance of achieving its goals.
    Some popular accounts use the term "artificial intelligence" to describe machines that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving", however this definition is rejected by major AI researchers.
    AI applications include advanced web search engines (e.g., Google), recommendation systems (used by YouTube, Amazon and Netflix), understanding human speech (such as Siri and Alexa), self-driving cars (e.g., Tesla), automated decision-making and competing at the highest level in strategic game systems (such as chess and Go).
    """
    NoteController.add_note("AI Definition", long_text)
    
    NoteController.add_note("Shopping List", "Milk, Eggs, Bread, Butter")
    
    # Reminders
    print("Adding reminders...")
    now = datetime.now()
    future = now + timedelta(days=1)
    past = now - timedelta(hours=1)
    
    ReminderController.add_reminder("Doctor Appointment", future.strftime("%Y-%m-%d %H:%M"))
    ReminderController.add_reminder("Meeting with team", past.strftime("%Y-%m-%d %H:%M")) # Should trigger notification

    print("Example data created.")

if __name__ == "__main__":
    create_data()

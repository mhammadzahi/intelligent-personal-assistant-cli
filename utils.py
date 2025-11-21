from datetime import datetime

def parse_date(date_str: str) -> datetime:
    """Parses a date string into a datetime object.
    Supported formats: YYYY-MM-DD HH:MM, YYYY-MM-DD
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD or YYYY-MM-DD HH:MM")

def format_date(dt: datetime) -> str:
    """Formats a datetime object to string."""
    return dt.strftime("%Y-%m-%d %H:%M")

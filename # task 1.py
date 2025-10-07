# task 1
from datetime import datetime

def get_days_from_today(date):
    """
    Обчислює кількість днів між заданою датою та поточною датою.
    """
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        # Якщо користувач ввів дату у неправильному форматі
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

print(get_days_from_today("2025-10-09"))
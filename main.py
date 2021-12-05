from application.salary import calculate_salary as salary
from application.db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    print('Запуск программы: ', datetime.now())
    salary()
    get_employees()
    print('Расчет завершен: ', datetime.now())
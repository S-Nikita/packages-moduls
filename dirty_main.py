from application.salary import *
from application.db.people import *
from datetime import *


if __name__ == '__main__':
    print('Запуск программы: ', datetime.now())
    calculate_salary()
    get_employees()
    print('Расчет завершен: ', datetime.now())
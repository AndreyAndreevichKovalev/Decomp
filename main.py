from datetime import datetime
from prettytable import PrettyTable
from application.salary import calculate_salary
from application.db.people import get_employees


table = PrettyTable()
def print_table():
    table.field_names = [res_str]
    print(table)

if __name__ == '__main__':
    dt = datetime.today()
    res_str = datetime.strftime(dt, '%A, %B %d, %Y')
    print_table()
    calculate_salary()
    get_employees()

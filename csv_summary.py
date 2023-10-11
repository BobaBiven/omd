import csv


def get_csv_data(input_line: str, delimiter: str):
    '''Gets data from csv file'''
    with open(input_line, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=delimiter)
        next(data)
        return list(data)


def save_as_csv(data: dict, name: str = 'report.csv'):
    '''Saves report as csv'''
    with open(name, 'w', newline='') as csvfile:
        report = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        report.writerow(['Департмаент', 'Количество работников',
                         'Средняя з/п', 'з/п низ', 'з/п верх'])
        for k, v in data.items():
            report.writerow([k,
                             v['number_of_staff'],
                             round(v['total_salary'] / v['number_of_staff']),
                             v['min_salary'],
                             v['max_salary']])


def hierarchy(input_line: str = 'Corp_Summary.csv', delimiter: str = ';'):
    '''Outputs hierarchy of teams'''
    data = get_csv_data(input_line, delimiter)

    departments = {}
    for line in data:
        if line[1] not in departments:
            departments[line[1]] = [line[2]]
        else:
            if line[2] not in departments[line[1]]:
                departments[line[1]].append(line[2])

    print('В компании следующая иерархия команд:')
    for k, v in departments.items():
        print(k, '-', ', '.join(str(x) for x in v))


def create_report(input_line: str = 'Corp_Summary.csv', delimiter: str = ';') -> dict:
    '''Creates report'''
    data = get_csv_data(input_line, delimiter)

    departments = {}
    for line in data:
        if line[1] not in departments:
            tmp = {'total_salary': int(line[5]), 'number_of_staff': 1,
                   'max_salary': int(line[5]), 'min_salary': int(line[5])}
            departments[line[1]] = tmp
        else:
            departments[line[1]]['number_of_staff'] += 1
            departments[line[1]]['total_salary'] += int(line[5])
            departments[line[1]]['max_salary'] = max(int(line[5]), departments[line[1]]['max_salary'])
            departments[line[1]]['min_salary'] = min(int(line[5]), departments[line[1]]['min_salary'])

    return departments


def print_report(data: dict):
    '''Prints report in console'''
    print('Отчёт по командам:')
    for k, v in data.items():
        print(k, '\n\tКоличество работников: ', v['number_of_staff'],
              '\n\tСредняя з/п: ', v['total_salary'] / v['number_of_staff'],
              '\n\tВилка: ', v['min_salary'], '--', v['max_salary'])


def start():
    '''Starting function'''
    print('Выберете функцию:')
    print('1: Вывести иерархию команд')
    print('2: Вывести отчёт по департаментам')
    print('3: Сохранить сводный отчёт в виде csv-файла')
    t = int(input())
    if t == 1:
        hierarchy()
    if t == 2:
        print_report(create_report())
    if t == 3:
        save_as_csv(create_report())


if __name__ == '__main__':
    start()

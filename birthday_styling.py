from datetime import datetime

# Ввод данных от пользователя
day = int(input("Введите день рождения (дд): "))
month = int(input("Введите месяц рождения (мм): "))
year = int(input("Введите год рождения (гггг): "))

# Функция определения дня недели
def get_weekday(day, month, year):
    date = datetime(year, month, day)
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return weekdays[date.weekday()]

# Функция проверки високосного года
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Функция вычисления возраста
def calculate_age(day, month, year):
    today = datetime.now()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

# Функция вывода даты рождения в формате дд мм гггг, цифры прорисованы звёздочками (*)
def print_date_in_stars(day, month, year):
    digit_map = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", "   ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "*   *", "   * ", "  *  ", "*****"],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["   * ", "   ", " * * ", "*****", "   * "],
        '5': ["*****", "*    ", "**** ", "    *", " *** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "]
    }
    
    date_str = f"{day:02d}{month:02d}{year}"
    
    for i in range(5):  # 5 строк для отображения каждой цифры
        line = ""
        for digit in date_str:
            if digit != " ":
                line += digit_map[digit][i] + "  "
        print(line)

# Вывод результатов
weekday = get_weekday(day, month, year)
leap_year = is_leap_year(year)
age = calculate_age(day, month, year)

print(f"\nВы родились в {weekday}.")
print(f"Год рождения {'високосный' if leap_year else 'не високосный'}.")
print(f"Вам {age} лет.")

print("\nВаша дата рождения:")
print_date_in_stars(day, month, year)
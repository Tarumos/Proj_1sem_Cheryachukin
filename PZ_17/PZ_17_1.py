# Вариант 29
# создайте класс "Календарь", который имеет атрибуты год, месяц и день. Добавьте методы для определения дня недели,
# проверки на високосный год и определения количества дней в месяце
import datetime


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_of_week(self):
        date_obj = datetime.date(self.year, self.month, self.day)
        return date_obj.strftime("%A")

    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def days_in_month(self):
        if self.month == 2:  # февраль
            if self.is_leap_year():
                return 29
            else:
                return 28
        elif self.month in [4, 6, 9, 11]:  # апрель, июнь, сентябрь, октябрь
            return 30
        else:
            return 31


my_calendar = Calendar(2023, 4, 23)

print("День недели:", my_calendar.day_of_week())
print("Високосный год:", my_calendar.is_leap_year())
print("Количество дней в месяце:", my_calendar.days_in_month())

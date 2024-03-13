def read_data(filename):
    '''
    Чтение примера из файла filename
    '''
    with open(filename, encoding = 'utf-8') as file:
        text = [line.replace("\n", "") for line in file]
        solve = text[0].split() #Разбиваем запись на отдельные слова
    return solve

def math(numbers, solve):
    """
    Переводит слова в числа и производит их подсчёт
    """
    number1 = 0 #Первое число для рассчета
    number2 = 0 #Второе число для рассчета
    minus = 0 #Отрицательное число или нет, 0 - нет, 1 - да
    flag = 0 #Какое действие будет выполняться и также определяет первое ли это действие в примере, 0 - первое действие
    #1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление
    for i in range(len(solve)): #Просмотр всех слов в примере
        if solve[i] != "на": #Никак не используем "на"
            if solve[i] == "минус" and i == 0:
                minus = 1
            elif solve[i] in numbers and flag == 0: #Если до этого не было вычислений
                number1 += numbers[solve[i]] #Составляем число из слов
            elif solve[i] in numbers and flag != 0: #Если до этого были вычисления
                number2 += numbers[solve[i]] #Составляем число из слов
            elif solve[i] == "плюс":
                if flag != 0: #Если посчитали два числа и дошли до следующего действия
                    if minus == 1: #Добавляем минус к числу
                        number2 = str(number2)
                        number2 = "-" + number2
                        number2 = int(number2)
                        minus = 0
                    number1 += number2 #Совершаем предыдущее действие
                    number2 = 0 #Для следующего числа
                    flag = 1 #Сложение
                else: #Если действие первое
                    if minus == 1: #Добавляем минус к числу
                        number1 = str(number1)
                        number1 = "-" + number1
                        number1 = int(number1)
                        minus = 0
                    flag = 1 #Сложение
#Аналогично для других действий
            elif solve[i] == "минус":
                if flag != 0:
                    if minus == 1:
                        number2 = str(number2)
                        number2 = "-" + number2
                        number2 = int(number2)
                        minus = 0
                    number1 -= number2
                    number2 = 0
                    flag = 2
                else:
                    if minus == 1:
                        number1 = str(number1)
                        number1 = "-" + number1
                        number1 = int(number1)
                        minus = 0
                    flag = 2
            elif solve[i] == "умножить":
                if flag != 0:
                    if minus == 1:
                        number2 = str(number2)
                        number2 = "-" + number2
                        number2 = int(number2)
                        minus = 0
                    number1 *= number2
                    number2 = 0
                    flag = 3
                else:
                    if minus == 1:
                        number1 = str(number1)
                        number1 = "-" + number1
                        number1 = int(number1)
                        minus = 0
                    flag = 3
            elif solve[i] == "поделить":
                if flag != 0:
                    if minus == 1:
                        number2 = str(number2)
                        number2 = "-" + number2
                        number2 = int(number2)
                        minus = 0
                    number1 /= number2
                    number2 = 0
                    flag = 4
                else:
                    if minus == 1:
                        number1 = str(number1)
                        number1 = "-" + number1
                        number1 = int(number1)
                        minus = 0
                    flag = 4
#Если у нас только одно действие в примере и также считает последнее действие
    if flag == 1:
        number1 += number2
    if flag == 2:
        number1 -= number2
    if flag == 3:
        number1 *= number2
    if flag == 4:
        number1 /= number2
    return number1
def main():
    '''
        Основная функция программы.

        numbers -- Словарь с разными вариациями записи чисел
        i -- индекс слова в записи
        '''
    numbers = {
              'один': 1,           'два': 2,           'три': 3,
              'четыре': 4,         'пять': 5,          'шесть': 6,
              'семь': 7,           'восемь': 8,        'девять': 9,
              'десять': 10,        'одиннадцать': 11,  'двенадцать': 12,
              'тринадцать': 13,    'четырнадцать': 14, 'пятнадцать': 15,
              'шестнадцать': 16,   'семнадцать': 17,   'восемнадцать': 18,
              'девятнадцать': 19,  'двадцать': 20,     'тридцать': 30,
              'сорок': 40,         'пятьдесят': 50,    'шестьдесят': 60,
              'семьдесят': 70,     'восемьдесят': 80,  'девяносто': 90,
              'сто': 100,          'двести': 200,      'триста': 300,
              'четыреста': 400,    'пятьсот': 500,     'шестьсот': 600,
              'семьсот': 700,      'восемьсот': 800,   'девятьсот': 900}

    solve = read_data("input.txt") #Считываем пример из файла
    answer = math(numbers, solve) #Подсчет примера
    print(answer) #Вывод ответа

main()
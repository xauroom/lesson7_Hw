########################################################################################################################
#
#       Шифровальная машина Encrip
#       Начало работы: 30.04.2023
#       © Ржевский С.Н.
#
########################################################################################################################

########################################################
#   Функция перевода чисел в 36-ю систему счисления
########################################################

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        n = int(number % base)
        result = digits[n] + result
        number //= base
    return result.upper() if upper else result

########################################################
#   Алгоритм шифрования
########################################################


def encripting_func():
    encripting_text = ""                                # Объявление строковой переменной для хранения текста
    print('Шифрование\n')
    print('Ввод текста из файла (нажмите F) или с клавы (нажмите K)?\n')
    vvod = input()
    vvod = vvod.upper()
    if vvod == 'K': encripting_text = input("введите текст для шифрования:\n")
    elif vvod == 'F':
        print('Введите путь и имя файла\n')
        file_name = input()
        with open(file_name) as f:      # Считываем файл в переменную encripting_text
            encripting_text = f.read()
            print(encripting_text)
    
    #   Разбиваем фразу на отдельные слова
    word_list = encripting_text.split()
    #   Предлагаем пользователю ввести ключевую фразу
    key_string = input("введите ключевую фразу из одного или нескольких слов без знаков пунктуации:\n")
    #   Разбиваем фразу на отдельные слова
    key_list = key_string.split()
    #   Вычисляем количество слов в ключевой фразе
    keys_number = len(key_list)
    
    output_text = ""
    cycl = 0
    m = keys_number                             # число слов в ключевой фразе (тексте)
    for word in range(len(word_list)):          # Для каждого шифруемого слова
        w10 = int(word_list[word], 36)          # Перевод слова в десятичное число
        # print('цикл: ', cycl)
        if word >= m and (word - m * cycl) >= m:    # Если шифруемый текст длинней ключевой фразы (что чаще и бывает)
            cycl += 1                           # Когда досчитали ключевые слова до конца, начинаем новый цикл счета
            # print('следующий цикл: ', cycl)
        n = word - m * cycl                     # Определяем номер ключевого слова
        k10 = int(key_list[n], 36)              # Перевод ключевого слова в десятичное число
        encript10 = w10 * k10                   # Вычисление десятичного соответствия шифруемого слова
        encript = convert_to(encript10, 36)     # Зашифрованное слово

        output_text += encript
        output_text += sep                      # Добавляем разделитель (задан в блоке main, по умолчанию - пробел)
    
    print('\n# Зашифрованный текст:\n')
    for x in format_func(output_text, len(output_text)): print(x)   # Выводим текст в виде страницы шириной 80 символов
    print('\n')
    return output_text

########################################################
#   Форматирование выводимого текста 
########################################################


def format_func(text, len_of_text):
    std_len = 80                                        # Задаем длину стандартную длину строки на вывод в 80 символов
    format_text = [c for c in text]                     # Преобразуем текст в список символов
    i = 0
    j = 0
    while len_of_text >= std_len:                       # Нарезаем текст на строки по 80 символов
        format_text[j] = text[i:(i + std_len)]
        i += std_len
        j += 1
        len_of_text -= std_len
    else:
        format_text[j] = text[i:]

    format_text = format_text[0:j+1]                    # Формируем страницу шириной 80 символов из j строк
    return format_text

########################################################
#   Алгоритм дешифровки
########################################################


def excripting_func():
    excripting_text = ""                                # Объявление строковой переменной для хранения текста
    print('Дешифровка')
    print('Ввод текста из файла (нажмите F) или с клавы (нажмите K)?\n')
    vvod = input()
    vvod = vvod.upper()
    if vvod == 'K': excripting_text = input("введите текст для расшифровки:\n")
    elif vvod == 'F':
        print('Введите путь и имя файла\n')
        file_name = input()
        with open(file_name) as f:        # Считываем файл в переменную encripting_text
            excripting_text = f.read()
            print(excripting_text)
    
    #   Разбиваем фразу на отдельные слова
    word_list = excripting_text.split()
    #   Предлагаем пользователю ввести ключевую фразу
    key_string = input("введите ключевую фразу из одного или нескольких слов без знаков пунктуации:\n")
    #   Разбиваем фразу на отдельные слова
    key_list = key_string.split()
    #   Вычисляем количество слов в ключевой фразе
    keys_number = len(key_list)

    output_text = ""
    cycl = 0
    m = keys_number                             # число слов в ключевой фразе
    for word in range(len(word_list)):          # Для каждого дешифруемого слова
        w10 = int(word_list[word], 36)          # Перевод слова в десятичное число
        # print('цикл: ', cycl)
        if word >= m and (word - m * cycl) >= m:     # Если дешифруемый текст длинней ключевой фразы
            cycl += 1                           # Когда досчитали ключевые слова до конца, начинаем новый цикл счета
            # print('следующий цикл: ', cycl)
        n = word - m * cycl                     # Определяем номер ключевого слова
        k10 = int(key_list[n], 36)              # Перевод ключевого слова в десятичное число
        decript10 = w10 / k10                   # Вычисление десятичного соответствия дешифруемого слова
        decript = convert_to(decript10, 36)     # Расшифрованное слово

        output_text += decript
        output_text += sep                      # Добавляем разделитель
     
    print('\n#    Расшифрованный текст:\n')
    for x in format_func(output_text, len(output_text)): print(x) # Выводим текст в виде страницы шириной 80 символов
    print('\n')
    return output_text

########################################################
#   Интерфейс 
########################################################

########################################################
#   Main
########################################################

output_ = ""
sep = " "
data = {'E': 'Шифрование', 'D': 'Дешифровка', 'X': 'Выход', 'C': 'Продолжение', 'F': 'Запись'}
meth = ""
while True:
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!   Вас приветствует шифровальная машина Encrip 1.0   !')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    print('Что Вы хотите сделать?')
    print('    Зашифровать текст - введите "E"')
    print('    Расшифровать текст - введите "D"')
    print('    Выйти из программы - нажмите "X"')
    method = input('>>  ')
    letter = method.upper()
    
    if letter == "X": exit()
    elif letter == "E":
        output_ = encripting_func()
        meth = 'E'           # Запоминаем, что мы сделали
    elif letter == "D":
        output_ = excripting_func()
        meth = 'D'           # Запоминаем, что мы сделали
    else:
        print("Неправильная команда. Попробуйте еще раз")
        continue
   
    print('Записать в файл? - Нажмите "F"')
    print('Хотите начать заново? - Нажмите "C"')
    print('Для выхода нажмите "X"')
    method = input('>>  ')
    letter = method.upper()
    print(data[letter])

    
    if letter == "F":       # Выводим результат в файл:
        if meth == "E":     # зашифрованный текст
            with open("_encripting.txt", "w") as file: file.write(output_)
        elif meth == "D":   # расшифрованный текст
            with open("_decripting.txt", "w") as file: file.write(output_)
        else: print('Что-то пошло не так. ', letter)
    
    if letter == "C": continue
    else: exit()

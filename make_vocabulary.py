import sys
file_name = ''
try:
    file_name = sys.argv[1]
except IndexError:
    exit(1)                 # "файл или директория не существует"

try:
    file_text = open(file_name, 'r')
    words = ''
    for line in file_text:
        words = line
    print(words)
    file_text.close()
    exit(0)
except FileNotFoundError:
    exit(1)                 # "файл или директория не существует"
except IsADirectoryError:
    exit(2)                 # "ожидался файл, но это директория"
except PermissionError:
    exit(3)                 # "не хватает прав доступа"
except TimeoutError:
    exit(4)                 # "закончилось время ожидания"

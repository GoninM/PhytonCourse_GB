# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.


words_in_str = []

with open('task2_in.txt', 'r') as f_obj:
    string_counter = 0
    for line in f_obj:
        string_counter += 1
        words_in_str.append((string_counter, len(line.split())))

for n1, n2 in words_in_str:
    print(f'в строке {n1} содержится {n2} слов')


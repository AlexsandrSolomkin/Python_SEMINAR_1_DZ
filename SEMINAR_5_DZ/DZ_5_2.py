# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

# =============================================================================

# Решение:

from itertools import groupby, starmap
from os import path


def create_record_file(start_file: str, name_record_file: str):

    # Проверка, существует ли файл, с которым мы хотим взаимодействовать 
    if path.exists(start_file):
        with open(start_file) as my_f_1, \
                open(name_record_file, "a", encoding="utf-8") as my_f_2:
            for i in my_f_1:
                # Цикл проходит построчно файл, и записывает кол. один.
                # симв. подряд, строка: "ааааАааа", после обработки будет: "4a1A3a"
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")


def create_decode_file(rle_file: str):
    
    # Проверка, существует ли файл, с которым мы хотим взаимодействовать
    if path.exists(rle_file):
        with open(rle_file) as my_f:
            n = ""
            for k in my_f:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += 1
                    else:
                        # Фиксирование точного кол. симв. числа 
                        # т.к. может быть больше 9 подряд одинаковых символов
                        word_nums.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("The files do not exist in the system!")



# open_f = input("Enter the name of the file with the text: ")
# record_f = input("Enter the file name to record: ")
# decode_f = input("Enter the name of the file to decode: ")

# =============================================================================
